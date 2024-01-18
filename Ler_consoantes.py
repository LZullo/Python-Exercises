#Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.
#-----------
#Make a program that reads a string and tells you how many consonants were read. Print the consonants.

def count_consonants(str):
  consonants=0
  show=[]
  str.lower()
  for i in str:
      if i not in "aeiou" and i.isalpha():
            consonants=consonants+1
            show.append(i)
  print('The Consonants:',show)
  print('\nThe number of consonant:', consonants)


str=input("Please enter a string: ")
count_consonants(str)

def test_count_consonants(self):
    assert count_consonants('cachorro') == 5