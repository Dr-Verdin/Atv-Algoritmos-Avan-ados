#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <unordered_map>

#include "types.h"
#include "utils.h"
#include "kruskal.h"
#include "closest_pair.h"

using namespace std;

int main(){
    int nCasos;
    cin >> nCasos;

    for(int n = 0; n < nCasos; n++){
        int nSistemas, nSistemasImportantes;
        float maxTensao;
        cin >> nSistemas >> nSistemasImportantes >> maxTensao;

        vector<Coordenada> sistemas;
        vector<Coordenada> importantes;
        unordered_map<std::string, size_t> nameToIndex;

        for(int i = 0; i < nSistemas; i++){
            string nome;
            float x, y;
            cin >> nome >> x >> y;
            sistemas.push_back({x, y, nome});
            nameToIndex[nome] = sistemas.size() - 1;
            if(i < nSistemasImportantes) importantes.push_back({x, y, nome});
        }

        // 1. A Malha de Túneis Essencial (Algoritmo Guloso)
        vector<Aresta> arestasImportantes = gerarArestas(importantes, maxTensao);
        vector<Aresta> malha = kruskal(importantes, arestasImportantes);

        for(const auto& a : malha){
            cout << a.u << ", " << a.v << ", " << fixed << setprecision(2) << a.peso << endl;
        }

        // 2. O Ponto de Ressonância Gravitacional (Algoritmo de Divisão e Conquista)
        Aresta zonaAlerta = closestPair(sistemas);

        auto itU = nameToIndex.find(zonaAlerta.u);
        auto itV = nameToIndex.find(zonaAlerta.v);

        std::string primeiro = zonaAlerta.u;
        std::string segundo  = zonaAlerta.v;

        // Se ambos encontrados, ordena por índice
        if (itU != nameToIndex.end() && itV != nameToIndex.end()) {
            if (itV->second < itU->second) {
                zonaAlerta.v = primeiro;
                zonaAlerta.u = segundo;
            }
        }   

        cout << "Ponto de Ressonância: " << zonaAlerta.u << ", " << zonaAlerta.v << ", " << fixed << setprecision(2) << zonaAlerta.peso << endl;
        cout << endl;
    }

    return 0;
}