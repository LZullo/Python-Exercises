#Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0
#-----------
#Make a program that asks for two grades from 5 students, calculate and store the average of each student in a vector, 
#print the number of students with an average greater than or equal to 7.0

#Opção1
#Opção1
# class Aluno1:
#     def __init__(self, nome, nota1=0, nota2=0):
#         self.nome = nome
#         self.nota1 = nota1
#         self.nota2 = nota2

#     def get_media(self):
#         return (self.nota1 + self.nota2)/2

# vetor_media=[]
# for i in range(5):
#     nome	= (input('Digite	o Nome do aluno:'))
#     nota1	=	float(input('Nota 1:'))
#     nota2	=	float(input('Nota 2:'))
#     aluno=Aluno1(nome,nota1,nota2)
#     media=aluno.get_media()
#     if(media>=7.0):
#       vetor_media.append(media)

# def test_get_media_alunos(self):
#     assert get_media_alunos(7.0,7.0)==7.0

# def test_get_aprovados(self):
#     assert get_aprovados([7.0,5.5,8.3])==2
# print(len(vetor_media))

#Opção2
def media():
  vetor_media=[]
  for i in range(3):
      nome	= (input('Digite	o Nome do aluno:'))
      nota1	=	float(input('Nota 1:'))
      nota2	=	float(input('Nota 2:'))
      media=(nota1 + nota2)/2
      if(media>=7.0):
        vetor_media.append(media)
  return vetor_media

print(len(media()))