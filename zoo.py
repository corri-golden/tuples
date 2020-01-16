
# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("lion", "tiger", "bear", "shark", "cheetah", "snake", "rabbit", "dog", "sheep", "wolf")

# Find one of your animals using the tuple.index(value) syntax on the tuple
# print(zoos.index("bear"))

# Determine if an animal is in your tuple by using value in tuple syntax
animal_to_find = "cheetah"
if animal_to_find in zoo:
    # Print that the animal was found
    print(f"{animal_to_find} was found!")

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.

animals = ("lion", "tiger", "bear", "shark", "cheetah", "snake", "rabbit", "dog", "sheep", "wolf")
# (first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = animals
# print(first_animal)
# print(second_animal)
# print(third_animal)
# print(fourth_animal)
# print(fifth_animal)
# print(sixth_animal)
# print(seventh_animal)
# print(eighth_animal)
# print(ninth_animal)
# print(tenth_animal)

# Convert your tuple into a list.
animalList = list(animals)
# new_animals = ("bird", "zebra", "fox")

animalList.extend(["bird", "zebra", "fox"])
# print(animalList)

animalListTuple = tuple(animalList)
print(animalListTuple)







# convert tuple into a list

