#Crie uma classe para representar datas com as seguintes regras:
#a. deve ter três atributos: o dia, o mês e o ano;
#b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos;
#c. encapsule cada um dos atributos;
#d. forneça o método str para retornar uma representação da data como string. Considere que a deve ser formatada mostrando o dia, o mês e o ano separados por barra (/);
#e. forneça uma operação para avançar uma data para o dia seguinte.
#-----------
#Create a class to represent dates with the following rules:
#a. must have three attributes: the day, the month and the year;
#b. must have a constructor that initializes the three attributes and checks the validity of the provided values;
#c. encapsulate each of the attributes;
#d. provide the str method to return a string representation of the date. Consider that a must be formatted showing the day, month and year separated by a slash (/);
#e. provide an operation to advance a date to the next day.

from datetime import datetime, timedelta

class Data:
    def __init__(self, dia=0, mes=0, ano=0):
        today = datetime.today().date()
        self.__dia = dia if dia != 0 else today.day
        self.__mes = mes if mes != 0 else today.month
        self.__ano = ano if ano != 0 else today.year

    def __str__(self):
        return '{}/{}/{}'.format(self.__dia, self.__mes, self.__ano)

    def dia_seguinte(self):
        self.__dia += 1
        date = datetime(self.__ano, self.__mes, self.__dia) + timedelta(days=0)
        self.__dia, self.__mes, self.__ano = date.day, date.month, date.year

data = Data()  # hoje
print("Data atual =", data)
data.dia_seguinte()
print("Dia seguinte =", data)

data = Data(30, 11, 2021)
print("Data fim do mês =", data)
data.dia_seguinte()
print("Dia seguinte =", data)

data = Data(31, 12, 2021)
print("Data no fim do ano =", data)
data.dia_seguinte()
print("Dia seguinte =", data)
