def analyze_all_gpx_files(folder):
    
    results = []
    files = glob.glob(os.path.join(folder, '*.gpx'))

    for file in files:
        print(f"🔍 Analyzing: {os.path.basename(file)}")
        try:
            result = analyze_gpx_track(file)
            results.append(result)
        except Exception as e:
            print(f"Error in {file}: {e}")

    output_file = os.path.join(folder, 'track_analysis.csv')

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['File', 'Highest Point (m)', 'Distance (km)', 'Max Grade (%)', 'Avg Grade (%)'])

        for entry in results:
            writer.writerow([
                entry['name'],
                entry['elevation'] if entry['elevation'] is not None else '',
                entry['distance'] if entry['distance'] is not None else '',
                entry['max_grade'] if entry['max_grade'] is not None else '',
                entry['avg_grade'] if entry['avg_grade'] is not None else ''
            ])

    print(f"\n Analysis complete – File saved: {output_file}")
