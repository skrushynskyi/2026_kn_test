import unittest


def count_vowels(text: str) -> int:
    """Рахує кількість голосних літер у рядку (латиниця + кирилиця)."""
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")

    vowels = set("aeiouyAEIOUYаеєиіїоуюяАЕЄИІЇОУЮЯ")
    return sum(1 for char in text if char in vowels)


class TestCountVowels(unittest.TestCase):

    def test_english_words(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_mixed_case(self):
        # 'y' та 'o' — це 2 голосні
        self.assertEqual(count_vowels("PyThOn"), 2)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    # --- Завдання 5 (🔥): Додаткові тести ---
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_string_with_digits_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#$"), 0)
        # 'y' та 'o' у "Python 3.10!" — це 2 голосні
        self.assertEqual(count_vowels("Python 3.10!"), 2)

    def test_ukrainian_letters(self):
        # 'и', 'і', 'У', 'а', 'і', 'а' — це 6 голосних
        self.assertEqual(count_vowels("Привіт, Україна"), 6)


if __name__ == "__main__":
    unittest.main()