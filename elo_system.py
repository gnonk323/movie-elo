import math


def probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


def match(movie1, movie2, outcome, k=30):

    m1_elo = float(movie1.elo)
    m2_elo = float(movie2.elo)

    prob1 = probability(m1_elo, m2_elo)
    prob2 = probability(m2_elo, m1_elo)

    if outcome.equals(movie1):
        movie1.set_elo(round(m1_elo + k * (1 - prob1), 2))
        movie2.set_elo(round(m2_elo + k * (0 - prob2), 2))

    elif outcome.equals(movie2):
        movie1.set_elo(round(m1_elo + k * (0 - prob1), 2))
        movie2.set_elo(round(m2_elo + k * (1 - prob2), 2))
