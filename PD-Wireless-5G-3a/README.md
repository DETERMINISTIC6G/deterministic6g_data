# PD-Wireless-5G-3a

he data set in this repository provides packet delay data of a wireless TSN bridge based on measurements from a 5G testbed implementing standardized functionality for ultra-reliable and low latency communication in an industrial research shopfloor.

# Acknowledgments

The measurements have been made in a collaboration of Ericsson and the Fraunhofer Institute for Production Technology.

The data set in this repository is provided as part of the DETERMINISTIC6G project, which has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No. 101096504.

[DETERMINISTIC6G Project Website](https://deterministic6g.eu/).

DETERMINISTIC6G e-mail: coordinator@deterministic6g.eu

# License

The data set is licensed under the [CC BY-ND 4.0 license](../LICENSE-CC-BY-ND.md).

If you use this data set in your published work, please cite the following paper:

J. Ansari, C. Andersson, P. de Bruin, J. Farkas, L. Grosjean, J. Sachs, J. Torsner, B. Varga, D. Harutyunyan, N. König, R. H. Schmitt: Performance of 5G Trials for Industrial Automation. Electronics, 11(3):412, 2022, DOI: 10.3390/electronics11030412

# Description of the measured data

The data set described the packet delay (PD) of a wireless TSN bridge based on measurements from a 5G testbed in an industrial research shopfloor. The 5G testbed corresponds to a pre-commercial 5G URLLC standalone prototype network with 100 MHz carrier bandwidth operating in the 28 GHz band; it implements 5G standardized functionality for ultra-reliable and low latency communication [\[AVK+22\]](#references).
The trial network is deployed at the 5G Industry Campus Europe in Aachen Germany. The network setup and the measurement methodology are further described in [\[AAB+22\]](#references) and in [\[AVK+22\]](#references).
Two histogram data sets have been derived from measurements in the trial network, one measurement for downlink and one measurement for uplink. The measurements are made for periodic UDP messages with 32 bytes payload that are transmitted every 7 ms.
 
Further information can be found in the publicly available report of Deliverable D4.1, available from the website of the [DETERMINISTIC6G Project](https://deterministic6g.eu/)

# Data format

This repository contains the measurement data in the [raw](raw) folder.
This measurement data is provided in the CSV format, where each row corresponds to a bin with its lower bound and relative count.

The [main.py](main.py) script processes the raw data and converts it to a Histogram which can be user by the OMNeT++ simulation framework.

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

# References

[AAB+22] J. Ansari, C. Andersson, P. de Bruin, J. Farkas, L. Grosjean, J. Sachs, J. Torsner, B. Varga, D. Harutyunyan, N. König, R. H. Schmitt: Performance of 5G Trials for Industrial Automation. Electronics, 11(3):412, 2022, DOI: 10.3390/electronics11030412

[AVK+22] J. Ansari, B. Varga, P. Kehl, N. König, R. H. Schmitt: 5G and TSN integrated prototype for flexible production. Presentation at TSN/A conference, Stuttgart, September 28-29, 2022 