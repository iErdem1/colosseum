class Gladiator:
    def __init__(self, name, age, birthplace, health):
        self.name = name
        self.age = age
        self.birthplace = birthplace
        self.health = health
        self.hitpoint = self.health/10
        self.audienceArray = []
        self.damagedhealth = health

    def notify(self, event):
        for i in self.audienceArray:
            i.update(event)

    def register(self, audience):
        self.audienceArray.append(audience)

    def deregister(self, auidience):
        self.audienceArray.remove(auidience)