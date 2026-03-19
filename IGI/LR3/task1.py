#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK 1
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""
import math
from decorators import timer_decorator, log_decorator
from validation import get_float_input, repeat_program


def sin_series(x, eps=1e-6, max_iter=500):
    """
    Calculate sin(x) using series expansion with given precision.
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... = sum_{n=0}^{∞} (-1)^n * x^(2n+1) / (2n+1)!
    """
    if eps <= 0:
        raise ValueError("Precision eps must be positive")
    if max_iter <= 0:
        raise ValueError("Maximum iterations must be positive")

    term = x
    sum_sin = term
    n = 0

    for n in range(1, max_iter):
        term *= -x * x / ((2 * n) * (2 * n + 1))
        sum_sin += term

        if abs(term) < eps:
            break

    math_value = math.sin(x)

    return sum_sin, n + 1, math_value


@timer_decorator
@log_decorator
def task1():
    """
    Demonstrates sin(x) calculation using series expansion.
    """
    print("\n" + "=" * 60)
    print("TASK 1: Series Expansion of sin(x)")
    print("Formula: sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...")
    print("=" * 60)

    while True:
        try:
            x = get_float_input("\nEnter x: ")
            eps = get_float_input("Enter precision eps: ", allow_negative=False, allow_zero=False)

            print(f"\nCalculating sin({x}) with precision {eps}...")
            print("-" * 50)

            result, n, math_result = sin_series(x, eps)

            print(f"x = {x:.6f}")
            print(f"F(x) = {result:.10f}")
            print(f"n = {n}")
            print(f"Math F(x) = {math_result:.10f}")
            print(f"Absolute error: {abs(result - math_result):.2e}")

        except ValueError as e:
            print(f"Error: {e}")
        except OverflowError:
            print("Error: Numerical overflow.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        if not repeat_program():
            break


if __name__ == "__main__":
    task1()