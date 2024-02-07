#Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as notas lidas e a respectiva média.
#-----------

#Make a program that reads 4 student grades and, at the end, shows the read grades and the respective average on the screen.

class Aluno2:
    def __init__(self, nome, nota1=0, nota2=0, nota3=0, nota4=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def get_media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def __str__(self):
        return f"Nome: {self.nome}\nNotas: {self.nota1:.1f}, {self.nota2:.1f}, {self.nota3:.1f}, {self.nota4:.1f}\nMédia: {self.get_media():.1f}"

a3 = Aluno2('Pedro Antonio', 8, 10, 10, 9)
a4 = Aluno2('Maria Luiza', 7, 7.5, 9, 9)
print(a4)
