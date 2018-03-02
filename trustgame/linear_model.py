from collections import deque

from scipy.stats import norm

from trustgame.base import *


def default_param_evolution(parent1, parent2):
    a = (parent1 + parent2) / 2
    sigma = max(abs(parent1 - parent2) / 2, max(abs(parent1), abs(parent2)) / 10, 0.1)
    return norm.rvs(size=1, loc=a, scale=sigma)[0]


class LinearModel(Player):
    action_to_num = [[0, 1], [2, 3]]

    def __init__(self, memory_size=50):
        self.memory_size = memory_size
        self.coefficients = [[0.0] * 4 for i in range(memory_size)]
        self.free_coefficient = 1.0
        self.memory = deque()

    def make_turn(self):
        decision = self.free_coefficient

        for i in range(len(self.memory)):
            turn = self.memory[i]
            decision += self.coefficients[i][LinearModel.action_to_num[turn.mine][turn.opponent]]

        if decision < 0:
            return Action.cheat
        else:
            return Action.cooperate

    def set_turn_result(self, turn: Turn):
        self.memory.appendleft(turn)
        if len(self.memory) > self.memory_size:
            self.memory.pop()

    def clear(self):
        self.memory.clear()


def linear_model_evolution(parent1: LinearModel, parent2: LinearModel, evolution_func=default_param_evolution):
    if parent1.memory_size != parent2.memory_size:
        raise ValueError("parents have different memory sizes")

    new_free_coefficient = evolution_func(parent1.free_coefficient, parent2.free_coefficient)
    new_coefficients = [[evolution_func(parent1.coefficients[i][j], parent2.coefficients[i][j]) for j in range(4)] for i
                        in range(parent1.memory_size)]

    result = LinearModel(memory_size=parent1.memory_size)
    result.free_coefficient = new_free_coefficient
    result.coefficients = new_coefficients
    return result
