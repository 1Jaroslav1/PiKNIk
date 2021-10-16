from Figures.Knight import Knight
from Figures.Rook import Rook
from Figures.Queen import Queen
from Figures.Bishop import Bishop
from Figures.EmptyField import EmptyField
from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self._board = Board()
        self._time = 0
        self._message = ""
        self.create_players()

    def create_players(self):
        self._playerW = Player(True)
        self._playerB = Player(False)

    def get_board(self):
        return self._board

    def get_time(self):
        return self._time

    def get_message(self):
        return self._message

    def get_playerW(self):
        return self._playerW

    def get_playerB(self):
        return self._playerB

    def set_time(self, new_time):
        self._time = new_time

    def set_message(self, new_message):
        self._message = new_message

    def move(self, player):
        old_x, old_y = 0, 0
        figure = EmptyField([0, 0], " ")

        is_ok = False
        while not is_ok:
            print(f"{self._currentPlayer.get_name()} Choose figure: ")
            old_x, old_y = list(map(int, input().split()))

            figure = self._board.get_array()[old_x][old_y]

            if figure.get_name() != " ":
                if figure.get_team() == player.get_team():
                    next_fields_list = figure.check_next_field(self._board)
                    if len(next_fields_list):
                        is_ok = True
                    else:
                        print("You can`t move this figure choose another one")

                elif figure.get_team() != player.get_team():
                    print("It is not your figure")
                else:
                    print("Choose another figure")
            else:
                print("It is not a figure")

        castling_fields = []
        if figure.get_name().lower() == "k":
            castling_fields = figure.if_castling(self._board)
            for new_field in castling_fields:
                next_fields_list.append(new_field)

        print(f"You can move this figure to: {next_fields_list}")

        is_ok = False
        new_figure = None
        wasCastling = False
        while not is_ok:
            print(f"{self._currentPlayer.get_name()} Choose field to move on: ")
            new_position = list(map(int, input().split()))
            new_x, new_y = new_position

            for next_field in next_fields_list:
                next_field = next_field.get_new_position()
                if new_x == next_field[0] and new_y == next_field[1]:
                    is_ok = True
                    for castling_field in castling_fields:
                        castling_field = castling_field.get_new_position()
                        if next_field == castling_field:
                            self._board.castling(next_field)
                            wasCastling = True
                            break

                    if figure.get_name().lower() == "p" and (new_position[0] == 0 or new_position[0] == 7):
                        nameChoosen = False
                        while not nameChoosen:
                            new_figure_name = input(f"Your pawn will convert to (r, n, b, q): ")
                            if new_figure_name == "r" or new_figure_name == "n" or new_figure_name == "b" or new_figure_name == "q":
                                nameChoosen = True
                            else:
                                print("Choose r, n, b or q")

                        if new_figure_name == "r":
                            if player.get_team():
                                new_figure = Rook("R", new_position, True)
                            else:
                                new_figure = Rook("r", new_position, False)
                        elif new_figure_name == "n":
                            if player.get_team():
                                new_figure = Knight("N", new_position, True)
                            else:
                                new_figure = Knight("n", new_position, False)
                        elif new_figure_name == "b":
                            if player.get_team():
                                new_figure = Bishop("B", new_position, True)
                            else:
                                new_figure = Bishop("b", new_position, False)
                        else:
                            if player.get_team():
                                new_figure = Queen("Q", new_position, True)
                            else:
                                new_figure= Queen("q", new_position, False)

                    if wasCastling:
                        break
                    figure = self._board.get_array()[new_x][new_y]
                    if not figure.get_name() == " ":
                        pass
                    
                    self._board.change_figure_position([old_x, old_y], new_position)
                    if new_figure:
                        self._board.addFigure(new_figure)
                    break

            if not is_ok:
                print("This figure can't go to this field. Try another.")

    def play(self):
        winner = None
        isDraw = False

        round = True
        while True:
            self._board.print_board()
            if round:
                self._currentPlayer = self._playerW
                round = False
                self.move(self._playerW)
                if self._board.is_checkmate(False):
                    winner = self._playerW
                    break
                elif self._board.is_check(False):
                    print("Check!")
            else:
                self._currentPlayer = self._playerB
                round = True
                self.move(self._playerB)
                if self._board.is_checkmate(True):
                    winner = self._playerB
                    break
                elif self._board.is_check(True):
                    print("Check!")
            if self._board.check_if_draw():
                print("Draw")
                isDraw = True
                break

        self._board.print_board()

        if not isDraw:
            print("Checkmate!")
            winner.won()
            print(f"{winner.get_name()} won this round")





