import csv
import math

from scripts.hist_writer import write_bins


def convert_csv_to_xml(filename: str, out_name: str):
    # Read the file as csv
    final_rows = [{
        'count': 0,
        'lower_bound': -math.inf,
        'upper_bound': math.inf
    }]

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header
        next(reader, None)
        # Read the rows
        for row in reader:
            final_rows.append({
                'count': int(row[0]),
                'lower_bound': str(float(row[2])) + "us",
                'upper_bound': str(float(row[3])) + "us"
            })

    final_rows[0]['upper_bound'] = final_rows[1]['lower_bound']
    final_rows.append({
        'count': 0,
        'lower_bound': final_rows[-1]['upper_bound'],
        'upper_bound': math.inf
    })

    write_bins(final_rows, out_name)


