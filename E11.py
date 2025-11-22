# Implementar DSU
import sys

def union(pai, tamanho, u, v):
    """
        Une os conjuntos que contêm os elementos u e v.
    """
    # encontra as raízas de u e v
    ru = find(pai, u)
    rv = find(pai, v)

    # se já tem a mesma raiz, já estão no mesmo conjunto
    if ru == rv:
        return False
    # união por tamanho: anexar a árvore menor à maior
    if tamanho[ru] < tamanho[rv]:
        ru, rv, = rv, ru    # troca para garantir ru é a maior raiz

    # faz rv apontar para ru (une os conjuntos) e atualiza o tamanho
    pai[rv] = ru
    tamanho[ru] += tamanho[rv]
    return True

def find(pai, x):
    """
        Descobre qual é a raiz (representante) do conjunto ao qual o elemento x pertence.
    """
    while pai[x] != x:
        pai[x] = pai[pai[x]]    # faz x pular um nível (reduz altura)
        x = pai[x]              # continua subindo
    return x

# número de casos testes
n_casos = int(input())

for _ in range(n_casos):
    n_atomos, n_ligacoes = map(int, input().split())

    # inicialização
    pai = [i for i in range(n_atomos + 1)]
    tamanho = [1] * (n_atomos + 1)

    # processar arestas
    for _ in range(n_ligacoes):
        u, v = map(int, input().split())
        union(pai, tamanho, u, v)

    # contar componentes: colecione raízes adjuntas distintas
    raizes = set()
    for v in range(1, n_atomos + 1):
        raizes.add(find(pai, v))
    print(len(raizes))