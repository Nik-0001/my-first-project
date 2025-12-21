"""
Модуль калькулятора с математическими операциями.
Версия 2.0 - с аннотациями типов и обработкой ошибок.
"""

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление двух чисел с проверкой на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def power(a: float, b: float) -> float:
    """Возведение в степень."""
    return a ** b


def square_root(x: float) -> float:
    """Квадратный корень числа."""
    if x < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    return x ** 0.5


def main() -> None:
    """Основная функция для демонстрации."""
    print("Улучшенный калькулятор:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2^3 = {power(2, 3)}")
    
    try:
        print(f"√9 = {square_root(9)}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()