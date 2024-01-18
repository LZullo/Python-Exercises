#Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as notas lidas e a respectiva média.
#-----------

#Make a program that reads 4 student grades and, at the end, shows the read grades and the respective average on the screen.

#Opção1
# info=[]
# op=1
# while op== 1:
#     nome	= (input('Digite	o Nome do aluno:'))
#     nota1	=	float(input('Nota 1:'))
#     nota2	=	float(input('Nota 2:'))
#     nota3	=	float(input('Nota 3:'))
#     nota4	=	float(input('Nota 4:'))
#     media=(nota1 + nota2+ nota3+nota4)/4
#     txt = 'Nome: ' + nome
#     txt += ' Notas: %2.1f, %2.1f, %2.1f, %2.1f' % (nota1, nota2, nota3, nota4)
#     txt += ' Média: %2.1f' % media
#     info.append(txt)
#     op	= int(input('Deseja adicionar as notas de outro aluno? (Não=0):'))

# print(info)

#Opção2
class Aluno2:
    def __init__(self, nome, nota1=0, nota2=0, nota3=0,nota4=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def get_media(self):
        return (self.nota1 + self.nota2 + self.nota3 +self.nota4)/4

    def __str__(self):
        txt = 'Nome: ' + self.nome
        txt += '\nNotas: %2.1f, %2.1f, %2.1f, %2.1f' % (self.nota1, self.nota2, self.nota3, self.nota4)
        txt += '\nMédia: %2.1f' % self.get_media()
        return txt

a3 = Aluno2('Pedro Torees',8,10,10,9)
a4 = Aluno2('Maria Luiza',7,7.5,9,9)
print(a4.__str__())