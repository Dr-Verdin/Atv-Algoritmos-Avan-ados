# Função para calcular o número de ultrapassagens (qunado a ordem relativa dos jogadores muda)
def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0

    meio = len(arr) // 2
    esquerda, inv_esq = merge_count(arr[:meio])
    direita, inv_dir = merge_count(arr[meio:])

    merged = []
    i = j = 0
    inversoes = inv_esq + inv_dir

    # Merge das duas metades
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            merged.append(esquerda[i])
            i += 1
        else:
            merged.append(direita[j])
            j += 1
            # Todos os elementos restantes da esquerda são maiores -> inversões
            inversoes += len(esquerda) - i

    merged.extend(esquerda[i:])
    merged.extend(direita[j:])

    return merged, inversoes


def calc_ultrapassagens(local_jogadores):
    # Ordena por posição inicial
    local_jogadores.sort(key=lambda x: x[0])

    # Extrai a sequência das posições finais
    finais = [fim for _, fim in local_jogadores]

    # Conta inversões na lista de posições finais
    _, ultrapassagens = merge_count(finais)
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