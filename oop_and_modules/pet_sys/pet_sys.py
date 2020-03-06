
from pets import Pets
from bulldog import Bulldog
from jackal import Jackal
from dog import Dog
# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    Jackal("JK", 7), 
    Dog("GS", 9)
]

my_dogs.append(Bulldog("Jimmy",8))

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("All dogs are {}s".format(dog.species))