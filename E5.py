
# Número de trechos
nTrechos = int(input())

for _ in range(nTrechos):
    # Número de jogadores
    nPlayersTrecho = int(input())
    localPlayers = []

    # Posição dos jogadores
    for _ in range(nPlayersTrecho):
        inicio, final = input().split()
        localPlayers.append([inicio, final])

    