class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def animal_factory(pet_type: str):
    pets = {"dog": Dog, "cat": Cat}
    return pets[pet_type]()


pet = animal_factory("dog")
print(pet.speak())