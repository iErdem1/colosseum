from responses import *
from random import *
from abc import ABC, abstractmethod


class Decision(ABC):

    @abstractmethod
    def decide(self):
        pass


class Audience:
    def __init__(self):
        self.responseType = None
        self.decision_type = None

    def action(self, decision):
        decision.decide()

    def update(self, eventtype):
        if eventtype == "harmed":
            return self.responseType.audienceResponse()
        elif eventtype == "g1":
            return self.responseType.audienceResponse()
        elif eventtype == "g2":
            return self.responseType.audienceResponse()

    def set(self):
        rand = randint(0, 2)
        if rand == 0:
            self.responseType = Happy()
        elif rand == 1:
            self.responseType = unHappy()
        else:
            self.responseType = Normal()


class ThumbsUp(Decision):
    def __init__(self, g, array):
        self.g = g
        self.array = array
        self.decide()

    def decide(self):
        self.g.damagedhealth = self.g.health
        self.array.append(self.g)


class ThumbsDown(Decision):
    def __init__(self):
        self.decide()

    def decide(self):
        pass
