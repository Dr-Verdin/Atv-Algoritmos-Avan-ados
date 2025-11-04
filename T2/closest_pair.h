#ifndef CLOSEST_PAIR_H
#define CLOSEST_PAIR_H

#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <climits>

#include "types.h"
#include "utils.h"

// Força bruta: compara todos os pares (usado para n pequeno)
inline Aresta bruteForce(const std::vector<Coordenada>& p){
    Aresta menor;
    menor.peso = std::numeric_limits<float>::infinity();
    menor.u = "";
    menor.v = "";
    menor.idx_u = INT_MAX;
    menor.idx_v = INT_MAX;

    size_t n = p.size();
    if(n < 2) return menor;

    for(size_t i = 0; i < n - 1; ++i){
        for(size_t j = i + 1; j < n; ++j){
            float d = distEuclidiana(p[i], p[j]);
            int iu = p[i].index;
            int iv = p[j].index;

            // critério de "melhor": primeiro menor distância, depois desempates por índices
            bool better = false;
            if(d < menor.peso){
                better = true;
            } else if(d == menor.peso){
                int min_new = std::min(iu, iv);
                int min_old = std::min(menor.idx_u, menor.idx_v);
                if(min_new < min_old) better = true;
                else if(min_new == min_old){
                    int max_new = std::max(iu, iv);
                    int max_old = std::max(menor.idx_u, menor.idx_v);
                    if(max_new < max_old) better = true;
                }
            }

            if(better){
                menor.peso = d;
                menor.u = p[i].name;
                menor.v = p[j].name;
                menor.idx_u = iu;
                menor.idx_v = iv;
            }
        }
    }
    return menor;
}

// Função recursiva do algoritmo de divisão e conquista
inline Aresta closestPairRec(const std::vector<Coordenada>& pX, const std::vector<Coordenada>& pY){
    // caso base: usa força bruta quando pequeno
    if(pX.size() <= 3) return bruteForce(pX);
    
    int meio = pX.size() / 2;
    std::vector<Coordenada> qX(pX.begin(), pX.begin() + meio);      // metade esquerda ordenada por x
    std::vector<Coordenada> rX(pX.begin() + meio, pX.end());        // metade direita ordenada por x
    float xMeio = qX.back().x;  // linha vertical de separação

    // Construir pY dividido em qY e rY, mantendo ordenação por y
    std::vector<Coordenada> qY, rY;
    for(const auto& p : pY){
        if(p.x <= xMeio) qY.push_back(p);
        else rY.push_back(p);
    }

    // recursão nas duas metades
    Aresta esq = closestPairRec(qX, qY);
    Aresta dir = closestPairRec(rX, rY);

    // escolher a melhor aresta entre esq e dir (considera desempates por índices)
    Aresta menor = (esq.peso < dir.peso) ? esq : dir; 
    menor = esq;
    if(dir.peso < esq.peso){
        menor = dir;
    } else if(dir.peso == esq.peso){
        int min_esq = std::min(esq.idx_u, esq.idx_v);
        int min_dir = std::min(dir.idx_u, dir.idx_v);
        if(min_dir < min_esq) menor = dir;
        else if(min_dir == min_esq){
            int max_esq = std::max(esq.idx_u, esq.idx_v);
            int max_dir = std::max(dir.idx_u, dir.idx_v);
            if(max_dir < max_esq) menor = dir;
        }
    }

    float distMin = menor.peso; // distância mínima atual

    // Construir "strip": pontos cuja abscissa está a menos de distMin da linha média
    std::vector<Coordenada> strip;
    strip.reserve(pY.size());
    for(const auto &pt : pY){
        if(fabsf(pt.x - xMeio) < distMin) strip.push_back(pt);
    }

    // Verifica pares no strip — propriedade do algoritmo garante checar só alguns próximos por y
    for(size_t i = 0; i < strip.size(); ++i){
        for(size_t j = i + 1; j < strip.size(); ++j){
            // poda: se a diferença em y já ≥ distMin, não precisa verificar mais neste i
            if((strip[j].y - strip[i].y) >= distMin) break;
            float dij = distEuclidiana(strip[i], strip[j]);
            int iu = strip[i].index;
            int iv = strip[j].index;

            // mesmo critério de desempate usado antes
            bool better = false;
            if(dij < distMin){
                better = true;
            } else if(dij == distMin){
                int min_new = std::min(iu, iv);
                int min_old = std::min(menor.idx_u, menor.idx_v);
                if(min_new < min_old) better = true;
                else if(min_new == min_old){
                    int max_new = std::max(iu, iv);
                    int max_old = std::max(menor.idx_u, menor.idx_v);
                    if(max_new < max_old) better = true;
                }
            }

            if(better){
                distMin = dij;
                menor.peso = dij;
                menor.u = strip[i].name;
                menor.v = strip[j].name;
                menor.idx_u = iu;
                menor.idx_v = iv;
            }
        }
    }
    return menor;
}

// Função wrapper: prepara vetores ordenados por x e por y e chama a recursiva
inline Aresta closestPair(const std::vector<Coordenada>& pontos){
    std::vector<Coordenada> pX = pontos;
    std::sort(pX.begin(), pX.end(), [](const Coordenada &a, const Coordenada &b){
        return a.x < b.x;
    });

    std::vector<Coordenada> pY = pontos;
    std::sort(pY.begin(), pY.end(), [](const Coordenada &a, const Coordenada &b){
        return a.y < b.y;
    });

    return closestPairRec(pX, pY);
}

#endif
