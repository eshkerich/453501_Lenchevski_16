#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK 3
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

from decorators import timer_decorator, log_decorator
from validation import repeat_program


def count_non_whitespace(text):
    """
    Count characters that are not whitespace in a string.
    Whitespace characters: space (' '), tab ('\t'), newline ('\n'), etc.
    """
    if not text:
        return 0

    count = 0
    for char in text:
        if not char.isspace():
            count += 1

    return count


def analyze_string(text):
    """
    Perform comprehensive string analysis.
    """
    result = {
        'original': text,
        'length': len(text),
        'non_whitespace': count_non_whitespace(text),
        'whitespace': sum(1 for c in text if c.isspace()),
        'spaces': text.count(' '),
        'tabs': text.count('\t'),
        'newlines': text.count('\n'),
        'digits': sum(1 for c in text if c.isdigit()),
        'letters': sum(1 for c in text if c.isalpha()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }

    return result


def display_analysis(analysis):
    """
    Display string analysis results in a formatted way.
    """
    print("\n" + "=" * 50)
    print("STRING ANALYSIS RESULTS")
    print("=" * 50)

    print(f"Original string: \"{analysis['original']}\"")
    print(f"Total length: {analysis['length']} characters")
    print(f"Non-whitespace characters: {analysis['non_whitespace']}")
    print(f"Whitespace characters: {analysis['whitespace']}")
    print(f"  - Spaces: {analysis['spaces']}")
    print(f"  - Tabs: {analysis['tabs']}")
    print(f"  - Newlines: {analysis['newlines']}")
    print(f"Digits: {analysis['digits']}")
    print(f"Letters: {analysis['letters']}")
    print(f"  - Uppercase: {analysis['uppercase']}")
    print(f"  - Lowercase: {analysis['lowercase']}")


@timer_decorator
@log_decorator
def task3():
    """
    Main function for Task 3.
    Analyzes user-input string and counts non-whitespace characters.
    """
    print("\n" + "=" * 60)
    print("TASK 3: String Analysis - Count Non-Whitespace Characters")
    print("=" * 60)

    while True:
        try:
            print("\nEnter a string to analyze (press Enter twice to finish):")

            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)

            if lines and lines[-1] == "":
                lines.pop()

            text = "\n".join(lines)

            if not text:
                print("Empty string entered. Please enter some text.")
                if not repeat_program():
                    break
                continue

            analysis = analyze_string(text)
            display_analysis(analysis)

            print(f"\nCount of non-whitespace characters: {analysis['non_whitespace']}")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")

        if not repeat_program():
            break


if __name__ == "__main__":
    task3()