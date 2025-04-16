def analyze_gpx_track(gpx_file):
    
    with open(gpx_file, 'r', encoding='utf-8') as f:
        gpx = gpxpy.parse(f)

    filename = os.path.basename(gpx_file)
    points = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if point.elevation is not None:
                    points.append((point.latitude, point.longitude, point.elevation))

    if not points:
        print(f"No elevation data in {filename}")
        return {
            'name': filename,
            'elevation': None,
            'distance': None,
            'max_grade': None,
            'avg_grade': None
        }

    elevations = [p[2] for p in points]
    highest_elevation = max(elevations)

    total_distance_km = 0
    gradients = []

    for i in range(1, len(points)):
        p1 = (points[i-1][0], points[i-1][1])
        p2 = (points[i][0], points[i][1])

        dist_km = geodesic(p1, p2).kilometers
        dist_m = dist_km * 1000

        if dist_m < 1:
            continue

        total_distance_km += dist_km
        elevation_diff = points[i][2] - points[i-1][2]

        if dist_m >= 5:
            grade = (elevation_diff / dist_m) * 100
            if abs(grade) <= 30:
                gradients.append(grade)

    uphill = [g for g in gradients if g > 0]
    max_grade = max(uphill) if uphill else 0
    avg_grade = sum(uphill) / len(uphill) if uphill else 0

    return {
        'name': filename,
        'elevation': round(highest_elevation, 1),
        'distance': round(total_distance_km, 2),
        'max_grade': round(max_grade, 1),
        'avg_grade': round(avg_grade, 1)
    }
