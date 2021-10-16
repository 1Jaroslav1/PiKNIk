class Move:
    def __init__(self, old_position, new_position):
        self._old_position = old_position
        self._new_position = new_position
    
    def get_old_position(self):
        return self._old_position
    
    def get_new_position(self):
        return self._new_position
    
    def __str__(self):
        return f"{self._new_position}"

    def __repr__(self):
        return f"{self._new_position}"
