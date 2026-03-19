#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VALIDATION
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""


def repeat_program():
    """
    Ask user if user want to repeat the operation.
    """
    while True:
        answer = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
        if answer in ['y', 'yes', 'да', 'д']:
            return True
        elif answer in ['n', 'no', 'нет', 'н']:
            return False
        else:
            print("Please answer 'y' or 'n'")


def get_float_input(prompt, allow_negative=True, allow_zero=True):
    """
    Get and validate float input from user.
    """
    while True:
        try:
            value = float(input(prompt))
            if not allow_negative and value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            if not allow_zero and value == 0:
                print("Value cannot be zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(prompt, allow_negative=True, allow_zero=True):
    """
    Get and validate integer input from user.
    """
    while True:
        try:
            value = int(input(prompt))
            if not allow_negative and value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            if not allow_zero and value == 0:
                print("Value cannot be zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_positive_int_input(prompt):
    """
    Get and validate positive integer input from user.
    """
    return get_int_input(prompt, allow_negative=False, allow_zero=False)


def get_list_from_user():
    """
    Get a list of real numbers from user input.
    """
    size = get_positive_int_input("Enter the size of the list: ")

    print(f"\nEnter {size} real numbers:")
    result = []
    for i in range(size):
        value = get_float_input(f"Element {i + 1}: ")
        result.append(value)

    return result


def get_list_from_generator():
    """
    Generate a list using a generator function.
    """
    size = get_positive_int_input("Enter the size of the list: ")

    def generator():
        import random
        return [random.uniform(-10, 10) for _ in range(size)]

    return generator()