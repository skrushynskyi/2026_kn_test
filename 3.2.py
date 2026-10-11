import unittest
from app import Figure


class TestFigure(unittest.TestCase):

    def test_get_figure_length(self):
        fig = Figure("квадрат", 10)
        self.assertEqual(fig.get_figure_length(), 10)

    def test_get_angles(self):
        square = Figure("квадрат", 5)
        rectangle = Figure("прямокутник", 8)
        triangle = Figure("трикутник", 3)

        self.assertEqual(square.get_angles(), 4)
        self.assertEqual(rectangle.get_angles(), 4)
        self.assertEqual(triangle.get_angles(), 3)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", -5)

    def test_unknown_figure_type(self):
        with self.assertRaises(ValueError):
            Figure("коло", 10)


if __name__ == "__main__":
    unittest.main()