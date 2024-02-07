#Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos 
#possuem altura inferior à média de altura desses alunos.
#-----------
#Make a Program that reads the ages and heights of 10 students and determines how many students over 13 are taller 
#than the average height of those students.
from statistics import mean

def alunos_abaixo_media():
    total_alunos = 10
    alturas = []

    for _ in range(total_alunos):
        idade = int(input('Digite a idade do aluno:'))
        altura = float(input('Digite a altura do aluno:'))
        alturas.append(altura)

    media_alturas = mean(alturas)

    alunos_abaixo_media = sum(1 for altura in alturas if idade > 13 and altura < media_alturas)

    return alunos_abaixo_media

print(alunos_abaixo_media())

