from Figures.Figure import Figure
from Move import Move

class King(Figure):
    def __init__(self, name, position, team, is_moved = False):
        super().__init__(name, position, team)
        self._combinations = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        self._long_step_move = False
        self._is_moved = is_moved
        self._weight = 900
        if not team:
            self._weight = -900

    def if_castling(self, board):
        fields_for_castling = []

        team = self._team
        if board.is_check(team):
            return fields_for_castling

        if not self._is_moved:
            array = board.get_array()
            row = self.get_position()[0]

            castling_data = [[0, [1, 4], 2], [7, [5, 7], 6]]

            for data in castling_data:
                if array[row][data[0]].get_name().lower() == "r" and not array[row][data[0]].get_is_moved():
                    castling = True

                    for i in range(data[1][0], data[1][1]):
                        if array[row][i].get_name() != " ":
                            castling = False
                            break

                    if castling:
                        fields_for_castling.append(Move(self._position, [row, data[2]]))

        return fields_for_castling

    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self):
        self._is_moved = True
