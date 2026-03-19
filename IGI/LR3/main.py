#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Laboratory Work No. 3
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

import task1
import task2
import task3
import task4
import task5
from validation import repeat_program


def main():
    print("=" * 30)
    print("LABORATORY WORK No. 3")
    print("Variant 16")
    print("=" * 30)

    while True:
        print("\nSelect task to execute:")
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("4. Task 4")
        print("5. Task 5")
        print("0. Exit")

        choice = input("\nEnter (0-5): ").strip()

        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            task1.task1()
        elif choice == '2':
            task2.task2()
        elif choice == '3':
            task3.task3()
        elif choice == '4':
            task4.task4()
        elif choice == '5':
            task5.task5()
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

        if not repeat_program():
            break


if __name__ == "__main__":
    main()