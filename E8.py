# Estratégia Utilizada -> diferença ótima: dp[i][j]=max(a[i]−dp[i+1][j],a[j]−dp[i][j−1])
def max_score(pedras):
    n = len(pedras)
    if n == 1:
        return pedras[0]

    dp = [[0]*n for _ in range(n)]    # score atual - score oponente
    for i in range(n):
        dp[i][i] = pedras[i]
    for lenght in range(2, n+1):
        for i in range(0, n-lenght+1):
            j = i + lenght - 1
            esq = pedras[i] - dp[i+1][j]
            dir = pedras[j] - dp[i][j-1]
            dp[i][j] = max(esq, dir)
    
    total = sum(pedras)
    diff = dp[0][n-1]   # vantagem do jogador que começa sobre o outro
    score_first = (total + diff) / 2
    score_second = total - score_first

    return int(max(score_first, score_second))


n_casos = int(input())

for _ in range(n_casos):
    n_pedras = int(input())
    if n_pedras % 2 != 0 or n_pedras > 28:
        print("Número de pedras inválido!")

    linha = input().strip()
    partes = linha.split()

    pedras = []
    for p in partes:
        esq, dir = p.strip("()").split(",")
        pedras.append(int(esq) + int(dir))
    
    print(max_score(pedras))