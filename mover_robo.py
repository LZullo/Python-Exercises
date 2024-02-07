def obter_movimento(comando):
    movimentos = {'L': -1, 'R': 1}
    if comando in movimentos:
        return movimentos[comando]
    else:
        raise ValueError(f"Comando inválido: {comando}")

def mover_robo(posicao_inicial, comandos):
    posicao_final = posicao_inicial + sum(map(obter_movimento, comandos))

    return posicao_final

posicao_inicial=0
comandos=['L','R','L','R']
comando=[]
print(mover_robo(posicao_inicial,comandos))


