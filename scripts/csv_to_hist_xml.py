import csv
import math

import numpy as np
from matplotlib import pyplot as plt

from scripts.hist_writer import write_bins


def convert_pdd2_csv_to_xml(filename: str, out_name: str):
    # Read the file as csv
    final_rows = [{
        'count': 0,
        'lower_bound': -math.inf,
        'upper_bound': math.inf
    }]

    counts = []
    bin_edges = []
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
            counts += [int(row[0])]
            bin_edges += [float(row[2])]

    final_rows[0]['upper_bound'] = final_rows[1]['lower_bound']
    final_rows.append({
        'count': 0,
        'lower_bound': final_rows[-1]['upper_bound'],
        'upper_bound': math.inf
    })

    # Plot the histogram
    # plt.hist(bin_edges, weights=counts, bins=bin_edges)
    # plt.grid()
    # plt.xlabel("t in us")
    # plt.ylabel("count")
    # plt.show()

    write_bins(final_rows, out_name)


def convert_pdw5g_csv_to_xml(filename: str, out_name: str):
    # Read the file as csv
    final_rows = [{
        'count': 0,
        'lower_bound': str(-math.inf) + " ms",
        'upper_bound': str(math.inf) + " ms"
    }]

    counts = []
    bin_edges = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        # Skip the header
        next(reader, None)
        # Read the rows
        for row in reader:
            bound = str(row[0]) + " ms"
            count = float(row[1]) * 1e6
            final_rows[-1]['upper_bound'] = bound
            final_rows.append({
                'count': count,
                'lower_bound': bound,
            })
            counts += [count]
            bin_edges += [float(row[0])]


    # Plot the histogram
    # plt.hist(bin_edges, weights=counts, bins=bin_edges)
    # plt.grid()
    # plt.xlabel("t in us")
    # plt.ylabel("count")
    # plt.show()

    write_bins(final_rows, out_name)
