import math

def haversine(lat1, long1, lat2, long2):
    R = 6371    # raio da Terra em km
    
    # Converter graus para radianos:
    phi1 = math.radians(lat1)   # 𝜙1
    phi2 = math.radians(lat1)   # 𝜙2
    delta_phi = math.radians(lat2-lat1)
    delta_lambda = math.radians(long2-long1)

    # Fórmula de Haversine:
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

nPlayers = int(input())

lat_correct, long_correct = map(float, input().split())
if abs(lat_correct) > 90 or abs(long_correct) > 180:
    print("Latitude ou Longitude inválidos.")

bestDist = float('inf')
rank = []

for _ in range(nPlayers):
    line = input().split()
    nickname = line[0]
    if len(nickname) > 20:
        print("Nickname muito longo! Máximo 20 caracteres.")

    lat = float(line[1])
    long = float(line[2])
    if abs(lat) > 90 or abs(long) > 180:
        print("Latitude ou Longitude inválidos.")

    dist = haversine(lat, long, lat_correct, long_correct)

    if dist < bestDist:
        bestDist = dist
        rank.insert(0, [nickname, bestDist])
    else:
        rank = [rank[0]] + sorted(rank[1:], key=lambda x: x[1])

    print(f"> [AVISO] MELHOR PALPITE: {bestDist: .3f}km")

print(f"\nRANKING")
print(f"-------")
for i, (nickname, dist) in enumerate(rank, start=1):
    print(f"{i}. {nickname:<20} : {dist: 8.3f}km {' [FANTASTICO]' if dist < 0.05 else ''}")
