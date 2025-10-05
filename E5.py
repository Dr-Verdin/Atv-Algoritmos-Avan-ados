# FUnção para calcular o número de ultrapassagens
def calc_ultrapassagens(local_jogadores):
    #  desenvolver ...
    return total_ultrapassagens

# Número de trechos
n_trechos = int(input())
ultrapassagens_trecho = []                # Armazena os trechos com a quantidade de ultrapassagens

for trecho in range(n_trechos):
    # Número de jogadores
    n_jogadores_trecho = int(input())
    local_jogadores = []

    # Posição dos jogadores
    for _ in range(n_jogadores_trecho):
        inicio, final = input().split()
        local_jogadores.append([inicio, final])

    # Calculo do número de ultrapassagens
    total_ultrapassagens = calc_ultrapassagens(local_jogadores)

    ultrapassagens_trecho.append([trecho, total_ultrapassagens])

# Ordenar os trechos de acordo com o número de ultrapassagens
ultrapassagens_trecho.sort(key=lambda x: x[1], reverse=True)

# Imprimir resultado
for trecho, n_ultrapassagens in ultrapassagens_trecho:
    print(trecho, n_ultrapassagens)