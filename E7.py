# Leitura da entrada
n_reliquias = int(input())
reliquias = list(map(int, input().split()))

# Tabela
# A DP precisa guardar o menor custo para cada escolha, porque a escolha de um elemento afeta a próxima escolha
# i: indica até qual elemento de reliquias estamos considerando
# j: indica o estado do elemento atual (0 ou 1)
dp = [[0, 0] for _ in range(n_reliquias+1)]

# Inicialização
dp[0][0] = 0
dp[0][1] = 1

for i in range(n_reliquias):
    dp[i+1][0] = min(dp[i][0], dp[i][1]) + reliquias[i]
    dp[i+1][1] = min(dp[i][1] + (reliquias[i] - 1), dp[i][0] + max(reliquias[i] - i, 0))

print(min(dp[n_reliquias][0], dp[n_reliquias][1]))