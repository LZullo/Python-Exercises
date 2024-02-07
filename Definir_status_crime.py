#Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# . "Mora perto da vítima?"
# d. "Devia dinheiro para a vítima?"
# e. "Já trabalhou com a vítima?"
#-----------
# No final, o programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"; entre 3 e 4, como "Cúmplice", e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
# Using lists, write a program that asks a person 5 questions about a crime. The questions are:*
# a. "Did you call the victim?"
# b. "Were you at the crime scene?"
# c. "Do you live near the victim?"
# d. "Did you owe the victim money?"
# e. "Have you ever worked with the victim?"
# At the end, the program must issue a rating on the person's participation in crime. If the person responds positively to 2 questions, he/she should be classified as "Suspect"; between 3 and 4, as "Accomplice", and 5 as "Murderer". Otherwise, he will be classified as "Innocent".

op = 1
while (op ==1):
  lista = []
  print(" Interrogatório:\n")
  lista.append(int(input("Telefonou para a vítima ? 1- SIM ou 0-NAO :" )))
  lista.append(int(input("Esteve no local do crime? 1- SIM ou 0-NAO :" )))
  lista.append(int(input("Mora perto da vítima? 1- SIM ou 0-NAO : ")))
  lista.append(int(input("Devia para a vítima? 1- SIM ou 0-NAO : " )))
  lista.append(int(input("Já trabalhou com a vítima? 1- SIM ou 0-NAO : " )))
  if sum(lista) < 2:
        print("\n Pessoa Inocente\n")
  elif sum(lista) == 2:
        print("\n Pessoa Suspeita\n")
  elif sum(lista) in [3, 4]:
        print("\n Pessoa Cúmplice\n")
  else:
        print("\n Pessoa Assassino\n")
  op = int(input("Deseja Interrogar outra Pessoa ? 1- SIM ou 2 - NAO :"))
print("\n")