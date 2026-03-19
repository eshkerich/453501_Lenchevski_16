#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK 2
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

from decorators import timer_decorator, log_decorator
from validation import repeat_program


def is_even_natural(num):
    """
    Check if a number is an even natural number.
    """
    return num > 0 and num % 2 == 0


@timer_decorator
@log_decorator
def task2():
    """
    Main function for Task 2.
    Accepts integers from keyboard and counts even natural numbers.
    Loop terminates when 0 is entered.
    """
    print("\n" + "=" * 60)
    print("TASK 2: Counting Even Natural Numbers")
    print("Enter integers (0 to exit)")
    print("=" * 60)

    while True:
        count_even_natural = 0
        total_numbers = 0

        print("\nStart entering numbers:")

        while True:
            try:
                user_input = input("Enter integer (0 to exit): ").strip()

                if not user_input:
                    print("Input cannot be empty. Please enter a number.")
                    continue

                num = int(user_input)

                if num == 0:
                    print(f"\nTermination condition met (entered 0)")
                    break

                total_numbers += 1

                if is_even_natural(num):
                    count_even_natural += 1
                    print(f"  {num} is an even natural number (count: {count_even_natural})")
                else:
                    if num <= 0:
                        print(f"  {num} is not a natural number")
                    elif num % 2 != 0:
                        print(f"  {num} is odd")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                return
            except Exception as e:
                print(f"Unexpected error: {e}")

        print("\n" + "-" * 40)
        print("RESULTS:")
        print(f"Total numbers entered: {total_numbers}")
        print(f"Count of even natural numbers: {count_even_natural}")

        if total_numbers > 0:
            percentage = (count_even_natural / total_numbers) * 100
            print(f"Percentage: {percentage:.1f}%")

        if not repeat_program():
            break


if __name__ == "__main__":
    task2()