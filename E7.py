def prox_batida(s):
    """
        Retorna o indice da proxima batida.
    """
    if len(s) > 2:
        menor = min(s[1:-1], key=lambda t: t[0])
        return s.index(menor)+1
    else:
        menor = min(s, key=lambda t: t[0])
        return s.index(menor)

def batida(s, idx):
    """
        Bate em uma das reliquias e faz as alterações necessárias nas colunas.
    """
    # Decremento do número do indice
    valor, tipo = s[idx]
    if valor - 1 < 0:
        return KeyError
    s[idx] = (valor-1, tipo)

    # Cria uma nova coluna
    if valor - 1 == 0:
        # Caso 1: deleta o topo elemento
        if tipo == "topo" and len(s) > idx + 1:
            valor, tipo = s[idx+1]
            s[idx+1] = valor-1, "topo"
        # Caso 2: deleta a base elemento
        elif tipo == "base" and len(s) > idx:
            valor, tipo = s[idx-1]
            s[idx-1] = valor, "base"
        # Caso 3: deleta um elemento do meio -> não precisa fazer nada
        # Caso 4: deleta o ultimo elemento -> só deleta
        del s[idx]
    else:
        # Caso 1: subtrai o topo do elemento
        if tipo == "topo" and len(s) > idx + 1:
            valor, tipo = s[idx+1]
            s[idx+1] = valor-1, "topo"
        # Caso 2: subtrai a base elemento
        elif tipo == "base" and len(s) > idx:
            valor, tipo = s[idx-1]
            s[idx-1] = valor, "base"
        # Caso 3: subtrai um elemento do meio -> só subtrair
        # Caso 4: subtrai o ultimo elemento  -> só subtrair

def calc_n_batidas(s):
    n_batidas = 0
    while len(s) != 0:
        idx = prox_batida(s)

        # Batida (Cascata)
        batida(s, idx)
        n_batidas += 1

    return n_batidas

n_reliquias = int(input())
reliquias = list(map(int, input().split()))

print(calc_n_batidas(n_reliquias))