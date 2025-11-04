#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <cmath>
#include "types.h"

// Calcula a distância euclidiana entre duas coordenadas
inline float distEuclidiana(const Coordenada& a, const Coordenada& b){
    float dx = b.x - a.x;
    float dy = b.y - a.y;
    return std::sqrt(dx*dx + dy*dy);
}

// Gera todas as arestas possíveis entre os vértices dentro do limite de tensão
inline std::vector<Aresta> gerarArestas(const std::vector<Coordenada>& vertices, float maxTensao) {
    std::vector<Aresta> arestas;
    for (size_t i = 0; i < vertices.size(); i++) {
        for (size_t j = i + 1; j < vertices.size(); j++) {
            float tensao = distEuclidiana(vertices.at(i), vertices.at(j));
            // adiciona aresta apenas se estiver dentro do limite
            if (tensao <= maxTensao) {
                Aresta a;
                a.u = vertices[i].name;
                a.v = vertices[j].name;
                a.peso = tensao;
                a.idx_u = vertices[i].index;
                a.idx_v = vertices[j].index;
                arestas.push_back(a);
            }
        }
    }
    return arestas;
}

// Ordena as arestas por peso e, em caso de empate, pelos índices dos vértices
void ordenarArestas(std::vector<Aresta>& a){
    std::sort(a.begin(), a.end(), [](const Aresta& e1, const Aresta& e2) {
        if (e1.peso != e2.peso)
            return e1.peso < e2.peso;

        // desempate: primeiro pelo menor índice
        int min1 = std::min(e1.idx_u, e1.idx_v);
        int min2 = std::min(e2.idx_u, e2.idx_v);
        if (min1 != min2)
            return min1 < min2;

        // se ainda empatar, pelo maior índice
        int max1 = std::max(e1.idx_u, e1.idx_v);
        int max2 = std::max(e2.idx_u, e2.idx_v);
        return max1 < max2;
    });
}

#endif