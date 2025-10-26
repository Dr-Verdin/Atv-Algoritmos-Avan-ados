def process_list(nums):
    total_subtracoes = 0

    # Função para encontrar o menor número em uma coluna específica,
    # priorizando os elementos do meio quando houver repetidos
    def encontrar_menor_em_coluna(col):
        if not col:
            return None
        menores = [i for i, x in enumerate(col) if x > 0 and x == min([v for v in col if v > 0])]
        for i in menores:
            if i != 0 and i != len(col) - 1:
                return i
        return menores[0] if menores else None

    colunas = [nums]  # lista inicial de colunas

    while colunas:
        # 1. Encontrar o menor T entre todas as colunas
        menor_valor = float('inf')
        pos_col = None
        pos_idx = None

        for c_idx, col in enumerate(colunas):
            if not col:
                continue
            idx = encontrar_menor_em_coluna(col)
            if idx is not None and col[idx] < menor_valor:
                menor_valor = col[idx]
                pos_col = c_idx
                pos_idx = idx

        if pos_col is None:  # todas as colunas estão vazias ou sem valores positivos
            break

        # 2. Subtrair 1 do T
        total_subtracoes += 1
        colunas[pos_col][pos_idx] -= 1

        # 3. Subtrair índice+1 do próximo elemento à direita, se existir
        if pos_idx + 1 < len(colunas[pos_col]):
            colunas[pos_col][pos_idx + 1] -= (pos_idx + 1)
            if colunas[pos_col][pos_idx + 1] < 0:
                colunas[pos_col][pos_idx + 1] = 0

        # 4. Se T chegou a zero, dividir a coluna
        if colunas[pos_col][pos_idx] == 0:
            direita = colunas[pos_col][pos_idx + 1:] if pos_idx + 1 < len(colunas[pos_col]) else []
            colunas[pos_col] = colunas[pos_col][:pos_idx]
            if direita:
                colunas.insert(pos_col + 1, direita)

        # 5. Remover colunas vazias
        colunas = [col for col in colunas if col]

        # 6. Imprimir o estado atual das colunas
        print(' | '.join(str(col) for col in colunas))

    print("Total de subtrações:", total_subtracoes)


# Exemplo de uso
N = int(input("N: "))
nums = list(map(int, input("Lista: ").split()))
process_list(nums)
