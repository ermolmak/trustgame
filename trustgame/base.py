class Action:
    cooperate = 0
    cheat = 1


class Turn:
    def __init__(self, mine, opponent):
        self.mine = mine
        self.opponent = opponent


class Player:
    def make_turn(self):
        pass

    def set_turn_result(self, turn: Turn):
        pass

    def clear(self):
        pass


class Price:
    def __init__(self, cooperation=2, cheating=0, winner=3, loser=-1):
        self.cooperation = cooperation
        self.cheating = cheating
        self.winner = winner
        self.loser = loser
        self.price = [[cooperation, loser], [winner, cheating]]
