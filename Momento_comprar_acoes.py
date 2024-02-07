#Melhor momento para vender e comprar ações
# Você recebe uma matriz pricesonde prices[i] está o preço de uma determinada ação no dia.ith
# Você deseja maximizar seu lucro escolhendo um único dia para comprar uma ação e escolhendo um dia diferente no futuro para vendê-la.
# Retorne o lucro máximo que você pode obter com esta transação . Se você não conseguir obter nenhum lucro, devolva 0.
# Exemplo 1:
# Entrada: preços = [7,1,5,3,6,4]
# Saída: 5
# Explicação: Compre no dia 2 (preço = 1) e venda no dia 5 (preço = 6), lucro = 6-1 = 5.
# Observe que não é permitido comprar no dia 2 e vender no dia 1 porque você deve comprar antes de vender.
# Exemplo 2:
# Entrada: preços = [7,6,4,3,1]
# Saída: 0
# Explicação: Neste caso, nenhuma transação é feita e o lucro máximo = 0.
prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
    comprar = float('inf')
    lucro = 0

    for i in prices:
        if i < comprar:
            comprar = i
        elif i - comprar > lucro:
            lucro = i - comprar

    return lucro

print(maxProfit(prices))
