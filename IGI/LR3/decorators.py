#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DECORATORS
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

import functools
import time


def timer_decorator(func):
    """
    Decorator to measure and display the execution time of a function.

    Args:
        func: The function to be decorated

    Returns:
        wrapper: The wrapped function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[DEBUG] Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result

    return wrapper


def log_decorator(func):
    """
    Decorator to log function calls and their arguments.

    Args:
        func: The function to be decorated

    Returns:
        wrapper: The wrapped function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        print(f"[LOG] Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function {func.__name__} returned: {result}")
        return result

    return wrapper


def input_validation_decorator(func):
    """
    Decorator to handle input validation exceptions.

    Args:
        func: The function to be decorated

    Returns:
        wrapper: The wrapped function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Input validation error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    return wrapper