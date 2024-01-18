#Dado um array de inteiros, encontre se o array possui algum valor duplicado. Sua função precisa retornar true se algum elemento aparecer 
#pelo menos duas vezes no array e retornar false se todos os elementos forem distintos.

a=[1,0,2,3,4]
def find_duplicated(a):
  if len(list(set(a)))<len(a):
    return True
  else:
    return False

print(find_duplicated(a))