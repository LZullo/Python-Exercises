#Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.
#-----------
#Make a program that reads a string and tells you how many consonants were read. Print the consonants.

def count_consonants(input_str):
    consonants = 0
    consonant_list = [char for char in input_str.lower() if char.isalpha() and char not in "aeiou"]

    consonants = len(consonant_list)

    print('The Consonants:', consonant_list)
    print('\nThe number of consonants:', consonants)

input_str = input("Please enter a string: ")
count_consonants(input_str)

# Teste
assert count_consonants('cachorro') == 5
