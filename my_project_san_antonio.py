# -*- coding: utf8 -*-
import random


quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]


characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item(my_list):
    rand_numb = random.randint(0,len(my_list)-1)
    item = my_list[rand_numb]
    return item

def capitalize(words):
    for word in words:
        word.capitalize

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")


while user_answer != "b":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

 