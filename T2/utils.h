#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <cmath>
#include "types.h"

inline float distEuclidiana(const Coordenada& a, const Coordenada& b){
    float dx = b.x - a.x;
    float dy = b.y - a.y;
    return std::sqrt(dx*dx + dy*dy);
}

inline std::vector<Aresta> gerarArestas(const std::vector<Coordenada>& vertices, float maxTensao) {
    std::vector<Aresta> arestas;
    for (size_t i = 0; i < vertices.size(); i++) {
        for (size_t j = i + 1; j < vertices.size(); j++) {
            float tensao = distEuclidiana(vertices.at(i), vertices.at(j));
            if (tensao <= maxTensao) {
                arestas.push_back({vertices[i].name, vertices[j].name, tensao});
            }
        }
    }
    return arestas;
}

#endif 