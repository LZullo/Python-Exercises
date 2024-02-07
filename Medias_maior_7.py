#Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0
#-----------
#Make a program that asks for two grades from 5 students, calculate and store the average of each student in a vector, 
#print the number of students with an average greater than or equal to 7.0

import unittest
from unittest.mock import patch

def media():
    vetor_media = [(input('Digite o Nome do aluno:'), (float(input('Nota 1:')) + float(input('Nota 2:'))) / 2) for _ in range(3) if (nota := (nota1 + nota2) / 2) >= 7.0]
    return vetor_media

class TestMediaFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['Joao', '8', '9', 'Maria', '6', '8', 'Ana', '7', '7'])
    def test_media(self, mock_input):
        result = media()
        self.assertEqual(result, [('Joao', 8.5), ('Ana', 7.0)])

if __name__ == '__main__':
    unittest.main()
