from abc import ABC, abstractmethod


class Human(ABC):

    @abstractmethod
    def about_info(self):
        raise NotImplemented('Nothing to say.')

    @abstractmethod
    def make_money(self):
        raise NotImplemented("I can't do it.")

    @abstractmethod
    def buy_house(self, house_cost):
        raise NotImplemented("I can't do it.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class Person(Human):
    def __init__(self, name, age, availability_of_money, having_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_home = having_home

    def buy_house(self, house: House):
        if self.availability_of_money > house.cost:
            self.availability_of_money -= house.cost
            self.having_home = True
            print(f'{self.name} have bought a house! House cost is {house.cost}, house area is {house.area}m2')
        else:
            print(f"{self.name} haven't bought this house!")

    def make_money(self):
        self.availability_of_money += 500

    def about_info(self):
        print(f"My name is {self.name}, I'm {self.age} y.o. I have {self.availability_of_money}$ and what about my own house - {self.having_home}")


human = Person('Lisa', 34, availability_of_money=5000, having_home=False)
house = House(area=40, cost=3000)
human.buy_house(house)
print(human.about_info())