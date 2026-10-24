print("Welcome to the Band Name Generator!")

# Ask the user for the city they grew up in
city = input("What city did you grow up in?\n")

# Ask the user for the name of a pet
pet = input("What is the name of a pet?\n")

# Combine them to make the band name
band_name = city + " " + pet

print("Your band name could be: " + band_name + "!")

import random

print("Welcome to the Random Band Name Generator!")

# Create lists of cool words
adjectives = ["Electric", "Midnight", "Crimson", "Neon", "Cosmic", "Iron"]
nouns = ["Tigers", "Shadows", "Echoes", "Riders", "Phantoms", "Rebels"]

# Pick one random word from each list
word1 = random.choice(adjectives)
word2 = random.choice(nouns)

# Combine and print
print("Your newly generated band name is: " + word1 + " " + word2)