#ifndef TYPES_H
#define TYPES_H

#include <string>

// Representa um sistema (ou ponto) com coordenadas e nome
struct Coordenada {
    float x;
    float y;
    std::string name;
    int index;
};

// Representa uma aresta entre dois sistemas
struct Aresta {
    std::string u;   // nome do primeiro sistema
    std::string v;   // nome do segundo sistema
    int idx_u;       // índice do primeiro sistema
    int idx_v;       // índice do segundo sistema
    float peso;      // distância (ou custo) da ligação

    // Define a ordem das arestas para comparação e ordenação
    bool operator<(const Aresta& other) const {
        if (peso != other.peso) {
            return peso < other.peso; // prioridade: menor peso primeiro
        } else {
            // desempate por índices (primeiro o menor índice entre os dois vértices)
            int min_this = std::min(idx_u, idx_v);
            int min_other = std::min(other.idx_u, other.idx_v);
            if (min_this != min_other) return min_this < min_other;

            // se ainda empatar, compara o maior índice
            int max_this = std::max(idx_u, idx_v);
            int max_other = std::max(other.idx_u, other.idx_v);
            if (max_this != max_other) return max_this < max_other;

            // último critério: ordem lexicográfica dos nomes (garante estabilidade)
            if (u != other.u) return u < other.u;
            return v < other.v;
        }
    }
};

#endif