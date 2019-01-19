class Dog:

    # Class Attribute
    species = "mammal"

    # Initializer / Instance Attributes
    def __init__(self, name="fido", age=1):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

if __name__ == '__main__':

    mikey = Dog()

    # call our instance methods
    print(mikey.description())
    print(mikey.speak("Gruff Gruff"))
    print(mikey.species)









