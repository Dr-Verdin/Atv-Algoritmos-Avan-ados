#ifndef KRUSKAL_H
#define KRUSKAL_H

#include <vector>
#include <string>
#include <map>
#include <algorithm>

#include "types.h"

class UnionFind{
private:
    std::map<std::string, std::string> parent;     // cada vértice (sistema) terá um "pai" na estrutura de conjuntos
public:
    void makeSet(const std::vector<Coordenada>& elementos){
        for(const auto& e : elementos) parent[e.name] = e.name;
    }

    // Encontra o representante do conjunto do vértice x
    std::string find(const std::string& x){
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    // Une os conjuntos de x e y
    bool unite(const std::string& a, const std::string& b){
        std::string pa = find(a);
        std::string pb = find(b);
        if(pa == pb) return false;
        parent[pb] = pa;    // une os conjuntos de u e v
        return true;
    }
};

inline std::vector<Aresta> kruskal(const std::vector<Coordenada>& vertices, const std::vector<Aresta>& arestas){
    std::vector<Aresta> mst; // Para armazenar as arestas da MST

    UnionFind uf;
    uf.makeSet(vertices);   // parent[vertice] = vertice

    std::vector<Aresta> sorted = arestas;
    std::sort(sorted.begin(), sorted.end());   // ordenar as arestas pelo peso crescente

    for(const auto& a : sorted){
        if(uf.unite(a.u, a.v)){     // u e v não estão no mesmo conjunto
            mst.push_back(a);
        }
    }
    return mst;
}

#endif