def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def find_upper_tangent(esq, dir, idx_esq, idx_dir):
    n_esq, n_dir = len(esq), len(dir)
    done = False

    while not done:
        done = True

        # enquanto ponto seguinte no hull direito estiver acima da tangente, move para frente
        while cross(esq[idx_esq], dir[idx_dir],
                    dir[(idx_dir + 1) % n_dir]) >= 0:
            idx_dir = (idx_dir + 1) % n_dir
            done = False

        # enquanto ponto anterior no hull esquerdo estiver acima, move para trás
        while cross(dir[idx_dir], esq[idx_esq],
                    esq[(idx_esq - 1) % n_esq]) <= 0:
            idx_esq = (idx_esq - 1 + n_esq) % n_esq
            done = False

    return idx_esq, idx_dir
    
def find_lower_tangent(esq, dir, idx_esq, idx_dir):
    n_esq, n_dir = len(esq), len(dir)
    done = False

    while not done:
        done = True

        # enquanto ponto seguinte no hull direito estiver acima da tangente, move para frente
        while cross(esq[idx_esq], dir[idx_dir],
                    dir[(idx_dir - 1 + n_dir) % n_dir]) <= 0:
            idx_dir = (idx_dir - 1 + n_dir) % n_dir
            done = False

        # enquanto ponto anterior no hull esquerdo estiver acima, move para trás
        while cross(dir[idx_dir], esq[idx_esq],
                    esq[(idx_esq + 1) % n_esq]) >= 0:
            idx_esq = (idx_esq + 1) % n_esq
            done = False

    return idx_esq, idx_dir

def merge_hulls(esq, dir):
    # encontrar indices dos pontos mais a direita do hull esquerdo e mais À esquerda do hull direito
    idx_esq = max(range(len(esq)), key=lambda i: esq[i][0])
    idx_dir = min(range(len(dir)), key=lambda i: dir[i][0])

    # ENcontrar tangente superior
    upper_esq, upper_dir = find_upper_tangent(esq, dir, idx_esq, idx_dir)

    # Encontrar tangente inferior
    lower_esq, lower_dir = find_lower_tangent(esq, dir, idx_esq, idx_dir)

    # combinar pontos do hull esquerdo e direito entre as tangentes
    merged = []
    i = upper_esq
    merged.append(esq[i])
    while i != lower_esq:
        i = (i + 1) % len(esq)
        merged.append(esq[i])

    i = lower_dir
    merged.append(dir[i])
    while i != upper_dir:
        i = (i + 1) % len(dir)
        merged.append(dir[i])

    return merged

def ordenar_hull_final(hull):
    # ponto inicial: menor Ei e menor Vi
    start = min(range(len(hull)), key=lambda i: (hull[i][0], hull[i][1]))
    hull = hull[start:] + hull[:start]

    # garantir anti-horário
    if len(hull) >= 3:
        if cross(hull[0], hull[1], hull[2]) < 0:
            hull.reverse()
    return hull

def convex_hull(pontos):
    pontos = [[round(x,4), round(y,4)] for x, y in pontos]

    # Ordenar pontos
    pontos.sort(key=lambda p: (p[0], p[1]))

    # Caso base
    if len(pontos) <= 3:
        if len(pontos) == 3 and cross(pontos[0], pontos[1], pontos[2]) < 0:
            pontos[1], pontos[2] = pontos[2], pontos[1]
        return pontos
    
    # Dividir em duas metades
    meio = len(pontos) // 2
    esq = pontos[:meio]
    dir = pontos[meio:]

    # COnquista (recursão)
    hull_esq = convex_hull(esq)
    hull_dir = convex_hull(dir)

    # Combinar (merge)
    merged = merge_hulls(hull_esq, hull_dir)
    return ordenar_hull_final(merged)

# Número de casos testes
n_casos = int(input())

for i in range(n_casos):
    # Número de pedras no templo
    n_pedras = int(input())
    pedras = []

    for _ in range(n_pedras):
        energia_arcana, vibracao_mistica = map(float, input().split())
        pedras.append([energia_arcana, vibracao_mistica])

    colar = convex_hull(pedras)

    print(f"Caso {i+1}:")
    print(f"Tamanho do colar: {len(colar)}")
    print(f'Pedras ancentrais: {", ".join(f"({e:.4f}, {v:.4f})" for e, v in colar)}\n')