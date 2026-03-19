#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK 5
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

from decorators import timer_decorator, log_decorator
from validation import get_list_from_user, get_list_from_generator, repeat_program
import math


def input_list_interactive():
    """
    Interactive list input from user.
    """
    return get_list_from_user()


def input_list_generated():
    """
    Generate list using generator.
    """
    return get_list_from_generator()


def find_max_abs_index(lst):
    """
    Find index of element with maximum absolute value.
    """
    if not lst:
        return None

    max_abs = abs(lst[0])
    max_index = 0

    for i, val in enumerate(lst):
        if abs(val) > max_abs:
            max_abs = abs(val)
            max_index = i

    return max_index


def find_min_abs_index(lst):
    """
    Find index of element with minimum absolute value.
    """
    if not lst:
        return None

    min_abs = abs(lst[0])
    min_index = 0

    for i, val in enumerate(lst):
        if abs(val) < min_abs:
            min_abs = abs(val)
            min_index = i

    return min_index


def sum_non_negative(lst):
    """
    Calculate sum of non-negative elements.
    """
    return sum(x for x in lst if x >= 0)


def product_between_indices(lst, idx1, idx2):
    """
    Calculate product of elements between two indices (exclusive).
    """
    if not lst or idx1 is None or idx2 is None:
        return None

    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)

    if start >= end:
        return 1.0

    product = 1.0
    for i in range(start, end):
        product *= lst[i]

    return product


def process_list(lst):
    """
    Process list according to variant 16 requirements.
    """
    if not lst:
        return {"error": "Empty list"}

    max_abs_idx = find_max_abs_index(lst)
    min_abs_idx = find_min_abs_index(lst)

    non_negative_sum = sum_non_negative(lst)

    product = product_between_indices(lst, max_abs_idx, min_abs_idx)

    return {
        "list": lst,
        "size": len(lst),
        "max_abs_index": max_abs_idx,
        "max_abs_value": lst[max_abs_idx] if max_abs_idx is not None else None,
        "max_abs": abs(lst[max_abs_idx]) if max_abs_idx is not None else None,
        "min_abs_index": min_abs_idx,
        "min_abs_value": lst[min_abs_idx] if min_abs_idx is not None else None,
        "min_abs": abs(lst[min_abs_idx]) if min_abs_idx is not None else None,
        "non_negative_sum": non_negative_sum,
        "product_between": product,
        "non_negative_elements": [x for x in lst if x >= 0]
    }


def display_list(lst):
    """
    Display list in a formatted way.
    """
    print("\nList contents:")
    for i, val in enumerate(lst):
        print(f"  [{i}]: {val:.6f}")


def display_results(results):
    """
    Display processing results in a formatted way.
    """
    print("\n" + "=" * 60)
    print("LIST PROCESSING RESULTS")
    print("=" * 60)

    if "error" in results:
        print(f"Error: {results['error']}")
        return

    print(f"List size: {results['size']}")

    print("\n" + "-" * 40)
    print("Maximum absolute value element:")
    print(f"  Index: {results['max_abs_index']}")
    print(f"  Value: {results['max_abs_value']:.6f}")
    print(f"  |Value|: {results['max_abs']:.6f}")

    print("\n" + "-" * 40)
    print("Minimum absolute value element:")
    print(f"  Index: {results['min_abs_index']}")
    print(f"  Value: {results['min_abs_value']:.6f}")
    print(f"  |Value|: {results['min_abs']:.6f}")

    print("\n" + "-" * 40)
    print("Non-negative elements:")
    non_neg = results['non_negative_elements']
    if non_neg:
        print(f"  Count: {len(non_neg)}")
        print(f"  Values: {[f'{x:.6f}' for x in non_neg]}")
        print(f"  Sum: {results['non_negative_sum']:.6f}")
    else:
        print("  No non-negative elements found")

    print("\n" + "-" * 40)
    print("Product between max and min absolute value elements:")
    print(f"  Indices between: {min(results['max_abs_index'], results['min_abs_index']) + 1} "
          f"to {max(results['max_abs_index'], results['min_abs_index'])}")

    if results['product_between'] is not None:
        if abs(results['product_between'] - 1.0) < 1e-10 and \
                abs(min(results['max_abs_index'], results['min_abs_index']) + 1 -
                    max(results['max_abs_index'], results['min_abs_index'])) >= 0:
            print("  No elements between the two indices")
        else:
            print(f"  Product: {results['product_between']:.10f}")

            if abs(results['product_between']) > 1e100:
                print("  Warning: Very large product (possible overflow)")
            elif abs(results['product_between']) < 1e-100 and results['product_between'] != 0:
                print("  Warning: Very small product (possible underflow)")
    else:
        print("  Cannot calculate product (invalid indices)")


@timer_decorator
@log_decorator
def task5():
    """
    Main function for Task 5.
    """
    print("\n" + "=" * 60)
    print("TASK 5: List Processing")
    print("Variant 16: Sum of non-negative elements and product of elements")
    print("between maximum and minimum absolute value elements")
    print("=" * 60)

    while True:
        try:
            print("\nChoose list initialization method:")
            print("1. User input")
            print("2. Generator (random values)")

            choice = input("Enter your choice (1 or 2): ").strip()

            if choice == '1':
                lst = input_list_interactive()
            elif choice == '2':
                lst = input_list_generated()
            else:
                print("Invalid choice. Please enter 1 or 2.")
                if not repeat_program():
                    break
                continue

            if not lst:
                print("Empty list. Please try again.")
                if not repeat_program():
                    break
                continue

            display_list(lst)

            results = process_list(lst)

            display_results(results)

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            return
        except ValueError as e:
            print(f"Input error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero encountered")
        except OverflowError:
            print("Error: Numerical overflow")
        except Exception as e:
            print(f"Unexpected error: {e}")

        if not repeat_program():
            break


if __name__ == "__main__":
    task5()