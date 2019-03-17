class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is siting")


class Life:
    def __init__(self):
        self.max_life = 15


class JinMaoDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.life = Life()

    def max_life(self):
        print(self.life.max_life)


my_dog = Dog("dog", 18)
my_dog.sit()
my_jinMaoDog = JinMaoDog('ddd', 1)
my_jinMaoDog.sit()
my_jinMaoDog.max_life()
