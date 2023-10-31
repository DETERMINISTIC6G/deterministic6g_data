import os
import pyarrow.parquet as pq
import pandas as pd
import numpy as np


def get_combined_df_from_parquets(parent_directory, subdirectories):
    # Iterate through subdirectories and process Parquet files in each
    dfs_by_directory = {}
    for subdirectory in subdirectories:
        print(f"In subdirectory {subdirectory}")
        subdirectory_path = os.path.join(parent_directory, subdirectory)
        parquet_files = [f for f in os.listdir(subdirectory_path) if f.endswith('.parquet')]
        tables = [pq.read_table(os.path.join(subdirectory_path, file)) for file in parquet_files]
        dataframes = [table.to_pandas() for table in tables]

        # Add a new column with the name of the Parquet file
        file_names = [os.path.splitext(file)[0] for file in parquet_files]
        for i, df in enumerate(dataframes):
            df['parquet_file'] = file_names[i]

        combined_df = pd.concat(dataframes, ignore_index=True)
        # Calculate wall latency (timestamps.client.send.wall - timestamps.server.receive.wall)
        combined_df['wall_latency'] = (combined_df['timestamps.server.receive.wall'] - combined_df[
            'timestamps.client.send.wall']) / 1e6
        # Calculate monotonic latency (timestamps.client.send.monotonic - timestamps.server.receive.monotonic)
        combined_df['monotonic_latency'] = (combined_df['timestamps.server.receive.monotonic'] - combined_df[
            'timestamps.client.send.monotonic']) / 1e6
        dfs_by_directory[subdirectory] = combined_df
    return dfs_by_directory
