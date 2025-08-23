import math
import sys
input = sys.stdin.readline

def haversine(lat1, long1, lat2, long2):
    R = 6371    # raio da Terra em km
    
    # Converter graus para radianos:
    phi1 = math.radians(lat1)   # 𝜙1
    phi2 = math.radians(lat2)   # 𝜙2
    delta_phi = math.radians(lat2-lat1)
    delta_lambda = math.radians(long2-long1)

    # Fórmula de Haversine:
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

# Número de jogadores
nPlayers = int(input())

# Coordenada correta
lat_correct, long_correct = map(float, input().split())

bestDist = float('inf')
players = []

# Jogadores
for _ in range(nPlayers):
    line = input().split()
    nickname = line[0]
    lat, long = map(float, line[1:])
    dist = haversine(lat, long, lat_correct, long_correct)
    players.append([nickname, dist])
    
    if dist < bestDist:
        bestDist = dist
    print(f"> [AVISO] MELHOR PALPITE: {bestDist:.3f}km")

rank = sorted(players, key=lambda x: x[1])

# Impressão do Ranking
print(f"\nRANKING")
print(f"-------")
for i, (nickname, dist) in enumerate(rank, start=1):
    status = ' [FANTASTICO]' if dist < 0.05 else ''
    print(f"{i:2}. {nickname:<21}:{dist:7.3f} km{status}")