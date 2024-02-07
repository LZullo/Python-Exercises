#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.
#-----------
#Write a program that reads 20 integers and stores them in an array. 
#Store the even numbers in the EVEN vector and the ODD numbers in the odd vector. Print the three vectors.

vetor = [[], [], []]

for _ in range(20):
    numero = int(input('Digite um número: '))
    vetor[0].append(numero)

    if numero % 2 == 0:
        vetor[1].append(numero)
    else:
        vetor[2].append(numero)

def par_impar(lista):
    vetor_par = [num for num in lista if num % 2 == 0]
    vetor_impar = [num for num in lista if num % 2 != 0]
    return vetor_par, vetor_impar

# Teste da função par_impar
vetor_par, vetor_impar = par_impar(vetor[0])
assert vetor_par == vetor[1]
assert vetor_impar == vetor[2]

print("Todos os números:", vetor[0])
print("Pares:", vetor[1])
print("Ímpares:", vetor[2])
