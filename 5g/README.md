# 5G Measurement Data

The measurements were carried out in different rounds using the KTH EP5G setup.
For each round there are about 1M samples in total which are contained in different parquet files corresponding to different runs per round.
Each round corresponds to a combination of UE, packet interval and payload, etc.
A spreadsheet can be found in the shared directory where you can find which round corresponds to what combination.
A python code snippet (read_parquets.py) in the directory can be used to extract latencies from a directory containing parquet files.

_Due to its size the raw dataset is not included in this repository._