#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('clean.csv')

df = df[(df.stroke == 1)]

df['gender'].value_counts().plot(kind='bar')

plt.title("Stroke occurences by gender")
plt.show()
