#ifndef TYPES_H
#define TYPES_H

#include <string>

struct Coordenada{
    float x;
    float y;
    std::string name;
};

struct Aresta {
    std::string u;
    std::string v;
    float peso;
    
    bool operator<(const Aresta& other) const {
        return peso < other.peso;
    }
};

#endif