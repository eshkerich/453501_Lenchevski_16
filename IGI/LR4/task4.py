# task4.py
"""
Lab 4 - Task 4
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
Triangle circumscribed about a circle with radius R
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import os
from abc import ABC, abstractmethod
from typing import Optional


class DrawableMixin:
    def get_vertices(self):
        raise NotImplementedError

    def get_center(self):
        raise NotImplementedError


class GeometricFigure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class FigureColor:
    def __init__(self, color: str):
        self._color = color
        self._opacity = 0.7

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        if not value or not isinstance(value, str):
            raise ValueError("Color must be a non-empty string")
        self._color = value.lower()

    @property
    def opacity(self) -> float:
        return self._opacity

    @opacity.setter
    def opacity(self, value: float) -> None:
        if not 0 <= value <= 1:
            raise ValueError("Opacity must be between 0 and 1")
        self._opacity = value

    def __str__(self) -> str:
        return f"{self._color} (opacity: {self._opacity})"


class Triangle(GeometricFigure, DrawableMixin):
    figure_type = "Equilateral triangle circumscribed about a circle"
    _instance_count = 0

    def __init__(self, R: float, color: str, label: str = ""):
        super().__init__()
        self._R = R
        self._validate_positive(R, "Radius")
        self._color_obj = FigureColor(color)
        self._label = label if label else "Triangle"
        self._side = 2 * R * math.sqrt(3)
        self.created_at = "Runtime"
        Triangle._instance_count += 1

    @staticmethod
    def _validate_positive(value: float, name: str) -> None:
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")

    @property
    def R(self) -> float:
        return self._R

    @R.setter
    def R(self, value: float) -> None:
        self._validate_positive(value, "Radius")
        self._R = value
        self._side = 2 * value * math.sqrt(3)

    @property
    def side(self) -> float:
        return self._side

    @property
    def color_obj(self) -> FigureColor:
        return self._color_obj

    @color_obj.setter
    def color_obj(self, value: FigureColor) -> None:
        if not isinstance(value, FigureColor):
            raise TypeError("Must be FigureColor instance")
        self._color_obj = value

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        self._label = value if value else "Triangle"

    def area(self) -> float:
        return (3 * math.sqrt(3) / 4) * self._side ** 2

    def perimeter(self) -> float:
        return 3 * self._side

    def get_vertices(self) -> list:
        height = self._side * math.sqrt(3) / 2
        return [
            (0, 0),
            (self._side, 0),
            (self._side / 2, height)
        ]

    def get_center(self) -> tuple:
        return (self._side / 2, self._side * math.sqrt(3) / 6)

    def __str__(self) -> str:
        return (f"{self.figure_type}: R={self._R}, side={self._side:.2f}, "
                f"perimeter={self.perimeter():.2f}, area={self.area():.2f}, "
                f"color={self._color_obj.color}, label='{self._label}'")

    def __repr__(self) -> str:
        return f"Triangle(R={self._R}, color='{self._color_obj.color}', label='{self._label}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Triangle):
            return False
        return self.area() == other.area()

    def __lt__(self, other) -> bool:
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.area() < other.area()

    @classmethod
    def get_type(cls) -> str:
        return cls.figure_type

    @classmethod
    def get_instance_count(cls) -> int:
        return cls._instance_count

    @staticmethod
    def get_formula() -> str:
        return "Area = (3√3/4) * (2R√3)^2 = 3√3 * R^2"

    def get_info(self) -> dict:
        return {
            'type': self.figure_type,
            'radius': self._R,
            'side': self._side,
            'perimeter': self.perimeter(),
            'area': self.area(),
            'color': self._color_obj.color,
            'label': self._label
        }


def validate_input(prompt: str, input_type: type = float, min_val: float = None) -> any:
    while True:
        try:
            user_input = input(prompt)
            if not user_input.strip():
                print("Input cannot be empty. Please try again.")
                continue

            value = input_type(user_input)

            if min_val is not None and value <= min_val:
                print(f"Value must be greater than {min_val}. Please try again.")
                continue

            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


def get_color_input() -> str:
    """Get color input from user with validation for matplotlib colors"""
    valid_colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta',
                    'orange', 'purple', 'brown', 'pink', 'gray', 'lightblue',
                    'lightgreen', 'lightcoral', 'lightsalmon', 'lightyellow',
                    'lavender', 'thistle', 'plum', 'orchid', 'violet']

    print("\nAvailable colors:", ", ".join(valid_colors[:12]) + "...")

    while True:
        color = input("Enter fill color (e.g., blue, red, green): ").strip().lower()
        if not color:
            print("Color cannot be empty. Please try again.")
        else:
            return color


def get_label_input(default: str = "Triangle") -> str:
    """Get label/text input for figure"""
    label = input(f"Enter label for the figure (press Enter for default '{default}'): ").strip()
    if not label:
        return default
    return label


def draw_triangle(triangle: Triangle, title: str = None, save_path: Optional[str] = None) -> None:
    vertices = triangle.get_vertices()
    center_x, center_y = triangle.get_center()

    fig, ax = plt.subplots(figsize=(12, 10), facecolor='white')

    triangle_patch = patches.Polygon(
        vertices,
        closed=True,
        facecolor=triangle.color_obj.color,
        alpha=triangle.color_obj.opacity,
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(triangle_patch)

    circle = plt.Circle(
        (center_x, center_y),
        triangle.R,
        color='black',
        fill=False,
        linewidth=2,
        linestyle='--'
    )
    ax.add_patch(circle)

    ax.plot([center_x, center_x + triangle.R], [center_y, center_y], 'r-', linewidth=1.5)
    ax.annotate(f'R = {triangle.R:.2f}',
                xy=(center_x + triangle.R / 2, center_y + 0.1),
                fontsize=11, color='red', fontweight='bold')

    ax.annotate(f'side = {triangle.side:.2f}',
                xy=(triangle.side / 2, -triangle.side / 12),
                fontsize=11, ha='center', fontweight='bold')

    ax.plot(center_x, center_y, 'ro', markersize=6)
    ax.annotate('Center', xy=(center_x, center_y), xytext=(center_x + 0.2, center_y + 0.2),
                fontsize=10)

    label_x = triangle.side / 2
    label_y = triangle.side * math.sqrt(3) / 4
    ax.annotate(triangle.label,
                xy=(label_x, label_y),
                fontsize=14,
                fontweight='bold',
                ha='center',
                va='center',
                color='darkblue',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                          edgecolor='black', alpha=0.8))

    # Information panel
    info_text = (
        f"Figure: {triangle.figure_type}\n"
        f"Radius (R): {triangle.R:.2f}\n"
        f"Side length: {triangle.side:.2f}\n"
        f"Perimeter: {triangle.perimeter():.2f}\n"
        f"Area: {triangle.area():.2f}\n"
        f"Color: {triangle.color_obj.color}\n"
        f"Label: {triangle.label}\n"
        f"Formula: {triangle.get_formula()}"
    )

    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.95))

    # Set axes
    margin = triangle.side * 0.1
    ax.set_xlim(-margin, triangle.side + margin)
    ax.set_ylim(-margin, triangle.side * math.sqrt(3) / 2 + margin)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel('X coordinate', fontsize=12)
    ax.set_ylabel('Y coordinate', fontsize=12)

    # Set title
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    else:
        ax.set_title(f"Triangle circumscribed about circle (R={triangle.R})",
                     fontsize=14, fontweight='bold')

    # Axes lines
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)

    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='s', color='w', label=f'Triangle ({triangle.color_obj.color})',
               markerfacecolor=triangle.color_obj.color, markersize=15),
        Line2D([0], [0], linestyle='--', color='black', label='Inscribed circle'),
        Line2D([0], [0], color='red', label='Radius (R)'),
        Line2D([0], [0], marker='o', color='w', label='Center',
               markerfacecolor='red', markersize=8)
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to {save_path}")

    plt.show()


def task4():
    print("\n" + "=" * 60)
    print("Task 4: Triangle circumscribed about a circle")
    print("=" * 60)
    print("\nVariant 16: Triangle with user-defined fill color and text label")

    os.makedirs("data", exist_ok=True)

    print("\n--- Enter triangle parameters ---")
    R = validate_input("Enter circle radius R (positive number): ", float, min_val=0)
    color = get_color_input()
    label = get_label_input()

    try:
        triangle = Triangle(R, color, label)

        print("\n" + "=" * 40)
        print("Triangle Information:")
        print("=" * 40)

        print(f"\n{triangle}")
        print(f"Representation: {repr(triangle)}")

        print(f"\nFigure type (class attribute): {Triangle.get_type()}")
        print(f"Total instances created: {Triangle.get_instance_count()}")
        print(f"Area formula: {Triangle.get_formula()}")

        info_dict = triangle.get_info()
        print(f"\nAll parameters: {info_dict}")

        title = f"Triangle ({label}) circumscribed about circle (R={R})"
        draw_triangle(triangle, title, save_path="data/triangle_variant16.png")

        output_file = "data/triangle_info.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Task 4 Results - Variant 16\n")
            f.write("=" * 50 + "\n\n")
            f.write(str(triangle) + "\n\n")
            f.write("All parameters:\n")
            for key, val in info_dict.items():
                f.write(f"  {key}: {val}\n")
            f.write(f"\nInstance count: {Triangle.get_instance_count()}\n")

        print(f"\nTriangle information saved to {output_file}")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    task4()