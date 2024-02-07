#Há n crianças em fila. Cada filho recebe um valor de classificação fornecido na matriz de inteiros ratings.
# Você está dando doces a essas crianças sujeitas aos seguintes requisitos:
# Cada criança deve ter pelo menos um doce. As crianças com uma classificação mais elevada ganham mais doces do que os seus vizinhos. Devolva o número mínimo de doces que você precisa para distribuir os doces às crianças .

def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Passagem da esquerda para a direita
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Passagem da direita para a esquerda e atualização das notas se necessário
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

list_kids = [1, 2, 87, 87, 87, 2, 1]
print(candy(list_kids))
