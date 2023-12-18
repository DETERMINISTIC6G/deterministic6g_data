import math
import re

import matplotlib.pyplot as plt
import numpy as np

from scripts.hist_writer import write_bins, np_hist_to_bins


def extract_time(line):
    pattern = r'time=([\d.]+)\s*([a-zA-Z]+)'
    match = re.search(pattern, line)
    if match:
        time_value, unit = match.groups()
        return time_value, unit
    else:
        return None


def convert_pingtxt_to_xml(filename: str, out_name: str):
    # Read the file as csv
    times = []
    lastUnit = None

    with open(filename) as file:
        for line in file:
            time = extract_time(line)
            # print(time)
            if time is not None:
                times.append(float(time[0]))
                if lastUnit is None:
                    lastUnit = time[1]
                elif time[1] != lastUnit:
                    raise "Different units not supported by this code yet"

    n, bins = np.histogram(times, bins="auto")
    # plt.hist(times, bins=bins)
    # plt.show()

    final_rows = np_hist_to_bins(n, bins, lastUnit)

    write_bins(final_rows, out_name)
