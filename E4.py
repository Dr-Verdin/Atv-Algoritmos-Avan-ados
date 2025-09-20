from collections import defaultdict, deque

# Produtividade dos heróis
produtividade = {
    "Aprendiz": 0.75,
    "Aventureiro": 1.0,
    "Cavaleiro": 1.2,
    "Mestre": 1.5,
    "Lenda": 2.0
}

nTestes = int(input().strip())
for i in range(nTestes):
    nHerois, nQuests = map(int, input().split())
    
    # Ler heróis
    herois = []
    for _ in range(nHerois):
        nome, nivel = input().split()
        herois.append({
            "nome": nome,
            "nivel": nivel,
            "prod": produtividade[nivel],
            "tempo_livre": 0.0,
            "quests": []
        })
    
    # Ler quests
    tempo_base = {}
    dependencias_q = defaultdict(list)
    indegree = [0] * (nQuests+1)
    
    for _ in range(nQuests):
        linha = list(map(int, input().split()))
        id, tempo, *deps = linha
        tempo_base[id] = tempo
        if deps[0] != 0:  # se há dependências
            dependencias_q[id] = deps
            for d in deps:
                indegree[id] += 1
        else:
            dependencias_q[id] = []
    
    # Ordenação topológica (Kahn)
    fila = deque([i for i in range(1, nQuests+1) if indegree[i] == 0])
    ordem = []
    while fila:
        atual = fila.popleft()
        ordem.append(atual)
        for q, deps in dependencias_q.items():
            if atual in deps:
                indegree[q] -= 1
                if indegree[q] == 0:
                    fila.append(q)
    
    # Simulação
    fim_quest = {}
    for q in ordem:
        melhor_fim = float("inf")
        escolhido = None
        for h in herois:
            inicio = max(h["tempo_livre"], max((fim_quest[d] for d in dependencias_q[q]), default=0))
            duracao = tempo_base[q] / h["prod"]
            fim = inicio + duracao
            if fim < melhor_fim:
                melhor_fim = fim
                escolhido = h
        # Atribui quest ao herói
        escolhido["tempo_livre"] = melhor_fim
        escolhido["quests"].append(q)
        fim_quest[q] = melhor_fim
    
    # Saída
    for h in herois:
        quests_str = ",".join(map(str, h["quests"]))
        print(f"{h['nome']} = {{{quests_str}}}")
    print(f"Tempo mínimo: {max(fim_quest.values()):.2f}")
    if i != nTestes-1:
        print()