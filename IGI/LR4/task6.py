# task6.py
"""
Lab 4 - Task 6
Author: Lenchevski Vladimir
Date: 30.04.2026
Version: 1.0
Data analysis with pandas based on dataset.csv
"""

import pandas as pd
import numpy as np


def task6_a():
    """
    Task 6A: Load data from CSV, analyze structure, handle missing values,
    rename columns, filter by popularity, calculate statistics by genre.
    """
    print("\n" + "=" * 70)
    print("Task 6A: Data Loading and Analysis")
    print("=" * 70)

    # 1. Load data from CSV file
    print("\n1. Loading dataset...")
    df = pd.read_csv('dataset.csv', index_col=0)
    print(f"   Dataset loaded successfully!")
    print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    # 2. Display first 5 and last 5 rows
    print("\n2. First 5 rows:")
    print(df.head())
    print("\n   Last 5 rows:")
    print(df.tail())

    # 3. Display column names and total count
    print(f"\n3. Total number of columns: {len(df.columns)}")
    print("   Column names:")
    for i, col in enumerate(df.columns, 1):
        print(f"      {i:2d}. {col}")

    # 4. Display data types
    print("\n4. Data types of columns:")
    print(df.dtypes)

    # 5. Display basic info (alternative to df.info)
    print("\n5. Basic info about the dataset:")
    print(f"   Index: {df.index.name if df.index.name else 'None'}")
    print(f"   Total entries: {len(df)}")
    print(f"   Total columns: {len(df.columns)}")
    print(f"   Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    # 6. Check for missing values
    print("\n6. Missing values per column:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage (%)': missing_pct
    })
    if (missing > 0).any():
        print(missing_df[missing_df['Missing Count'] > 0])
    else:
        print("   No missing values found!")

    # 7. Handle missing values (fill with median for numeric columns)
    print("\n7. Handling missing values (filling with median for numeric columns):")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
            print(f"   Filled missing values in '{col}' with median: {median_val:.2f}")

    # 8. Rename columns: popularity -> pop, duration_ms -> duration
    print("\n8. Renaming columns:")
    df = df.rename(columns={
        'popularity': 'pop',
        'duration_ms': 'duration'
    })
    print(f"   Renamed: 'popularity' → 'pop'")
    print(f"   Renamed: 'duration_ms' → 'duration'")

    # 9. Filter tracks with popularity > 50
    print("\n9. Filtering tracks with popularity > 50...")
    df_filtered = df[df['pop'] > 50].copy()
    print(f"   Original dataset size: {len(df)}")
    print(f"   Filtered dataset size: {len(df_filtered)}")
    print(f"   Percentage of tracks with pop > 50: {len(df_filtered)/len(df)*100:.2f}%")

    # 10. Calculate mean, median, mode for pop and danceability
    print("\n10. Statistics for 'pop' and 'danceability' columns:")
    print("\n    Statistics for 'pop' (popularity):")
    print(f"        Mean:  {df_filtered['pop'].mean():.4f}")
    print(f"        Median: {df_filtered['pop'].median():.4f}")
    pop_mode = df_filtered['pop'].mode()
    print(f"        Mode:   {pop_mode.iloc[0] if len(pop_mode) > 0 else 'N/A'}")
    print(f"        Std:    {df_filtered['pop'].std():.4f}")
    print(f"        Min:    {df_filtered['pop'].min():.4f}")
    print(f"        Max:    {df_filtered['pop'].max():.4f}")

    print("\n    Statistics for 'danceability':")
    print(f"        Mean:  {df_filtered['danceability'].mean():.4f}")
    print(f"        Median: {df_filtered['danceability'].median():.4f}")
    dance_mode = df_filtered['danceability'].mode()
    print(f"        Mode:   {dance_mode.iloc[0] if len(dance_mode) > 0 else 'N/A'}")
    print(f"        Std:    {df_filtered['danceability'].std():.4f}")
    print(f"        Min:    {df_filtered['danceability'].min():.4f}")
    print(f"        Max:    {df_filtered['danceability'].max():.4f}")

    # 11. Group by 'track_genre' and calculate mean of 'pop' and 'danceability'
    print("\n11. Group by 'track_genre' - mean of 'pop' and 'danceability':")
    genre_stats = df_filtered.groupby('track_genre')[['pop', 'danceability']].mean().round(4)
    genre_stats = genre_stats.sort_values('pop', ascending=False)
    print("\n    Top 10 genres by mean popularity:")
    print(genre_stats.head(10))

    print("\n    Bottom 10 genres by mean popularity:")
    print(genre_stats.tail(10))

    return df, df_filtered


