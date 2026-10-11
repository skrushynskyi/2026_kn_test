class Figure:

    def __init__(self, figure_type: str, length: float):
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль!")

        valid_types = ["квадрат", "прямокутник", "трикутник"]
        if figure_type not in valid_types:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")

        self.figure_type = figure_type
        self.length = length

    def get_figure_type(self) -> str:
        return self.figure_type

    def get_figure_length(self) -> float:
        return self.length

    def get_angles(self) -> int:
        angles_map = {"квадрат": 4, "прямокутник": 4, "трикутник": 3}
        return angles_map.get(self.figure_type, 0)