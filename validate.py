#!/usr/bin/env python3

import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("file", help="CSV file for dataframe")
args = parser.parse_args()

print("Checking that the dataset is a valid CSV file, showing first 10 rows.")

df = pd.read_csv(args.file, nrows=10)

print(df)
