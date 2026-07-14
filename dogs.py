class labrador:

    species = "dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

mickie = labrador("Mickie", 12 )
minnie = labrador("Minnie", 10)

print("Mickie is a {}".format(mickie.species))
print("Minnie is also a {}".format(minnie.species))

print("{} is {} years old".format(mickie.name, mickie.age))
print("{} is {} years old".format(minnie.name, minnie.age))