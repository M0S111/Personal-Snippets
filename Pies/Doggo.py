class Dog:

    def __init__(self,name,age,weight):
        
        self.name = name
        self.age = age
        self.weight = weight

    def deets(self):

        print(self.name + "'s", 'age is', str(self.age), 'and weight is', str(self.weight) + '.\n')

    def bark(self):

        if self.weight <= 15:

            print(self.name, "says Yip! Yip!\n")

        else:

            print(self.name, "says Woof! Woof!\n")

    def  man_years(self):

        print(self.name, "is", self.age * 7, "in man years.\n")

Chewy = Dog('Chewy',5,13)

Red = Dog('Red',7,22)

Chewy.deets()

Chewy.man_years()

Red.deets()

Red.man_years()

Chewy.bark()

Red.bark()
