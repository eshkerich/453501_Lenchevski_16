# task4.py
"""
Lab 4 - Task 4
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
Triangle circumscribed about a circle with radius R
"""

import matplotlib.pyplot as plt
import math
import os
from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

class FigureColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Triangle(GeometricFigure):
    figure_type = "Triangle circumscribed about circle"

    def __init__(self, R, color):
        self.R = R
        self.color_obj = FigureColor(color)
        self.side = 2 * R * math.sqrt(3)

    def area(self):
        return (3 * math.sqrt(3) / 4) * self.side ** 2

    def __str__(self):
        return f"{self.figure_type}: R={self.R}, side={self.side:.2f}, color {self.color_obj.color}, area={self.area():.2f}"

    @classmethod
    def get_type(cls):
        return cls.figure_type

def draw_triangle(triangle, title="Triangle", save_path=None):
    side = triangle.side
    x = [0, side, side / 2]
    y = [0, 0, side * math.sqrt(3) / 2]
    center_x = side / 2
    center_y = side * math.sqrt(3) / 6
    plt.figure()
    plt.fill(x, y, color=triangle.color_obj.color, alpha=0.7)
    circle = plt.Circle((center_x, center_y), triangle.R, color='black', fill=False, linewidth=2)
    plt.gca().add_patch(circle)
    plt.plot(x + [x[0]], y + [y[0]], 'k-')
    plt.axis('equal')
    plt.title(title)
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.show()

def task4():
    print("\n=== Task 4: Triangle circumscribed about a circle ===")
    os.makedirs("data", exist_ok=True)

    try:
        R = float(input("Enter circle radius R: "))
        color = input("Enter fill color (e.g., blue, red, green): ")

        if R <= 0:
            raise ValueError("Radius must be positive")

        triangle = Triangle(R, color)
        print(triangle)
        draw_triangle(triangle, "Triangle circumscribed about circle", save_path="data/triangle.png")
    except ValueError as e:
        print(f"Input error: {e}")