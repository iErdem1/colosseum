import json
from gladiator import *
from audience import *


class Arena:
    def __init__(self):
        self.gladiators = []
        self.audienceArray = []
        self.winners = []

        self.up_counter = 0
        self.down_counter = 0

        for i in range(3):
            self.a = Audience()
            self.audienceArray.append(self.a)
        with open('gladiators.json') as f:
            data = json.load(f)

        for i in data:
            g = Gladiator(i['name'], i['age'], i['birthplace'], i['health'])
            self.gladiators.append(g)

        for k in self.audienceArray:
            k.set()

        self.fight()

    def fight(self):
        #if len(self.gladiators) % 2 == 0:
        while len(self.gladiators) > 1:
            length = int(len(self.gladiators) / 2)
            for i in range(length):
                gladiator1 = self.gladiators[i]
                gladiator2 = self.gladiators[-(i+1)]
                for j in self.audienceArray:
                    gladiator1.register(j)
                    gladiator2.register(j)
                while gladiator1.damagedhealth > 0 and gladiator2.damagedhealth > 0:
                    gladiator1.damagedhealth = gladiator1.damagedhealth - gladiator2.hitpoint
                    gladiator2.damagedhealth = gladiator2.damagedhealth - gladiator1.hitpoint
                    if gladiator1.damagedhealth > 0 and gladiator2.damagedhealth > 0:
                        gladiator1.notify("harmed")
                        gladiator2.notify("harmed")
                    elif gladiator1.damagedhealth <= 0 and gladiator2.damagedhealth > 0:
                        gladiator1.notify("g2")
                        gladiator2.notify("g2")

                        self.decider = randint(0, 1)

                        if self.decider == 0:
                            self.down_counter += 1
                        else:
                            self.up_counter += 1

                        self.winners.append(gladiator2)
                    elif gladiator1.damagedhealth > 0 and gladiator2.damagedhealth <= 0:
                        gladiator1.notify("g1")
                        gladiator2.notify("g1")
                        self.winners.append(gladiator1)

                        self.decider = randint(0, 1)

                        if self.decider == 0:
                            self.down_counter += 1
                        else:
                            self.up_counter += 1

                        if self.down_counter > self.up_counter:
                            self.a.action(ThumbsDown())
                        else:
                            self.a.action(ThumbsUp(gladiator2, self.winners))

                for k in self.audienceArray:
                    gladiator1.deregister(k)
                    gladiator2.deregister(k)


            self.gladiators = []
            for i in self.winners:
                i.damagedhealth = i.health
                self.gladiators.append(i)
            self.winners = []
