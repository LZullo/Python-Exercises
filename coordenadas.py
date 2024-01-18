# Encontrar o centro mais proximo de cada pacote, para enviá-lo, de acordo com as coordenadas.
# Exemplo:
# Entrada:
# listapacote=[{'id':1 ,'x':2, 'y':2},
#       {'id':2 ,'x':10, 'y':10},
#       {'id':3 ,'x':5, 'y':5}]
# listacentros=[{'id':1 ,'x':9, 'y':9},
#       {'id':2 ,'x':1, 'y':1},
#       {'id':3 ,'x':35, 'y':35}]
# Saída:
# Formato:
# {centro: pacote} => {Centro 2: [Pacote 1], Centro 1: [Pacote 2, Pacote 3]
# {2: [1], 1: [2, 3]})

from scipy.spatial import distance
from collections import defaultdict #biblioteca utilizada para o agrupamento do resultado, por idcentro

listapacote=[{'id':1 ,'x':2, 'y':2},
              {'id':2 ,'x':10, 'y':10},
              {'id':3 ,'x':5, 'y':5}]

listacentros=[{'id':1 ,'x':9, 'y':9},
              {'id':2 ,'x':1, 'y':1},
              {'id':3 ,'x':35, 'y':35}]

#Organizando a saída, agrupando os valores do dicionário pelo mesmo centro id, tendo como saida no formato {idcentro: [idpacotes],...}
def optimizes_output(saida):
  result = defaultdict(list)
  for s in saida:
      result[s["idcentro"]].append(s["idpacote"])
  print(result)

#Função Euclidiana
def Return_distance(x1,y1,x2,y2):
  a = [x1,x2]
  b = [x2,y2]
  return distance.euclidean(a,b)

#Função para encontrar a menor diatancia, pacote por pacote com todos os centros listados, verificando qual a menor distancia
def Find_shortest_distance(listapacotes,listacentros):
  saida=[]
  i=0
  for pacote in listapacotes:
    text={'idcentro':None, 'idpacote': pacote['id'], 'dist':None}
    saida.append(text)
    for centro in listacentros:
        dist=Return_distance(pacote['x'],pacote['y'],centro['x'],centro['y'])
        if saida[i]['dist']==None or dist<saida[i]['dist']: #atualizando a saida, substituindo o idcentro pelo idcentro com menor distancia
          saida[i].update({"idcentro": centro['id']})
          saida[i].update({"dist": dist})
    del saida[i]['dist'] #distância não é mais necessária para saída
    i=i+1
  optimizes_output(saida)

Find_shortest_distance(listapacote,listacentros)