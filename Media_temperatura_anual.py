#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, 
#calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas 
#ocorreram (mostrar o mês por extenso: 1 Janeiro, 2 – Fevereiro, . . . ).
#-----------
#Make a program that takes the average temperature for each month of the year and stores them in a list. 
#After that, calculate the annual average of temperatures and show all temperatures above the annual average, 
#and in which month they occurred (show the month in full: 1 January, 2 – February, . . . ).

def listar_meses(lista, mediaAnual, listaMes):
    print("Meses com temperaturas acima da média:\n")
    for mes, temperatura in zip(listaMes, lista):
        if temperatura >= mediaAnual:
            print(f'{mes}: Temperatura: {temperatura:.2f}')

def media_temp():
    lista = []
    listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    for i in range(1, 13):
        temp = float(input(f"Digite a Temperatura do Mês_{i}: "))
        lista.append(temp)

    mediaAnual = sum(lista) / len(lista)
    print("Temperatura Média Anual:", mediaAnual)
    listar_meses(lista, mediaAnual, listaMes)

media_temp()


