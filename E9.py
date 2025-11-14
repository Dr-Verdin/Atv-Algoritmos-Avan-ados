# dp[i][s]: A maior quantidade de diamantes possível no início do dia i, estando no estado s
# - s = 0: sem passe
# - s = 1: com passe
# - s = 2: descanso obrigatorio
# A DP vai processando os dias, atualizando os estados possíveis do próximo dia

import sys

def resolve_fase(diam, valores, dias):
    NEG = -10**18   # inicializar estados possíveis

    # matriz DP com dias + 1 linhas e 3 colunas (os estados). Dia 0, estado 0, temps diamantes, nos outros estados -infinito
    dp = [[NEG]*3 for _ in range(dias+1)]   
    dp[0][0] =  diam

    # Processar cada dia
    for i in range(dias):
        v = valores[i]  # pega o valor daquele dia

        # Estado 0: sem passe
        if dp[i][0] > NEG:  # estado 0
            dp[i+1][0] = max(dp[i+1][0], dp[i][0])  # pular (não faz nada; max serve para ele guardar o melhor caminho possível)
            if dp[i][0] >= v:   # comprar passe
                dp[i+1][1] = max(dp[i+1][1], dp[i][0]-v)    # no proximo dia estara com passe
        
        # Estado 1: com passe
        if dp[i][1] > NEG:
            dp[i+1][1] = max(dp[i+1][1], dp[i][1])      # pular mantendo o passe
            dp[i+1][2] = max(dp[i+1][2], dp[i][1]+v)    # garimpar (ganha v e usa o passe)

        # Estado 2: descanso obrogatorio
        if dp[i][2] > NEG:
            dp[i+1][0] = max(dp[i+1][0], dp[i][2])  # volta para o estado sem passe

    return max(dp[dias])

n_fases = int(input())

for _ in range(n_fases):
    start_diam = int(input())
    dias = int(input())
    valores_dias = list(map(int, input().split()))

    print(resolve_fase(start_diam, valores_dias, dias))


