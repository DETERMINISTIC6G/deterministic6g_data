import numpy as np
import pandas as pd

from scripts.hist_writer import np_hist_to_bins, write_bins

if __name__ == '__main__':
    from scipy.stats import norm

    # Assuming a normal distribution
    median = 100  # Replace with your actual median
    std_dev = 50  # Replace with your actual standard deviation

    # Z-scores for 0.0005 and 0.9995
    z_score_lower = norm.ppf(0.0001)
    z_score_upper = norm.ppf(0.9999)

    # Calculate the boundaries
    lower_boundary = median + (z_score_lower * std_dev)
    upper_boundary = median + (z_score_upper * std_dev)

    print(f"The boundaries for 99.9% of the values are {lower_boundary} and {upper_boundary}.")

    upstream_file_nocross_vlan = "raw/upstream-nocross_vlan-10pkt_per_sec.csv"
    downstream_file_nocross_vlan = "raw/downstream-nocross_vlan-10pkt_per_sec.csv"

    colnames = ['t', 'pktid']
    df_upstream_nocross_vlan = pd.read_csv(upstream_file_nocross_vlan, names=colnames, header=None)
    df_downstream_nocross_vlan = pd.read_csv(downstream_file_nocross_vlan, names=colnames, header=None)

    df_nocross_vlan = pd.merge(df_upstream_nocross_vlan, df_downstream_nocross_vlan, on='pktid', how='left')
    df_nocross_vlan.insert(loc=3, column='latency', value=(df_nocross_vlan.t_y - df_nocross_vlan.t_x))

    latencies = df_nocross_vlan.latency

    n, bins = np.histogram(latencies, bins="auto")
    # plt.ylabel('Sample Count')
    # plt.xlabel('Packet Delay [ns]')
    # plt.title('Packet Delay -- w/o cross traffic, VLAN active')
    # plt.hist(df_nocross_vlan.latency, bins=bins)
    # plt.show()

    final_rows = np_hist_to_bins(n, bins, "ns")
    write_bins(final_rows, "df_nocross_vlan.xml")
