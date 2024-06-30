import requests
import json
import pandas as pd

from dotenv import load_dotenv
import os

import dateparser

pd.set_option("display.max_rows", 500)

df_1 = pd.read_csv("data/csv/sh_interface_spine1_api.nxos.csv")
df_2 = pd.read_csv("data/csv/sh_interface_spine2_api.nxos.csv")

#
# Clean
#

# fmt: off
df_1 = (
    df_1

    # Fill in the missing values for the given columns
    .fillna({"eth_ip_mask": 0, "eth_mtu": 0, "eth_link_flapped": 0})

    # Convert the column types
    .astype({"eth_ip_mask": "int", "eth_mtu": "int", "eth_link_flapped": "str"})

    # Drop the 'eth_bw_str' column from the DataFrame in place
    .drop("eth_bw_str", axis=1)

    # Drop the 'Unnamed: 0' column from the DataFrame in place
    .drop("Unnamed: 0", axis=1)

    # Remove any text after the first space in the 'eth_speed' column in place
    .replace({"eth_speed": {r"^(.*?)\s.*$" : r"\1"}}, regex=True)
)
df_2 = (
    df_2

    # Fill in the missing values for the given columns
    .fillna({"eth_ip_mask": 0, "eth_mtu": 0, "eth_link_flapped": 0})

    # Convert the column types
    .astype({"eth_ip_mask": "int", "eth_mtu": "int", "eth_link_flapped": "str"})

    # Drop the 'eth_bw_str' column from the DataFrame in place
    .drop("eth_bw_str", axis=1)

    # Drop the 'Unnamed: 0' column from the DataFrame in place
    .drop("Unnamed: 0", axis=1)

    # Remove any text after the first space in the 'eth_speed' column in place
    .replace({"eth_speed": {r"^(.*?)\s.*$" : r"\1"}}, regex=True)
)
# fmt: on

#
# Manipulate
#

# Insert device column
df_1.insert(0, "device", "spine1")
df_2.insert(0, "device", "spine2")

# Concatenate both DataFrames together
df = pd.concat([df_1, df_2], ignore_index=True)

# Apply function to 'eth_link_flapped' to convert string to datetime64[ns] dtype
def convert_link_flap_to_date(row):
    return dateparser.parse(row["eth_link_flapped"])

# Add link_flapped datetime to new column
df["last_flap_date"] = df.apply(convert_link_flap_to_date, axis=1)

# Print the DataFrame
print(df)

# Show an iloc of one of the rows
print(df.iloc[70])