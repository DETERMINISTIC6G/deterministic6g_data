# ProcessingDelayDistribution2

The data set in this repository provides response time measurements of a cloudified application, considering the effect of the different delay components of the cloud execution environment, e.g., the application processing time, operating system, virtualization ecosystem, type of scheduling.

# Acknowledgments

The data set in this repository is provided by Ericsson as part of the DETERMINISTIC6G project, which has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No. 101096504.

[DETERMINISTIC6G Project Website](https://deterministic6g.eu/).

DETERMINISTIC6G e-mail: coordinator@deterministic6g.eu

# License

The data set is licensed under the [CC BY-ND 4.0 license](../LICENSE-CC-BY-ND.md).

If you use this data set in your published work, please cite the following paper:

G. P. Sharma, D. Patel, J. Sachs, M. De Andrade, J. Farkas, J. Harmatos, B. Varga, H. -P., Bernhard, R. Muzaffar, M. Ahmed, F. Dürr, D. Bruckner, E.M. De Oca, D. Houatra, H. Zhang and J. Gross: Toward Deterministic Communications in 6G Networks: State of the Art, Open Challenges and the Way Forward. IEEE Access, vol. 11, pp. 106898-106923, 2023, doi: 10.1109/ACCESS.2023.3316605

# Description of the measured data

The objective of this measurement experiment was to collect information about the response time of a cloudified application, considering the effect of the different delay components of the cloud execution environment, e.g., the application processing time, operating system, virtualization ecosystem, type of scheduling. 
An application was used to simulate a collaborative, cloud-based robot control application. The application comprises three components, arranged as a chain of functional steps of the application; the first component could simulate video-processing/object tracking module, the second component represented the collaborative robot control logic, while the third component modeled the low-level, individual robot control.

For the cloud infrastructure, a server with multiple CPU and Real-time Linux OS was used. The application components were deployed in docker containers, and multiple instances of the first and third components were deployed. In the used experiment each component had deterministic execution time.

The performance of two types of scheduling, namely SCHED_FIFO and SCHED_DEADLINE was compared, and the resulting histograms is based on cumulative results of multiple measurements. 
 
Further information can be found in the publicly available report of Deliverable D4.1, available from the website of the [DETERMINISTIC6G Project](https://deterministic6g.eu/)

# Data format

This repository contains the raw measurement in the [raw](raw) folder.

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
