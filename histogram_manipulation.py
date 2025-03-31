import csv
import os.path

import matplotlib.pyplot as plt
import math
import json
import numpy as np
from scipy.special import binom
import argparse
import xml.etree.ElementTree as ET

from scripts.hist_writer import np_hist_to_bins, write_bins


def reliability(data, N, rel):
    d = [0, math.inf]
    for i in range(len(data)):
        k = data[i][1]
        for j in range(i + 1, len(data)):
            if k >= N * rel:
                if data[j][0] - data[i][0] < d[1] - d[0]:
                    d = [data[i][0], data[j][0]]
                break
            k += data[j][1]
    return d


def get_bin_size(data):
    return data[-1][0] - data[-2][0]


def modify_histogram(data, total_count, pattern, pdc, vslot, name, savefig, showfig):
    bin_size = get_bin_size(data)

    if showfig:
        print("BEFORE", total_count)
        print("33.33% \t", reliability(data, total_count, 0.3333))
        print("50% \t", reliability(data, total_count, 0.5))
        print("90% \t", reliability(data, total_count, 0.90))
        print("99% \t", reliability(data, total_count, 0.99))
        print("99.9% \t", reliability(data, total_count, 0.999))
        print("99.99% \t", reliability(data, total_count, 0.9999))
        print(f"Bounds \t [{data[1][0]}, {data[-1][0]}]")

    if pdc > 0:
        plt.bar([d[0] for d in data[1:]], [d[1] for d in data[1:]], width=bin_size)
        k = 0
        while k / total_count < pdc and len(data) >= 2:
            k += data[1][1]
            data.pop(1)
        data[1][1] += k

        if vslot > 0:
            if len(data) < 3:
                data.append([0, 0])
            data[2][0] = data[1][0] + vslot / 1e3
    else:
        lower = data[1][0] - bin_size
        while lower > 0:
            data.insert(1, [round(lower, 3), 0])
            lower -= bin_size

        upper = data[-1][0] + bin_size
        while upper < 30:
            data.append([round(upper, 3), 0])
            upper += bin_size

        plt.bar([d[0] for d in data[1:]], [d[1] for d in data[1:]], width=bin_size)

        res = np.convolve([d[1] for d in data], pattern, mode="same")
        data = [[data[i][0], round(res[i])] for i in range(len(data))]
        last_i = max([i for i, d in enumerate(data) if d[1] != 0])
        data = data[: last_i + 1]
        total_count = sum([d[1] for d in data])

    if showfig:
        print("\nAFTER")
        print("33.33% \t", reliability(data, total_count, 0.3333))
        print("50% \t", reliability(data, total_count, 0.5))
        print("90% \t", reliability(data, total_count, 0.90))
        print("99% \t", reliability(data, total_count, 0.99))
        print("99.9% \t", reliability(data, total_count, 0.999))
        print("99.99% \t", reliability(data, total_count, 0.9999))
        print(f"Bounds \t [{data[1][0]}, {data[-1][0]}]")

    plt.bar([d[0] for d in data[1:]], [d[1] for d in data[1:]], width=bin_size)
    plt.xlabel("delay in ms")
    plt.ylabel("count")

    plt.ylim(0,15000000000)
    if showfig:
        plt.show()

    if savefig:
        plt.savefig(f"{name}.png")

        json_data = {
            "name": name,
            "data": [
                {
                    "count": data[i][1],
                    "lower_bound": f"{data[i][0]} ms",
                    "upper_bound": f"{data[i+1][0]} ms",
                }
                for i in range(len(data) - 1)
            ],
        }
        json_data["data"].append(
            {"count": data[-1][1], "lower_bound": f"{data[-1][0]} ms"}
        )
        with open(f"{name}.json", "w") as f:
            json.dump(json_data, f)

        data.append([data[-1][0] + bin_size, 0])

        xml_data = np_hist_to_bins(
            [d[1] for d in data[1:-1]], [d[0] for d in data[1:]], "ms"
        )
        write_bins(xml_data, f"{name}.xml")


def read_histogram(hist):
    # TODO: Fix that only ms as unit is supported atm
    if os.path.splitext(hist)[1] == ".xml":
        tree = ET.parse(hist)
        root = tree.getroot()

        data = []
        N = 0
        for child in root:
            if "." in child.text:
                count = float(child.text)
            else:
                count = int(child.text)
            if child.attrib["low"].endswith("ms"):
                data.append([float(child.attrib["low"][:-2]), count])
            else:
                raise ValueError("Only ms as unit is supported.")
            N += count

        return data, N
    elif os.path.splitext(hist)[1] == ".json":
        with open(hist) as f:
            j = json.load(f)

        data = []
        N = 0
        for d in j["data"]:
            data.append([float(d["lower_bound"].split(" ")[0]), d["count"]])
            N += d["count"]

        return data, N
    else:
        raise ValueError("Invalid filetype for histogram.")


def main():
    parser = argparse.ArgumentParser(
        description="Manipulate histogram by binomial convolution."
    )
    parser.add_argument(
        "-hist", "--hist", type=str, default="data/histograms/uplink_histogram.json"
    )
    parser.add_argument("-out", "--out", type=str, default=".")
    parser.add_argument("-name", "--name", type=str, default="")
    parser.add_argument("-shift", "--shift", type=float, default=0)
    parser.add_argument("-skew", "--skew", type=float, default=1 / 2)
    parser.add_argument("-dev", "--deviation", type=int, default=0)
    parser.add_argument("-mirror", "--mirror", action="store_true")
    parser.add_argument("-pdc", "--pdc", type=float, default=0)
    parser.add_argument("-vslot", "--vslot", type=int, default=0)
    parser.add_argument("-save", "--savefig", action="store_true")
    parser.add_argument("-show", "--showfig", action="store_true")
    args = parser.parse_args()

    data, total_count = read_histogram(args.hist)

    bin_size = get_bin_size(data)
    s = 2 * round(args.shift / bin_size)
    N = 2 * args.deviation
    p = args.skew
    pattern = np.zeros(abs(s) + N + 1)

    if not args.mirror:
        if s <= 0:
            pattern[: N + 1] = (
                [binom(N, k) * p**k * (1 - p) ** (N - k) for k in range(N + 1)]
                if N > 1
                else [1]
            )
        else:
            pattern[s:] = (
                [binom(N, k) * p**k * (1 - p) ** (N - k) for k in range(N + 1)]
                if N > 1
                else [1]
            )
    else:
        pattern[s:] = (
            [p * binom(N, k) * p**k * (1 - p) ** (N - k) for k in range(N + 1)]
            if N > 1
            else [1]
        )
        pattern[: N + 1] = (
            [(1 - p) * binom(N, k) * p**k * (1 - p) ** (N - k) for k in range(N + 1)]
            if N > 1
            else [1]
        )

    modify_histogram(
        data,
        total_count,
        pattern,
        args.pdc,
        args.vslot,
        (
            f"{args.out}/{args.hist.split('/')[-1].split('.')[0]}_conv_{args.shift}_{args.deviation}_{round(args.skew*100)}"
            if args.name == ""
            else f"{args.out}/{args.name}"
        ),
        args.savefig,
        args.showfig,
    )


if __name__ == "__main__":
    main()
