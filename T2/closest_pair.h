#ifndef CLOSEST_PAIR_H
#define CLOSEST_PAIR_H

#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

#include "types.h"
#include "utils.h"


inline Aresta bruteForce(const std::vector<Coordenada>& p){
    Aresta menor;
    menor.peso = std::numeric_limits<float>::infinity();
    menor.u = "";
    menor.v = "";

    size_t n = p.size();
    if(n < 2) return menor;

    for(size_t i = 0; i < n - 1; ++i){
        for(size_t j = i + 1; j < n; ++j){
            float d = distEuclidiana(p[i], p[j]);
            if(d < menor.peso){
                menor.peso = d;
                menor.u = p[i].name;
                menor.v = p[j].name;
            }
        }
    }
    return menor;
}

inline Aresta closestPairRec(const std::vector<Coordenada>& pX, const std::vector<Coordenada>& pY){
    if(pX.size() <= 3) return bruteForce(pX);
    
    int meio = pX.size() / 2;
    std::vector<Coordenada> qX(pX.begin(), pX.begin() + meio);
    std::vector<Coordenada> rX(pX.begin() + meio, pX.end());
    float xMeio = qX.back().x;  // linha vertical de separação (ultimo elemento do vetor qX)

    // Construir py dividido em Qy e Ry (manter ordenação por y)
    std::vector<Coordenada> qY, rY;
    for(const auto& p : pY){
        if(p.x <= xMeio) qY.push_back(p);
        else rY.push_back(p);
    }

    // Recursão nas duas metades
    Aresta esq = closestPairRec(qX, qY);
    Aresta dir = closestPairRec(rX, rY);

    // Escolher a menor entre as duas metades
    Aresta menor = (esq.peso <= dir.peso) ? esq : dir; 
    float distMin = menor.peso; // distância atual mínima

    // Construir strip: pontos dentro de distância d da linha xMeio
    std::vector<Coordenada> strip;
    strip.reserve(pY.size());
    for(const auto &pt : pY){
        if(fabsf(pt.x - xMeio) < distMin) strip.push_back(pt);
    }

    for(size_t i = 0; i < strip.size(); ++i){
        for(size_t j = i + 1; j < strip.size(); ++j){
            if((strip[j].y - strip[i].y) >= distMin) break;
            float dij = distEuclidiana(strip[i], strip[j]);
            if(dij < distMin){
                distMin = dij;
                menor.peso = dij;
                menor.u = strip[i].name;
                menor.v = strip[j].name;
            }
        }
    }
    return menor;
}

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