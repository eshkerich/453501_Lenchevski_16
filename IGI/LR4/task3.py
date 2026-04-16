# task3.py
"""
Lab 4 - Task 3
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
Plot F(x) from series vs math.sin(x)
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import os

def sin_series(x, n_terms=10):
    """sin(x) = x - x^3/3! + x^5/5! - ..."""
    total = 0
    for n in range(n_terms):
        sign = (-1) ** n
        term = sign * (x ** (2*n + 1)) / math.factorial(2*n + 1)
        total += term
    return total

def analyze_series(x_values, n_terms=10):
    results = []
    for x in x_values:
        f_series = sin_series(x, n_terms)
        f_math = math.sin(x)
        eps = abs(f_math - f_series)
        results.append((x, f_series, f_math, eps))
    return results

def task3():
    print("\n=== Task 3: sin(x) ===")
    os.makedirs("data", exist_ok=True)

    x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)
    results = analyze_series(x_vals, n_terms=10)

    x_plot = [r[0] for r in results]
    y_series = [r[1] for r in results]
    y_math = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_series, label='sin(x) series (10 terms)', color='red', linestyle='--')
    plt.plot(x_plot, y_math, label='math.sin(x)', color='blue', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Comparison of sin(x) Series vs math.sin(x)')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    output_path = "data/sin_series_plot.png"
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")
    plt.show()

    arr = [r[3] for r in results]
    mean_err = np.mean(arr)
    median_err = np.median(arr)
    mode_err = max(set(arr), key=arr.count) if arr else 0
    variance = np.var(arr)
    std_dev = np.std(arr)
    print(f"Mean error: {mean_err:.6f}")
    print(f"Median error: {median_err:.6f}")
    print(f"Mode error: {mode_err:.6f}")
    print(f"Variance: {variance:.6f}")
    print(f"Std deviation: {std_dev:.6f}")