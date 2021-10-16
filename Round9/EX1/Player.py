class Player:
    def __init__(self, team):
        self._team = team
        self._score = 0
        if team:
            self._name = input("Name of white player: ")
        else:
            self._name = input("Name of black player: ")

    def get_name(self):
        return self._name

    def get_team(self):
        return self._team

    def get_score(self):
        return self._score

    def set_time(self, new_time):
        self._time = new_time

    def won(self):
        self._score += 1
