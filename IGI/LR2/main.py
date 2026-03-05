import json
import os
import sys

try:
    from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
    from geometric_lib.square import area as square_area, perimeter as square_perimeter
except ImportError as e:
    print(f"Ошибка импорта geometric_lib: {e}")
    print("Убедитесь, что библиотека geometric_lib находится в правильной директории")
    sys.exit(1)

def load_config(config_path):
    """Загрузка конфигурации из JSON файла"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ОШИБКА: Конфигурационный файл {config_path} не найден!")
        print("Убедитесь, что вы смонтировали volume с config.json в /config/")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ОШИБКА: Неверный формат JSON в файле {config_path}")
        print(f"Детали: {e}")
        sys.exit(1)

def main():
    print("=" * 60)
    print("Геометрические вычисления с использованием Docker")
    print("Библиотека geometric_lib (circle.py и square.py)")
    print("=" * 60)
    
    # Путь к конфигурационному файлу (всегда через volume)
    config_path = '/config/config.json'
    
    print(f"\nЗагрузка конфигурации из {config_path}")
    config = load_config(config_path)
    
    # Получение типа фигуры из конфига
    figure_type = config.get('figure_type')
    if not figure_type:
        print("ОШИБКА: В конфигурационном файле не указан 'figure_type'")
        print("Допустимые значения: 'circle' или 'square'")
        sys.exit(1)
    
    print(f"Тип фигуры: {figure_type}")
    print("-" * 40)
    
    # Получение параметров из конфига
    params = config.get('params', {})
    
    if figure_type == 'circle':
        # Получение радиуса из конфига
        radius = params.get('radius')
        if radius is None:
            print("ОШИБКА: Для круга необходимо указать 'radius' в params")
            sys.exit(1)
        
        radius = float(radius)
        print(f"Радиус: {radius}")
        print(f"Площадь круга: {circle_area(radius):.2f}")
        print(f"Длина окружности: {circle_perimeter(radius):.2f}")
        
    elif figure_type == 'square':
        # Получение стороны из конфига
        side = params.get('side')
        if side is None:
            print("ОШИБКА: Для квадрата необходимо указать 'side' в params")
            sys.exit(1)
        
        side = float(side)
        print(f"Сторона квадрата: {side}")
        print(f"Площадь квадрата: {square_area(side):.2f}")
        print(f"Периметр квадрата: {square_perimeter(side):.2f}")
        
    else:
        print(f"ОШИБКА: неизвестный тип фигуры '{figure_type}'")
        print("Допустимые типы: 'circle', 'square'")
        sys.exit(1)
    
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())