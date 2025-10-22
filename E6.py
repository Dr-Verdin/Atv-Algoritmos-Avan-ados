def cross(a, b, c):
    """
        Função que calcula o produto vetorial
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) 

def monotone_chain(points):
    """
        Convex hull (Andrew) - retorna pontos em anti-horário, sem pontos colineares internos
    """
    pts = sorted(points)
    if len(pts) <= 1:
        return pts[:]
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def merge_hulls(hull_right, hull_left):
    """
        Merge robusto: calcula convex hull dos vértices das duas metades.
    """
    return monotone_chain(hull_left+hull_right)

def convex_hull_sorted(pts_sorted):
    """
        Recursiva — recebe a lista já ordenada por x (e y para desempate).
    """
    if len(pts_sorted) <= 3:
        return monotone_chain(pts_sorted)
    mid = len(pts_sorted) // 2
    left = convex_hull_sorted(pts_sorted[:mid])
    right = convex_hull_sorted(pts_sorted[mid:])
    return merge_hulls(left, right)

def convex_hull(pedras):
    """ 
        Função para calcular o fecho convexo 
    """
    # Ordenar pelo eixo x (energia arcana)
    pts_sorted = sorted(pedras)
    
    return convex_hull_sorted(pts_sorted)

# ------------------------------------------------------------------

# Número de casos testes
n_casos = int(input())

for i in range(n_casos):
    # Número de pedras no templo
    n_pedras = int(input())
    pedras = []

    for _ in range(n_pedras):
        energia_arcana, vibracao_mistica = map(float, input().split())
        pedras.append([energia_arcana, vibracao_mistica])

    # Achar fecho convexo
    colar = convex_hull(pedras)

    print(f"Caso {i+1}:")
    print(f"Tamanho do colar: {len(colar)}")
    print(f'Pedras ancestrais: {",".join(f"({e:.4f},{v:.4f})" for e, v in colar)}\n')    