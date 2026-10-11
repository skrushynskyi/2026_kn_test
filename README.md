![Звіт до роботи](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg)

**Звіт до Роботи**

**Тема роботи: Загальне тестування та Unit тестування**

**1.Загальне тестування та юніт-тести**

**1.1.Перевірка даних — Завдання 3**

![Скріншот-1](1.png)

**1.2.Тестування функцій — Завдання 4**

![Скріншот-2](2.png)

**1.3.Тестування функцій — Завдання 5**

![Скріншот-3](2.png)

**2.Перший приклад**

**1.1.Перший приклад — Завдання 5**

![Скріншот-4](3.1.png)

**1.2.Перший приклад — Завдання 6**

![Скріншот-5](3.1.png)

![Скріншот-6](3.2.png)

**1.3.Перший приклад — Завдання 7**

![Скріншот-7](3.1.png)

![Скріншот-8](3.2.png)

**3.Розширені можливості**

**1.1.Розширені можливості — Завдання 4**

![Скріншот-9](4.png)

**1.2.Розширені можливості — Завдання 5**

![Скріншот-10](4.png)

**1.Запуск окремих тестових файлів здійснюється з терміналу VS Code за допомогою таких команд:**

Bash
# Запуск перевірки введеного числа
python tasks/task1_validation.py

# Запуск юніт-тестів для підрахунку голосних
python tasks/task2_vowels.py

# Запуск юніт-тестів для класу Figure
python tasks/task3_test.py

# Запуск розширених тестів (subTest та mock.patch)
python tasks/task4_advanced.py

Також усі тести можна запустити однією командою через стандартний runner unittest у розширеному режимі (verbose):

python -m unittest discover -s tasks -p "*test*.py" -v

**2.Результат виконання тестів**

test_english_words (task2_vowels.TestCountVowels) ... ok
test_mixed_case (task2_vowels.TestCountVowels) ... ok
test_no_vowels (task2_vowels.TestCountVowels) ... ok
test_empty_string (task2_vowels.TestCountVowels) ... ok
test_string_with_digits_and_symbols (task2_vowels.TestCountVowels) ... ok
test_ukrainian_letters (task2_vowels.TestCountVowels) ... ok
test_get_figure_length (task3_test.TestFigure) ... ok
test_get_angles (task3_test.TestFigure) ... ok
test_zero_length (task3_test.TestFigure) ... ok
test_negative_length (task3_test.TestFigure) ... ok
test_unknown_figure_type (task3_test.TestFigure) ... ok
test_all_figure_types_with_subtest (task4_advanced.TestAdvancedFeatures) ... ok
test_get_user_figure_length (task4_advanced.TestAdvancedFeatures) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.006s

OK

**3.Тест, який спочатку не проходив, та його виправлення***

При виконанні task2_vowels.py тест test_mixed_case повертав помилку FAIL:

FAIL: test_mixed_case (task2_vowels.TestCountVowels)
Traceback (most recent call last):
  File "tasks/task2_vowels.py", line 19, in test_mixed_case
    self.assertEqual(count_vowels("PyThOn"), 1)
AssertionError: 2 != 1

Причина помилки: У слові "PyThOn" присутні дві голосні літери (y та o), але в очікуваному результаті тесту було помилково вказано значення 1.

Виправлення:

def test_mixed_case(self):
    # 'y' та 'o' — це 2 голосні
    self.assertEqual(count_vowels("PyThOn"), 2)

**4.Пояснення призначення subTest та mock у власному прикладі**

Призначення subTest (у файлі task4_advanced.py):

subTest використовується для параметризованого тестування декількох наборів даних у межах одного тестового методу.
Перевага: Якщо один з параметрів (наприклад, для "прямокутник") зазнає невдачі, виконання тесту не зупиняється на ньому. unittest перевірить усі інші параметри ("квадрат", "трикутник") та точно вкаже, на яких саме даних стався збій. 

Призначення mock / patch (у файлі task4_advanced.py):

Декоратор @patch("builtins.input", return_value="15.5") ізолює тест від зовнішнього інтерактивного введення.
Перевага: Він підміняє стандартну системну функцію input() на об'єкт-макет (mock), який автоматично повертає заздалегідь визначений рядок "15.5". Це дозволяє повністю автоматизувати тестування функцій з користувацьким введенням без зупинки програми та очікування ручних дій користувача

