from datetime import datetime 

# Número de casos testes
n_testes = int(input())

for _ in range(n_testes):
    n_datas = int(input())

    dados = []
    for _ in range(n_datas):
        # armazenar as datas com os valores 
        line = input().split()
        data = line[0]
        lucro = float(line[1])
        dados.append([data, lucro])
    
    # Guloso: pegar os dias com maiores valores
    # pegar o maior valor e somar o resto e comparar, se for menor pega o segundo maior soma pega o resto soma e compara, etc
    dados_ordenados = sorted(dados, key=lambda x: x[1], reverse=True)
    soma_resto = sum(x[1] for x in dados)
    soma_maiores = 0
    datas_soma_maiores = []
    for i, (data, lucro) in enumerate(dados_ordenados, start=1):
        soma_maiores += lucro
        soma_resto -= lucro
        datas_soma_maiores.append(data)
        if soma_maiores > soma_resto:
            break
    
    # Saída
    print(f"{len(datas_soma_maiores)} dias ({', '.join(sorted(datas_soma_maiores, key=lambda x: datetime.strptime(x, "%d/%m/%Y")))}) | soma={soma_maiores:.2f} | {(len(datas_soma_maiores)*100)/len(dados):.2f}% dos dias totais")