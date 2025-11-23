from collections import defaultdict
import heapq

def dijkistra(grafo, inicio, fim):
    distancia = {v: float('inf') for v in grafo}
    predecessor = {v: None for v in grafo}

    distancia[inicio] = 0
    pq = [(0, inicio)]

    while pq:
        dist_u, u = heapq.heappop(pq)

        if u == fim:
            break

        if dist_u > distancia[u]:
            continue

        for v, peso in grafo[u]:
            nova_dist = dist_u + peso
            if nova_dist < distancia[v]:
                distancia[v] = nova_dist
                predecessor[v] = u
                heapq.heappush(pq, (nova_dist, v))

    return distancia, predecessor

n_comp, quant_cabos = map(int, input().split())

conexoes = []
for _ in range(quant_cabos):
    u, v, c = map(int, input().split())
    conexoes.append([u, v, c])

adj = {}
for u, v, c in conexoes:
    adj.setdefault(u, []).append((v, c))
    if v not in adj:
        adj[v] = []

# achar o menor caminho entre 1 e n_comp
dist, pred = dijkistra(adj, 1, n_comp)
print(dist[n_comp])