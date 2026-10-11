def check_positive_number(value):
    """Перевіряє, чи є введене значення додатним числом."""
    if not isinstance(value, (int, float)):
        raise TypeError("Введене значення має бути числом!")
    if value <= 0:
        raise ValueError("Число має бути більшим за нуль!")
    return value

if __name__ == "__main__":
    print("Правильне введення")
    try:
        result = check_positive_number(10)
        print(f"Результат: {result} (Перевірку пройдено успішно)")
    except (ValueError, TypeError) as e:
        print(f"Помилка: {e}")

    print("\nНеправильне введення")
    try:
        result = check_positive_number(-5)
        print(f"Результат: {result}")
    except (ValueError, TypeError) as e:
        print(f"Помилка: {e}")