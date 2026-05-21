import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.is_sleeping = False

    def feed(self):
        if self.is_sleeping:
            return
        self.satiety += 15
        self.happiness += 5
        if self.satiety > 100:
            self.satiety = 100
            self.happiness -= 30
        if self.happiness < 0:
            self.happiness = 0

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
            if self.happiness < 0:
                self.happiness = 0
            return
        self.happiness += 15
        self.satiety -= 10
        if random.randint(1, 3) == 1:
            self.happiness = 0
        if self.happiness > 100:
            self.happiness = 100
        if self.satiety < 0:
            self.satiety = 0

    def sleep(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
            if self.happiness < 0:
                self.happiness = 0
        else:
            self.is_sleeping = True

    def get_avatar(self):
        if self.happiness >= 70:
            return 'images/happy.jpeg'
        elif self.happiness >= 40:
            return 'images/normal.jpeg'
        else:
            return 'images/sad.jpeg'