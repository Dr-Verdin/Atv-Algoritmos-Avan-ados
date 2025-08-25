lines, columns = map(int, input().split())

while lines < 1 or lines > 50:
    print("Valor inválido! Digite novamente.")
    lines = int(input("Digite um número de 1 à 50: "))

while columns < 1 or columns > 50:
    print("Valor inválido! Digite novamente.")
    columns = int(input("Digite um número de 1 à 50: "))

word_search = []

for i in range(lines):
    while True:
        line = input().strip()
        if len(line) != columns or not line.isupper():
            print(f"Erro! A linha deve ter exatamente {columns} letras maiúsculas.")
        else:
            word_search.append(list(line))
            break

n_words = int(input())
while n_words < 1 or n_words > 50000:
    print("Valor inválido! Digite novamente.")
    lines = int(input("Digite um número de 1 à 50000: "))

words = []

for i in range(n_words):
    word = input().strip
    words.append(word)

# entrada ok
# sistema de busca na matriz
# saída