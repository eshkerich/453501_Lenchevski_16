# task5.py
"""
Lab 4 - Task 5
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
Find column with smallest sum, compute median (numpy and manual)
"""

import numpy as np

def manual_median(arr):
    sorted_arr = np.sort(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]

def task5():
    print("\n=== Task 5: NumPy Operations ===")
    np.random.seed(67)
    n, m = 5, 4
    A = np.random.randint(-20, 50, size=(n, m))
    print("Matrix A:\n", A)

    col_sums = np.sum(A, axis=0)
    min_col_idx = np.argmin(col_sums)
    print(f"Column sums: {col_sums}")
    print(f"Column with smallest sum: {min_col_idx + 1}")

    col_data = A[:, min_col_idx]
    median_np = np.median(col_data)
    median_manual = manual_median(col_data)

    print(f"Median of column {min_col_idx} (NumPy): {median_np}")
    print(f"Median of column {min_col_idx} (manual): {median_manual}")