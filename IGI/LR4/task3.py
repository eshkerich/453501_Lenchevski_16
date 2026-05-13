# task3.py
"""
Lab 4 - Task 3
Author: Lenchevski Vladimir
Date: 30.04.2026
Version: 1.0
Plot F(x) from Taylor series vs math.sin(x) with statistical analysis
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import os
from statistics import mean, median, mode, variance, stdev
from collections import Counter


def sin_series(x, n_terms=10):
    """
    Calculate sin(x) using Taylor series expansion:
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    total = 0.0
    for n in range(n_terms):
        sign = (-1) ** n
        power = 2 * n + 1
        term = sign * (x ** power) / math.factorial(power)
        total += term
    return total


def calculate_statistics(sequence):
    """
    Calculate statistical parameters for a sequence.
    """
    if not sequence:
        return {}

    mean_val = mean(sequence)

    median_val = median(sequence)

    freq = Counter(sequence)
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    mode_val = min(modes) if modes else 0

    variance_val = variance(sequence) if len(sequence) > 1 else 0

    std_dev = stdev(sequence) if len(sequence) > 1 else 0

    return {
        'mean': mean_val,
        'median': median_val,
        'mode': mode_val,
        'variance': variance_val,
        'std_dev': std_dev
    }


def analyze_series(x_values, n_terms=10):
    """
    Analyze series and math function values.
    """
    results = []
    f_series_values = []

    for x in x_values:
        f_series = sin_series(x, n_terms)
        f_math = math.sin(x)
        eps = abs(f_math - f_series)
        results.append((x, f_series, f_math, eps))
        f_series_values.append(f_series)

    return results, f_series_values


def task3():
    print("\n=== Task 3: sin(x)  ===")

    os.makedirs("data", exist_ok=True)

    x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    n_terms = 10

    results, f_series_values = analyze_series(x_vals, n_terms)

    x_plot = [r[0] for r in results]
    y_series = [r[1] for r in results]
    y_math = [r[2] for r in results]
    errors = [r[3] for r in results]

    stats = calculate_statistics(f_series_values)

    print("\n=== Statistical Analysis of F(x) Series Values ===")
    print(f"Arithmetic mean: {stats['mean']:.6f}")
    print(f"Median: {stats['median']:.6f}")
    print(f"Mode: {stats['mode']:.6f}")
    print(f"Variance: {stats['variance']:.6f}")
    print(f"Standard Deviation: {stats['std_dev']:.6f}")

    print("\n=== Error Statistics ===")
    print(f"Mean absolute error: {mean(errors):.6f}")
    print(f"Max error: {max(errors):.6f}")
    print(f"Min error: {min(errors):.6f}")

    plt.figure(figsize=(12, 7))

    plt.plot(x_plot, y_series, label=f'Taylor Series sin(x) (n={n_terms} terms)',
             color='red', linestyle='--', linewidth=2)

    plt.plot(x_plot, y_math, label='math.sin(x)',
             color='blue', linewidth=2)

    max_error_idx = errors.index(max(errors))
    plt.annotate(f'Max error: {max(errors):.4f}',
                 xy=(x_plot[max_error_idx], y_series[max_error_idx]),
                 xytext=(x_plot[max_error_idx] + 0.5, y_series[max_error_idx] + 0.3),
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

    stats_text = f'Statistics (F(x) series):\n'
    stats_text += f'Mean = {stats["mean"]:.4f}\n'
    stats_text += f'Median = {stats["median"]:.4f}\n'
    stats_text += f'Mode = {stats["mode"]:.4f}\n'
    stats_text += f'Variance = {stats["variance"]:.4f}\n'
    stats_text += f'Std Dev = {stats["std_dev"]:.4f}'

    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes,
             fontsize=9, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.xlabel('x (radians)', fontsize=12)
    plt.ylabel('sin(x)', fontsize=12)
    plt.title('Comparison of sin(x) Taylor Series vs math.sin(x)', fontsize=14)
    plt.legend(loc='lower left', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)

    plt.xlim(-2 * np.pi - 0.5, 2 * np.pi + 0.5)
    plt.ylim(-1.5, 1.5)

    output_path = "data/sin_series_plot_variant16.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved to {output_path}")

    plt.show()

    output_file = "data/task3_results.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Task 3 Results - Variant 16 (sin x)\n")
        f.write("=" * 50 + "\n\n")
        f.write("x, F(x) series, math.sin(x), error\n")
        for r in results[:20]:
            f.write(f"{r[0]:.4f}, {r[1]:.6f}, {r[2]:.6f}, {r[3]:.6e}\n")
        f.write("\nStatistical Analysis of F(x) Series Values:\n")
        for key, val in stats.items():
            f.write(f"{key}: {val:.6f}\n")

    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    task3()