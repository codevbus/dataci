#!/usr/bin/env python3

import pandas as pd


df = pd.read_csv('healthcare-dataset-stroke-data.csv')

print("Dropping rows with null/NaN values")

df = df.dropna()

print("Dropping outlier values(age>120, BMI>50)")

df = df[df.age < 120]

df = df[df.bmi < 50]

print("Creating new CSV file")

df.to_csv('clean.csv', index=False)