def task6_b(df):
    """
    Task 6B: Create pivot table and additional analysis.
    """
    print("\n" + "=" * 70)
    print("Task 6B: Pivot Table and Advanced Analysis")
    print("=" * 70)

    # 1. Create pivot table: rows = 'track_genre', columns = 'explicit', values = 'pop'
    print("\n1. Creating pivot table (rows: track_genre, columns: explicit, values: pop)")
    print("\n   Pivot table - Mean popularity by genre and explicitness:")
    pivot_table = pd.pivot_table(
        df,
        values='pop',
        index='track_genre',
        columns='explicit',
        aggfunc='mean',
        fill_value=0
    )
    # Rename columns for clarity
    pivot_table.columns = ['Non-Explicit', 'Explicit']
    print(pivot_table.round(2))

    # 2. Add row and column totals
    print("\n2. Pivot table with row and column totals:")
    pivot_with_totals = pivot_table.copy()
    pivot_with_totals['Total'] = pivot_with_totals.sum(axis=1)
    total_row = pivot_with_totals.sum(axis=0)
    pivot_with_totals.loc['OVERALL TOTAL'] = total_row
    print(pivot_with_totals.round(2))

    # 3. Additional analysis: genres with highest popularity difference
    print("\n3. Analysis: Impact of explicitness on popularity")
    if 'Explicit' in pivot_table.columns and 'Non-Explicit' in pivot_table.columns:
        pivot_table['pop_diff'] = pivot_table['Explicit'] - pivot_table['Non-Explicit']
        print("\n    Top 5 genres where explicit tracks are more popular:")
        print(pivot_table.nlargest(5, 'pop_diff')[['pop_diff']].round(2))
        print("\n    Top 5 genres where non-explicit tracks are more popular:")
        print(pivot_table.nsmallest(5, 'pop_diff')[['pop_diff']].round(2))
    else:
        print("    Only one explicitness category available in data")

    # 4. Correlation analysis between numeric features
    print("\n4. Correlation analysis (features correlation with popularity):")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    pop_corr = corr_matrix['pop'].drop('pop').sort_values(ascending=False)
    print("\n    Correlation of features with 'pop' (popularity):")
    for feat, corr_val in pop_corr.items():
        print(f"        {feat:20s}: {corr_val:.4f}")

    # 5. Analyze popularity by time signature
    print("\n5. Popularity analysis by time_signature:")
    time_stats = df.groupby('time_signature')['pop'].agg(['mean', 'median', 'count', 'std']).round(2)
    print(time_stats)

    # 6. Find most energetic acoustic track
    print("\n6. Most energetic acoustic track (energy > 0.9 and acousticness > 0.5):")
    acoustic_energetic = df[(df['energy'] > 0.9) & (df['acousticness'] > 0.5)]
    if len(acoustic_energetic) > 0:
        top_energetic = acoustic_energetic.nlargest(5, 'energy')
        for idx, row in top_energetic.iterrows():
            print(f"        {row['track_name']} by {row['artists']}")
            print(f"            Energy: {row['energy']:.3f}, Acousticness: {row['acousticness']:.3f}, Pop: {row['pop']}")
    else:
        print("        No tracks found matching criteria")

    # 7. Additional analysis: most danceable genres
    print("\n7. Top 10 most danceable genres (average danceability):")
    dance_by_genre = df.groupby('track_genre')['danceability'].mean().sort_values(ascending=False)
    for genre, val in dance_by_genre.head(10).items():
        print(f"        {genre:20s}: {val:.4f}")

    # 8. Valence analysis (musical positiveness)
    print("\n8. Top 5 happiest and saddest genres (valence analysis):")
    valence_by_genre = df.groupby('track_genre')['valence'].mean().sort_values(ascending=False)
    print("\n    Happiest genres (highest valence):")
    for genre, val in valence_by_genre.head(5).items():
        print(f"        {genre:20s}: {val:.4f}")
    print("\n    Saddest genres (lowest valence):")
    for genre, val in valence_by_genre.tail(5).items():
        print(f"        {genre:20s}: {val:.4f}")

    return pivot_table


if __name__ == "__main__":
    df_original, df_filtered = task6_a()
    pivot_result = task6_b(df_original)