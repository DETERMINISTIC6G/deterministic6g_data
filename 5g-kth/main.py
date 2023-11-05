import numpy as np
from matplotlib import pyplot as plt

from scripts.hist_writer import np_hist_to_bins, write_bins
from scripts.read_parquets import get_combined_df_from_parquets

data_dir = "/home/haugls/Downloads/EP5G_USTUTT/"
subdirs = ["s1", "s10-DL"]

if __name__ == '__main__':
    result = get_combined_df_from_parquets(data_dir, subdirs)
    # TODO: What is the monotonic latency?
    for key, value in result.items():
        wall_latencies = value["wall_latency"]
        monotonic_latencies = value["monotonic_latency"]

        n_wall, bins_wall = np.histogram(wall_latencies, bins="auto")
        # n_monotonic, bins_monotonic = np.histogram(monotonic_latencies, bins="auto")

        plt.hist(wall_latencies, bins=bins_wall)
        plt.title(key + " wall")
        plt.xlabel("ms")
        plt.xlim(0, 14)
        plt.show()

        # plt.hist(monotonic_latencies, bins=bins_monotonic)
        # plt.title(key + " monotonic")
        # plt.xlabel("ms")
        # plt.show()

        rows_wall = np_hist_to_bins(n_wall, bins_wall, "ms")
        # rows_monotonic = np_hist_to_bins(n_monotonic, bins_monotonic, "ms")

        write_bins(rows_wall, key + "_wall.xml")
        # write_bins(rows_monotonic, key + "_monotonic.xml")
