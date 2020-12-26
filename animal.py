class Animal:
    def __init__(self, size, age):
        self.size = size
        self.age = age

    def info(self):
        print(f"My animal's size is {self.size} and is {self.age} years old.")


class Cat(Animal):
    def __init__(self, size, age, name):
        super().__init__(size, age)
        self.name = name

    def info(self):
        print(f"My cat's name is {self.name}, it size is {self.size} and is {self.age} years old.")

    def sleep(self):
        print('Sleeping is my favorite!')


class Dog(Animal):
    def __init__(self, size, age, name):
        super().__init__(size, age)
        self.name = name

    def info(self):
        print(f"My dog's name is {self.name}, it size is {self.size} and is {self.age} years old.")

    def run(self):
        print('Running is my favorite!')


class Parrot(Animal):
    def __init__(self, size, age, name):
        super().__init__(size, age)
        self.name = name

    def info(self):
        print(f"My parrot's name is {self.name}, it size is {self.size} and is {self.age} years old.")

    def sing(self):
        print('Singing is my favorite!')


class Hamster(Animal):
    def __init__(self, size, age, name):
        super().__init__(size, age)
        self.name = name

    def info(self):
        print(f"My hamster's name is {self.name}, it size is {self.size} and is {self.age} years old.")

    def spin(self):
        print('Spinning the wheel is my favorite!')


class Fish(Animal):
    def __init__(self, size, age, name):
        super().__init__(size, age)
        self.name = name

    def info(self):
        print(f"My fish's name is {self.name}, it size is {self.size} and is {self.age} years old.")

    def swim(self):
        print('Swimming is my favorite!')