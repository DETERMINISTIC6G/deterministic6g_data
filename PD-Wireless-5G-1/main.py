import numpy as np
import requests
import zipfile
import os

from scripts.hist_writer import np_hist_to_bins, write_bins, write_traces
from scripts.read_parquets import get_combined_df_from_parquets
import matplotlib.pyplot as plt

import urllib.request


def download_file(url, dest_path):
    response = urllib.request.urlopen(url)
    total_size = response.getheader('Content-Length')
    if total_size is None:  # No content size header
        print('Downloading file...')
        with open(dest_path, 'wb') as f:
            f.write(response.read())
    else:
        total_size = int(total_size)
        downloaded_size = 0
        print('Downloading file of size: {} bytes'.format(total_size))
        with open(dest_path, 'wb') as f:
            while True:
                chunk = response.read(8192)
                downloaded_size += len(chunk)
                done = int(50 * downloaded_size / total_size)
                print('\r[{}{}]'.format('█' * done, '.' * (50 - done)), end='')
                if not chunk:
                    break
                f.write(chunk)
        print()


def main():
    # Download from
    tmp_dir = "tmp"
    subdirs = ["s1-UL", "s10-DL"]
    zenodo_record_id = '10390211'
    filename = 'COTS5G%20measurements.zip'
    dl_url = f'https://zenodo.org/record/{zenodo_record_id}/files/{filename}?download=1'
    dl_file = f'{tmp_dir}/{zenodo_record_id}.zip'

    # Create data_dir if not exists
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    if not os.path.exists(dl_file):
        print("Downloading file...")
        # Download file
        download_file(dl_url, dl_file)

    # Unzip file
    with zipfile.ZipFile(dl_file, 'r') as zip_ref:
        zip_ref.extractall(tmp_dir)

    data_dir = f'{tmp_dir}/COTS5G measurements'

    result = get_combined_df_from_parquets(data_dir, subdirs)
    # TODO: What is the monotonic latency?

    for key, value in result.items():
        wall_latencies = value["wall_latency"]
        monotonic_latencies = value["monotonic_latency"]

        n_wall, bins_wall = np.histogram(wall_latencies, bins="auto")
        # n_monotonic, bins_monotonic = np.histogram(monotonic_latencies, bins="auto")

        # plt.hist(wall_latencies, bins=bins_wall)
        # plt.gcf().set_figwidth(6.4)
        # plt.gcf().set_figheight(4.8)
        # plt.title(key)
        # #if key == "s10-DL":
        #    # plt.title("Downlink")
        # # elif key == "s1":
        # #    plt.title("Uplink")
        # #plt.xlabel("t in ms")
        # #plt.ylabel("count")
        #
        # plt.xlim(0,14)
        # plt.grid()
        # plt.xlabel("delay [us]")
        # plt.ylabel("sample count")
        # print(f"Default figure size: {plt.rcParams['figure.figsize']} inches")
        # plt.savefig(f'{tmp_dir}/{key}.png')
        # plt.show()



        # plt.hist(monotonic_latencies, bins=bins_monotonic)
        # plt.title(key + " monotonic")
        # plt.xlabel("ms")
        # plt.show()

        rows_wall = np_hist_to_bins(n_wall, bins_wall, "ms")
        # rows_monotonic = np_hist_to_bins(n_monotonic, bins_monotonic, "ms")

        write_bins(rows_wall, key + "_wall.xml")
        write_traces(wall_latencies, out_name = key + "_trace.csv")
        write_traces(wall_latencies, value["timestamps.client.send.monotonic"], key + "_trace_timestamped.csv")
        # write_bins(rows_monotonic, key + ".xml")


if __name__ == '__main__':
    main()
