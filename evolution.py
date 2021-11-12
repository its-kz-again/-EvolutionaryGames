from player import Player
import numpy as np
from config import CONFIG
import json
import random
from copy import deepcopy

class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        if random.uniform(0, 1) < 0.3:
            child.nn.w1 += np.random.normal(0, 0.5, size=child.nn.w1.shape)
        if random.uniform(0, 1) < 0.3:
            child.nn.w2 += np.random.normal(0, 0.5, size=child.nn.w2.shape)
        if random.uniform(0, 1) < 0.4:
            child.nn.b1 += np.random.normal(0, 0.5, size=child.nn.b1.shape)
        if random.uniform(0, 1) < 0.4:
            child.nn.b2 += np.random.normal(0, 0.5, size=child.nn.b2.shape)

        return child

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            f = []
            for p in prev_players:
                ff = p.fitness
                f.append(ff ** 4)
            parents = random.choices(prev_players, weights=f, k=num_players)
            children = []
            for p in parents:
                child = deepcopy(p)
                children.append(self.mutate(child))

            # TODO (additional): a selection method other than `fitness proportionate`
            # crossover
            parents2 = []
            children2 = []
            for i in range(num_players):
                p1, p2 = random.choices(prev_players, weights=f, k=2)
                parents2.append(p1)
                parents2.append(p2)
                # w1, b1 from p1 and w2, b2 from p2
                child = deepcopy(p1)
                child.nn.w2 = p2.nn.w2
                child.nn.b2 = p2.nn.b2
                children2.append(self.mutate(child))

            return children2

    def next_population_selection(self, players, num_players):

        # sort the players.fitness
        players.sort(key=lambda x: x.fitness, reverse=True)

        # a selection method other than `top-k`
        mini = min(players, key=lambda x: x.fitness).fitness
        maxi = max(players, key=lambda x: x.fitness).fitness
        avg = 0
        for p in players:
            avg += p.fitness
        sum = avg
        avg = avg / len(players)

        probability = []
        # tmp = 0
        for p in players:
            probability.append(p.fitness / sum)
        new_players = random.choices(players, weights=probability, k=num_players)
        # new_players = []
        # count = 0
        # for k in range(num_players):
        #     probability_select = random.uniform(0, 1)
        #     for i, prob in enumerate(probability):
        #         if not(new_players.__contains__(players[i])):
        #             if prob > probability_select:
        #                 new_players.append(players[i])
        #                 count += 1
        #                 break
        # for i in range(num_players - count):
        #     for j in players:
        #         if not(new_players.__contains__(j)):
        #             new_players.append(j)
        #             break
        # plotting
        with open("data.json", 'r+') as f:
                in_list = json.load(f)
                in_list['min'].append(str(mini))
                in_list['avg'].append(str(avg))
                in_list['max'].append(str(maxi))
                f.seek(0)
                json.dump(in_list, f, indent=4)

        # return players[: num_players]
        return new_players