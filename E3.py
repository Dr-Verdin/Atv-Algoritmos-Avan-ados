from collections import defaultdict

# Transformar a string de horas em minutos
def h_para_min(h_str):
    h, min = map(int, h_str.split(":"))
    return (h * 60) + min

# Número de casos testes
n_testes = int(input())

for _ in range(n_testes):
    n_modelos = int(input())
    n_alugueis = int(input())

    dados = []
    for __ in range(n_alugueis):
        line = input()
        line = line.split()
        id = int(line[0])
        h_inicio = h_para_min(line[1])
        h_fim = h_para_min(line[2])
        modelo = int(line[3])
        dados.append([id, h_inicio, h_fim, modelo])

    # Agrupar os alugueis por modelo
    dados_modelo = {modelo+1:[] for modelo in range(n_modelos)}
    for d in dados:
        dados_modelo[d[3]].append(d)

    saidas = [] # para impressão

    # Para cada modelo
    for modelo in sorted(dados_modelo.keys()):
        alugueis = dados_modelo[modelo]
        alugueis.sort(key=lambda x: (x[2], x[1]))   # ordenar por fim ed eposi por inicio

        fim_ultimo_aluguel = -1 # fim do ultimo aluguel escolhido
        escolhidos = []     # alugueis escolhidos
        for a in alugueis:
            if a[1] >= fim_ultimo_aluguel:
                escolhidos.append(a[0])
                fim_ultimo_aluguel = a[2]
        if len(escolhidos)>0:
            txt_out = f"{modelo}: {len(escolhidos)} = {', '.join(map(str, escolhidos))}"
        else:
            txt_out = f"{modelo}: 0"
        saidas.append(txt_out)   # saída de cada modelo
    
    print(" | ".join(saidas))   # saida completa do teste