# Função para calcular o número de ultrapassagens (qunado a ordem relativa dos jogadores muda)
def calc_ultrapassagens(local_jogadores):
    ultrapassagens = 0
    n  = len(local_jogadores)

    for i in range(n):
        for j in range(i+1, n):
            pos_inicial_i, pos_final_i = local_jogadores[i]
            pos_inicial_j, pos_final_j = local_jogadores[j]

            # Verifica se houve ultrapassagem
            if (pos_inicial_i > pos_inicial_j  and  pos_final_i < pos_final_j) \
            or (pos_inicial_i < pos_inicial_j  and  pos_final_i > pos_final_j):
                ultrapassagens += 1

    return ultrapassagens

# Número de trechos
n_trechos = int(input())
ultrapassagens_trecho = []                # Armazena os trechos com a quantidade de ultrapassagens

for trecho in range(n_trechos):
    # Número de jogadores
    n_jogadores_trecho = int(input())
    local_jogadores = []

    # Posição dos jogadores
    for _ in range(n_jogadores_trecho):
        inicio, final = map(int, input().split())
        local_jogadores.append([inicio, final])

    # Calculo do número de ultrapassagens
    total_ultrapassagens = calc_ultrapassagens(local_jogadores)

    ultrapassagens_trecho.append([trecho, total_ultrapassagens])

# Ordenar os trechos de acordo com o número de ultrapassagens
ultrapassagens_trecho.sort(key=lambda x: x[1], reverse=True)

# Imprimir resultado
for trecho, n_ultrapassagens in ultrapassagens_trecho:
    print(trecho, n_ultrapassagens)