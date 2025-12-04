from collections import deque

class Dinic:
    def __init__(self, n_comp):
        self.n_comp = n_comp
        self.lista_adj = [[] for _ in range(n_comp)]
        self.arestas = []

    def adicionar_aresta(self, origem, destino, capacidade):
        # Aresta de ida
        self.lista_adj[origem].append(len(self.arestas))
        self.arestas.append([destino, capacidade, 0])
        # Aresta de retorno (para o algoritmo de fluxo)
        self.lista_adj[destino].append(len(self.arestas))
        self.arestas.append([origem, 0, 0])

    def bfs(self, origem, destino):
        self.nivel = [-1] * self.n_comp
        fila = deque([origem])
        self.nivel[origem] = 0
        
        while fila:
            atual = fila.popleft()
            for idx_aresta in self.lista_adj[atual]:
                proximo, capacidade, fluxo = self.arestas[idx_aresta]
                if capacidade - fluxo > 0 and self.nivel[proximo] == -1:
                    self.nivel[proximo] = self.nivel[atual] + 1
                    fila.append(proximo)
        
        return self.nivel[destino] != -1

    def dfs(self, atual, destino, fluxo_atual):
        if atual == destino or fluxo_atual == 0:
            return fluxo_atual
        
        for i in range(self.ponteiro[atual], len(self.lista_adj[atual])):
            idx_aresta = self.lista_adj[atual][i]
            proximo, capacidade, fluxo = self.arestas[idx_aresta]
            
            if capacidade - fluxo > 0 and self.nivel[proximo] == self.nivel[atual] + 1:
                fluxo_aumentado = self.dfs(proximo, destino, min(fluxo_atual, capacidade - fluxo))
                
                if fluxo_aumentado > 0:
                    self.arestas[idx_aresta][2] += fluxo_aumentado  # Aumenta fluxo na aresta de ida
                    self.arestas[idx_aresta ^ 1][2] -= fluxo_aumentado  # Diminui fluxo na aresta de retorno
                    return fluxo_aumentado
            
            self.ponteiro[atual] += 1
        
        return 0

    def calcular_fluxo_maximo(self, origem, destino):
        fluxo_total = 0
        INFINITO = 10**18
        
        while self.bfs(origem, destino):
            self.ponteiro = [0] * self.n_comp
            
            while True:
                fluxo_aumentado = self.dfs(origem, destino, INFINITO)
                if fluxo_aumentado == 0:
                    break
                fluxo_total += fluxo_aumentado
        
        return fluxo_total


n_comp, n_cabos = map(int, input().split())

dinic = Dinic(n_comp)

for _ in range(n_cabos):
    origem, destino, capacidade = map(int, input().split())
    # Ajustando índices para 0-based (computador 1 vira índice 0)
    dinic.adicionar_aresta(origem - 1, destino - 1, capacidade)

# Fonte é o computador 1 (índice 0) e destino é o computador n (índice n-1)
resultado = dinic.calcular_fluxo_maximo(0, n_comp - 1)
print(resultado)