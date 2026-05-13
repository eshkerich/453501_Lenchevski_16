# task5.py
"""
Lab 4 - Task 5
Author: Lenchevski Vladimir
Date: 30.04.2026
Version: 1.0
Find column with smallest sum of elements. Compute median of that column.
"""

import numpy as np


def manual_median(arr):
    """
    Calculate median manually without using numpy.median().
    """
    sorted_arr = np.sort(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]


def task5():
    print("\n" + "=" * 60)
    print("Task 5: NumPy Matrix Analysis (Variant 16)")
    print("=" * 60)

    np.random.seed(67)

    n = int(input("\nEnter number of rows (n): ") or "5")
    m = int(input("Enter number of columns (m): ") or "4")

    print(f"\nGenerating random integer matrix of size {n}x{m}...")
    A = np.random.randint(-20, 50, size=(n, m))

    print("\n" + "=" * 60)
    print("Matrix A:")
    print("=" * 60)
    print(A)

    col_sums = np.sum(A, axis=0)
    print(f"\nColumn sums: {col_sums}")

    min_col_idx = np.argmin(col_sums)
    print(f"\nColumn with smallest sum: column {min_col_idx + 1} (index {min_col_idx})")
    print(f"Smallest column sum value: {col_sums[min_col_idx]}")

    col_data = A[:, min_col_idx]
    print(f"\nData in column {min_col_idx + 1}: {col_data}")

    median_np = np.median(col_data)
    median_manual = manual_median(col_data)

    print(f"\nMedian of column {min_col_idx + 1}:")
    print(f"  Using numpy.median(): {median_np}")
    print(f"  Using manual calculation: {median_manual}")
    print(f"  Results match: {np.isclose(median_np, median_manual)}")


if __name__ == "__main__":
    task5()