# MST 
def kruskal(edges, n):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        # encontra o representante do conjunto
        while x != parent[x]:
            parent[x] = parent[parent[x]]  # compressão de caminho
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False  # já estão conectados, não pode usar essa aresta (formaria ciclo)

        # união por rank
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True
    
    # ordena as arestas pelo peso
    edges_sorted = sorted(edges, key=lambda x: x[2])

    mst = []
    total_cost = 0

    for u, v, w in edges_sorted:
        if union(u, v):
            mst.append((u, v, w))
            total_cost += w

    return mst, total_cost

n_casos = int(input())

for _ in range(n_casos):
    n_camps, n_pontes = map(int, input().split())

    arestas = []
    for _ in range(n_pontes):
        u, v, c = map(int, input().split())
        arestas.append([u, v, c])
    
    pesos = [c for (_, _, c) in arestas]
    if len(pesos) != len(set(pesos)):
        print("Esse nao e o caminho correto para a Cidade Perdida de Z.\n")
        continue

    mst, custo = kruskal(arestas, n_camps)
    
    if len(mst) != n_camps - 1:
        print("O vale nao pode ser completamente atravessado.\n")
        continue

    print(f"custo minimo: {custo}")
    print(f"Pontes reconstruídas:")
    for u, v, c in mst:
        if u > v:
            u, v = v, u
        print(f"{u} - {v}")
    print()