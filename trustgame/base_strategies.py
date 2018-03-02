from trustgame.base import *


class Copycat(Player):
    def __init__(self):
        self.previous = Action.cooperate

    def __repr__(self):
        return 'Copycat'

    def make_turn(self):
        return self.previous

    def set_turn_result(self, turn: Turn):
        self.previous = turn.opponent

    def clear(self):
        self.__init__()


class AllCooperate(Player):
    def __repr__(self):
        return 'AllCooperate'

    def make_turn(self):
        return Action.cooperate


class AllCheat(Player):
    def __repr__(self):
        return 'AllCheat'

    def make_turn(self):
        return Action.cheat


class Grudger(Player):
    def __init__(self):
        self.has_cheated = False

    def __repr__(self):
        return 'Grundger'

    def make_turn(self):
        if self.has_cheated:
            return Action.cheat
        else:
            return Action.cooperate

    def set_turn_result(self, turn: Turn):
        self.has_cheated = self.has_cheated or turn.opponent == Action.cheat

    def clear(self):
        self.__init__()


class Detective(Player):
    initial = [Action.cooperate, Action.cheat, Action.cooperate, Action.cooperate]

    def __init__(self):
        self.times_played = 0
        self.has_cheated = False
        self.previous = Action.cooperate

    def __repr__(self):
        return 'Detective'

    def make_turn(self):
        if self.times_played < 4:
            return Detective.initial[self.times_played]
        elif self.has_cheated:
            return self.previous
        else:
            return Action.cheat

    def set_turn_result(self, turn: Turn):
        self.times_played += 1
        self.has_cheated = self.has_cheated or turn.opponent == Action.cheat
        self.previous = turn.opponent

    def clear(self):
        self.__init__()
