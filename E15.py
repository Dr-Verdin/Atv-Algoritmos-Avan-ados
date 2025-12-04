# memo + DFS

import sys
sys.setrecursionlimit(10**6)

def win(v):
    if memo[v] != -1:
        return bool(memo[v])
    # se não há saídas, perde
    if not cidade[v]:
        memo[v] = 0
        return False
    # se existe sucessor que é perdedor, v é vencedor
    for u in cidade[v]:
        if not win(u):
            memo[v] = 1
            return True
    memo[v] = 0
    return False


n_casos = int(input())

for _ in range(n_casos):
    quant_locais, quant_pistas, ponto_inicial = map(int, input().split())

    cidade = [[] for _ in range(quant_locais)]

    for _ in range(quant_pistas):
        u, v = map(int, input().split())
        cidade[u].append(v)

    # memo: -1 = não visitado, 0 = perdedor, 1 = vencedor
    memo = [-1] * quant_locais
    print("Ash" if win(ponto_inicial) else "Noir")