# task6.py
"""
Lab 4 - Task 6
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
UFO Sightings dataset
"""

import pandas as pd
import numpy as np
import os

def task6():
    print("\n=== Task 6: Pandas UFO Sightings ===")
    np.random.seed(42)
    data = {
        'state': ['ca', 'tx', 'ny', 'fl', 'ca', 'tx', 'ny', 'fl', 'ca', 'tx'],
        'shape': ['circle', 'triangle', 'circle', 'light', 'circle', 'triangle', 'circle', 'light', 'circle', 'triangle'],
        'duration (seconds)': np.random.randint(10, 1000, 10),
        'comments': ['cool', 'amazing', 'weird', 'nice', 'wow', 'strange', 'bright', 'fast', 'glow', 'silent']
    }
    df = pd.DataFrame(data)

    state_codes = df['state'].str[0].str.upper()
    print("\nState codes (first letters):\n", state_codes)

    unique_shapes = df['shape'].unique()
    shape_series = pd.Series(unique_shapes, index=[f'diff_{i+1}' for i in range(len(unique_shapes))])
    print("\nUnique shapes with custom indices:\n", shape_series)

    duration_series = df['duration (seconds)']
    median_duration = duration_series.median()
    duration_series.loc['median'] = median_duration
    print(f"\nDuration series with median added:\n{duration_series}")

    df['helpful_votes'] = np.random.randint(0, 100, 10)
    df['total_votes'] = df['helpful_votes'] + np.random.randint(0, 50, 10)
    df['helpfulness_ratio'] = df['helpful_votes'] / df['total_votes']
    df['helpfulness_ratio'] = df['helpfulness_ratio'].fillna(0).clip(0, 1)
    print("\nHelpfulness ratio:\n", df[['helpful_votes', 'total_votes', 'helpfulness_ratio']])

    avg_ca = df[df['state'] == 'ca']['duration (seconds)'].mean()
    avg_tx = df[df['state'] == 'tx']['duration (seconds)'].mean()
    if avg_tx > 0:
        ratio = avg_ca / avg_tx
        print(f"\nAverage duration in CA: {avg_ca:.2f}s, TX: {avg_tx:.2f}s")
        print(f"Ratio CA/TX: {ratio:.2f}")
    else:
        print("Cannot compute ratio, TX avg is zero.")