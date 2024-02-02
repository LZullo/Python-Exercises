import json

def transformar_para_centavos(valor):
    return int(valor * 100) if isinstance(valor, float) else valor

def analisar_solicitacao(solicitacao):
    pessoa = solicitacao.get("pessoa", {})
    score = solicitacao.get("score", {})
    imovel = solicitacao.get("imovel", {})
    
    renda = transformar_para_centavos(pessoa.get("renda", 0))
    entrada = transformar_para_centavos(solicitacao.get("entrada", 0))
    cpf = pessoa.get("cpf", "")

    constraints = []

    if score.get("pontuacao", 0) < 500:
        constraints.append("score-insuficiente")

    if renda <= 200000:  # 2000 * 100 para representar centavos
        constraints.append("renda-insuficiente")

    if "valor" in imovel and entrada < 0.05 * transformar_para_centavos(imovel["valor"]):
        constraints.append("entrada-insuficiente")

    status = "aprovado" if not constraints else "reprovado-parcialmente" if "entrada-insuficiente" in constraints and len(constraints)==1 else "reprovado"

    return {
        "cpf": cpf,
        "status": status,
        "constraints": constraints
    }

def main():
    entrada_json = input("Insira o JSON de entrada: ")
    try:
        entrada = json.loads(entrada_json)
    except json.JSONDecodeError:
        print("Erro: Entrada inválida. Certifique-se de que a entrada está no formato JSON.")
        return

    resultado = analisar_solicitacao(entrada)
    saida_json = json.dumps(resultado, indent=2)
    print("Resultado:")
    print(saida_json)

if __name__ == "__main__":
    main()
