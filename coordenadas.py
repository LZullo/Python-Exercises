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

listapacote = [{'id': 1, 'x': 2, 'y': 2},
               {'id': 2, 'x': 10, 'y': 10},
               {'id': 3, 'x': 5, 'y': 5}]

listacentros = [{'id': 1, 'x': 9, 'y': 9},
                {'id': 2, 'x': 1, 'y': 1},
                {'id': 3, 'x': 35, 'y': 35}]

def find_nearest_centro(pacote, centros):
    return min(centros, key=lambda centro: distance.euclidean((pacote['x'], pacote['y']), (centro['x'], centro['y'])))['id']

def group_pacotes_by_centro(listapacotes, listacentros):
    result = {}
    for pacote in listapacotes:
        centro_id = find_nearest_centro(pacote, listacentros)
        result.setdefault(centro_id, []).append(pacote['id'])

    return result

output = group_pacotes_by_centro(listapacote, listacentros)
print(output)