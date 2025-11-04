#ifndef KRUSKAL_H
#define KRUSKAL_H

#include <vector>
#include <string>
#include <map>
#include <algorithm>

#include "types.h"

// Estrutura Union-Find (Disjoint Set Union) usada pelo algoritmo de Kruskal
class UnionFind {
private:
    std::map<std::string, std::string> parent; // armazena o "pai" de cada vértice
public:
    // Inicializa cada vértice como seu próprio conjunto
    void makeSet(const std::vector<Coordenada>& elementos) {
        for (const auto& e : elementos)
            parent[e.name] = e.name;
    }

    // Retorna o representante do conjunto (com compressão de caminho)
    std::string find(const std::string& x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    // Une os conjuntos de dois vértices; retorna false se já estavam unidos
    bool unite(const std::string& a, const std::string& b) {
        std::string pa = find(a);
        std::string pb = find(b);
        if (pa == pb) return false;  // já pertencem ao mesmo conjunto
        parent[pb] = pa;             // une pb ao conjunto de pa
        return true;
    }
};

// Algoritmo de Kruskal: gera a Árvore Geradora Mínima (MST)
inline std::vector<Aresta> kruskal(const std::vector<Coordenada>& vertices, const std::vector<Aresta>& arestas) {
    std::vector<Aresta> mst; // armazena as arestas da MST

    UnionFind uf;
    uf.makeSet(vertices);    // cada vértice começa em seu próprio conjunto

    std::vector<Aresta> sorted = arestas;
    std::sort(sorted.begin(), sorted.end());  // ordena as arestas por peso

    // adiciona arestas que conectam conjuntos diferentes
    for (const auto& a : sorted) {
        if (uf.unite(a.u, a.v)) {
            mst.push_back(a);
        }
    }

    return mst;
}

#endif