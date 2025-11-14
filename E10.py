# Teoria dos números

# Checar se um número é primo
def eh_primo(p):
    if p < 2:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True

# Encontrar o menor primo > n
def proximo_primo(n):
    p = n + 1
    while not eh_primo(p):
        p += 1
    return p

# Algoritmo de euclides: encontra o MDC entre dois números
def mdc(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = mdc(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# JUnta tudo e retorna o inverso
def calc_a(n, t):
    p = proximo_primo(n)
    g, x, y = mdc(t, p)
    return x % p

n, t = map(int, input().split())
print(calc_a(n, t))