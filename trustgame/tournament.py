from trustgame.base import *


def play_match(first: Player, second: Player, rounds=10, price: Price = Price(), inversions=False, probability=0.):
    score1, score2 = 0, 0

    for i in range(rounds):
        decision1, decision2 = first.make_turn(), second.make_turn()

        # TODO: decision inversion

        score1 += price.price[decision1][decision2]
        score2 += price.price[decision2][decision1]

        first.set_turn_result(Turn(mine=decision1, opponent=decision2))
        second.set_turn_result(Turn(mine=decision2, opponent=decision1))

    return score1, score2


def play_tournament(participants, rounds=10, price: Price = Price(), inversions=False, probability=0.):
    size = len(participants)
    score = [0] * size

    for i in range(size):
        for j in range(i + 1, size):
            score1, score2 = play_match(participants[i], participants[j], rounds=rounds, price=price,
                                        inversions=inversions, probability=probability)
            score[i] += score1
            score[j] += score2
            participants[i].clear()
            participants[j].clear()

    return score


def play_survival(participants, environment, rounds=10, price: Price = Price(), inversions=False, probability=0.):
    size_part, size_env = len(participants), len(environment)
    score = [0] * size_part

    for p in range(size_part):
        for e in range(size_env):
            score[p] += play_match(participants[p], environment[e], rounds=rounds, price=price, inversions=inversions,
                                   probability=probability)[0]
            participants[p].clear()
            environment[e].clear()

    return score
