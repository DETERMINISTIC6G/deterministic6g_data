# PD-Wireless-5G-2a

The data set in this repository provides packet delay data of a wireless TSN bridge based on measurements from a 5G testbed in an industrial research shopfloor.

## Acknowledgments

The measurements have been made in a collaboration of Ericsson and the Fraunhofer Institute for Production Technology.

The data set in this repository is provided as part of the DETERMINISTIC6G project, which has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No. 101096504.

[DETERMINISTIC6G Project Website](https://deterministic6g.eu/).

DETERMINISTIC6G e-mail: coordinator@deterministic6g.eu

## License

The data set is licensed under the [CC BY-ND 4.0 license](../LICENSE-CC-BY-ND.md).

If you use this data set in your published work, please cite the following report:
J. Ansari, J. Sachs, Contribution of 5G Packet Delay Data Set “PD-Wireless-5G-2a”, in DETERMINISTIC6G deliverable D4.1, “Digest on First DetCom Simulator Framework Release,” December 2024

## Description of the measured data

The provided data describes the packet delay (PD) of a wireless TSN bridge based on measurements from a 5G testbed in an industrial research shopfloor. The 5G testbed corresponds to a 5G standalone trial network with 100 MHz carrier bandwidth operating in the 3.7 GHz band. It is deployed at the 5G Industry Campus Europe in Aachen Germany . The network setup and the measurement methodology are further described in [\[AAB+22\]](#references).

Two histogram data sets have been derived from measurements in the trial network, one measurement for downlink (from a controller to a mobile device over the 5G network) and one measurement for uplink (from the mobile device over 5G to the controller). The measurements are made for periodic PROFINET messages of 100 bytes size that are transmitted every 10 ms.
 
Further information can be found in the publicly available report of Deliverable D4.1, available from the website of the [DETERMINISTIC6G Project](https://deterministic6g.eu/)

## Data format

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

## References

[AAB+22] J. Ansari, C. Andersson, P. de Bruin, J. Farkas, L. Grosjean, J. Sachs, J. Torsner, B. Varga, D. Harutyunyan, N. König, R. H. Schmitt: Performance of 5G Trials for Industrial Automation. Electronics, 11(3):412, 2022, DOI: 10.3390/electronics11030412