from Figures.Figure import Figure

class Queen(Figure):
    def __init__(self, name, position, team):
        super().__init__(name, position, team)
        self._combinations = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        self._long_step_move = True
        self._weight = 90
        if not team:
            self._weight = -90