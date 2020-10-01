from setup import *


class Person:
    def __init__(self):
        self.age = 0
        self.income = rand.randrange(10, 100, 10)
        self.money = 0
        self.health = 100
        self.hunger = 100
        self.energy = 100
        self.food = 0
        self.birthday = 0

    def update(self, day):
        # Everyday
        self.check_bday(day)
        self.work()
        self.check_buy()
        self.check_hunger()
        dead = self.check_death()
        if dead:
            return True
        return False

    def check_bday(self, day):
        if self.birthday % day:
            self.age += 1

    def check_hunger(self):
        # Starve if too late
        if 10 < self.hunger <= 20:
            self.health -= 2

        elif self.hunger <= 10:
            self.health -= 5

        # Eat if possible
        elif self.hunger <= 70:
            if self.food > 0:
                self.food -= 1
                self.hunger += 20

    def check_buy(self):
        if self.money >= 100:
            self.money -= 100
            self.food += 1

    def check_death(self):
        if self.health <= 0:
            return True

        return False

    def work(self):
        self.money += self.income
        self.use_energy(20)

    def use_energy(self, amount):
        self.energy -= amount
        if self.energy <= 50:
            self.hunger -= 10
            self.energy += 20

            # If hunger goes negative, go to 0 and damage.
            if self.hunger < 0:
                self.health += self.hunger
                self.hunger = 0
