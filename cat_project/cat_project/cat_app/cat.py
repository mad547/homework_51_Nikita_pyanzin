import json
import os
import random


FILENAME = "cats.json"


class Cat:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age
        self.hp = random.randint(20, 100)
        self.mood = random.randint(20, 100)
        self.satiety = random.randint(20, 100)
        self.average_level = (self.hp + self.mood + self.satiety) // 3
        self.is_sleeping = False

    def feed(self):
        if self.is_sleeping:
            return "Спящего кота нельзя кормить"
        self.satiety += 15
        self.mood += 5
        if self.satiety > 100:
            self.satiety = 100
            self.mood -= 30
        self._update_stats()
        return f"Кот {self.name} поел"

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.mood -= 5
            self._update_stats()
            return f"Кот {self.name} проснулся но не в настроении"
        self.mood += 15
        self.satiety -= 10
        if random.randint(1, 3) == 1:
            self.mood = 0
            self._update_stats()
            return f"Кот {self.name} разозлился"
        self._update_stats()
        return f"Кот {self.name} поиграл"

    def sleep(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.mood -= 5
            self._update_stats()
            return f"Кот {self.name} проснулся"
        self.is_sleeping = True
        return f"Кот {self.name} уснул"

    def _update_stats(self):
        self.hp = max(0,min(100,self.hp))
        self.mood = max(0,min(100,self.mood))
        self.satiety = max(0,min(100,self.satiety))
        self.average_level = (self.hp + self.mood + self.satiety) // 3

    def get_avatar(self):
        if self.mood >= 70:
            return 'images/happy.jpeg'
        elif self.mood >= 40:
            return 'images/normal.jpeg'
        else:
            return 'images/sad.jpeg'

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'hp': self.hp,
            'mood': self.mood,
            'satiety': self.satiety,
            'average_level': self.average_level,
            'is_sleeping': self.is_sleeping
        }

    @staticmethod
    def from_dict(data):
        cat = Cat(data['name'], data['age'])
        cat.hp = data['hp']
        cat.mood = data['mood']
        cat.satiety = data['satiety']
        cat.average_level = data['average_level']
        cat.is_sleeping = data.get('is_sleeping', False)
        return cat

def load_cats():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r', encoding="utf-8") as f:
            data = json.load(f)
            return [Cat.from_dict(d) for d in data]
    except:
        return []

def save_cats(cats):
    data = [c.to_dict() for c in cats]
    with open(FILENAME, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)