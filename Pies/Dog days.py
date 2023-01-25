class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
            
        else:
            print(self.name, 'says "woof woof"')


    def human_years(self):

        dog_name = self.name
        dog_age = self.age

        human_age = int(dog_age) * 7

        return human_age

            
def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age,'and weight is', dog.weight)

    
codie = Dog('Codie', 12, 38)

jackson = Dog('Jackson', 9, 12)

print(codie.name + "'s age in human years is",codie.human_years())
print(jackson.name + "'s age in human years is",jackson.human_years())
