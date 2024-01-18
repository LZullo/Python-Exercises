#Há n crianças em fila. Cada filho recebe um valor de classificação fornecido na matriz de inteiros ratings.
# Você está dando doces a essas crianças sujeitas aos seguintes requisitos:
# Cada criança deve ter pelo menos um doce. As crianças com uma classificação mais elevada ganham mais doces do que os seus vizinhos. Devolva o número mínimo de doces que você precisa para distribuir os doces às crianças .

list_kids=[1,2,87,87,87,2,1]

def candy(ratings):
  candies = [1] * len(ratings)
  for i in range(1, len(ratings) ):
      if ratings[i] > ratings[i-1]:
          candies[i] = candies[i-1] + 1
  for i in range(len(ratings)-2, -1, -1):
      if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
          candies[i] = candies[i+1] + 1
  return sum(candies)

print(candy(list_kids))