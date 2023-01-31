# om 419 - lab02

cool_animals = ["cats", "dogs", "falcons", "penguins"]
user_input = ""

while user_input != "y":
    print("here are some of the COOLEST animals:")

    for animal in cool_animals:
        print(animal, end = "! ")

    user_input = input("Enter y to end program: ")