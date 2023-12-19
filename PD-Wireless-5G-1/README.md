# PD-Wireless-5G-1

The dataset contains the data collected during the latency measurements performed on a COTS 5G system.

## Acknowledgments

The data set in this repository is provided by University of Stuttgart as part of the DETERMINISTIC6G project, which has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No. 101096504.

[DETERMINISTIC6G Project Website](https://deterministic6g.eu/).

DETERMINISTIC6G e-mail: coordinator@deterministic6g.eu

## License

The data set is licensed under the [CC BY-SA 4.0 license](../LICENSE-CC-BY-SA.md).

If you use this data set in your published work, please cite the following paper:

G. P. Sharma, D. Patel, J. Sachs, M. De Andrade, J. Farkas, J. Harmatos, B. Varga, H. -P., Bernhard, R. Muzaffar, M. Ahmed, F. Dürr, D. Bruckner, E.M. De Oca, D. Houatra, H. Zhang and J. Gross: Toward Deterministic Communications in 6G Networks: State of the Art, Open Challenges and the Way Forward. IEEE Access, vol. 11, pp. 106898-106923, 2023, doi: 10.1109/ACCESS.2023.3316605

## Description of the measured data

The 5G network operates in band 78, in TDD mode, with a total of 106 PRBs which occupies 40 MHz of bandwidth.
The latency (one-way delay) samples were collected in both uplink and downlink directions using the irtt tool running on the end node (connected to the UE) and the edge node (connected to the 5G gateway).
The clocks in the 5G system, end node and edge node were precisely (<200ns) synchronized using Precision Time Protocol (PTP).
In addition to recording send and receive timestamps, various network conditions were also recorded for each latency sample.
The measurements were carried out in different sessions and for each session, there are about 1M samples in total which are contained in different parquet files corresponding to different rounds (30 mins) per session.
Each session corresponds to a combination of direction (uplink or downlink), UE device, a packet interval and payload length, etc. A spreadsheet (COTS5G measurement campaign.xlsx) in this directory contains the information detailed information on the combination for each session.


## Data format
The raw data can be found under this DOI: [10.5281/zenodo.10390211](https://doi.org/10.5281/zenodo.10390211)

The [main.py](main.py) script processes downloads and converts the raw data to a Histogram which can be user by the OMNeT++ simulation framework.

Each file describes a histogram of delay values, provided in XML format. An example histogram is shown next:

```xml
<histogram>
    <bin low="1ms">1</bin>
    <bin low="2ms">4</bin>
    <bin low="3ms">3</bin>
    <bin low="4ms">0</bin>
</histogram>
```

Each bin element covers a time interval ranging from value low to the low value of the next bin element and defines its value count as content of the element. The last element is only needed to define the upper bound of the last (previous) bin, and therefore, its count is always zero.
