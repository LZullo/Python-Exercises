#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.
#-----------
#Write a program that reads 20 integers and stores them in an array. 
#Store the even numbers in the EVEN vector and the ODD numbers in the odd vector. Print the three vectors.

n=0
vetor=[[],[],[]]
while	(n<20):
    numero	=	int(input('Digite	um	número:	'))
    vetor[0].append(numero)
    if numero%2 ==0:
      vetor[1].append(numero)
    else:
      vetor[2].append(numero)
    n +=1

def test_par_impar(self):
    vetor_par,vetor_impar=par_impar([1,2,3,4,5,6])
    assert vetor_par==[2,4,6]
    assert vetor_impar==[1,3,5]

print("Todos os numeros:",vetor[0])
print("Pares:",vetor[1])
print("Impares:",vetor[2])