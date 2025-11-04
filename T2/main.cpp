#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

#include "types.h"
#include "utils.h"
#include "kruskal.h"
#include "closest_pair.h"

using namespace std;

int main(){
    int nCasos;
    cin >> nCasos; // lê o número de casos de teste

    for(int n = 0; n < nCasos; n++){
        int nSistemas, nSistemasImportantes;
        float maxTensao;
        cin >> nSistemas >> nSistemasImportantes >> maxTensao;

        vector<Coordenada> sistemas;
        vector<Coordenada> importantes;

        // lê os sistemas e separa os importantes
        for(int i = 0; i < nSistemas; i++){
            string nome;
            float x, y;
            cin >> nome >> x >> y;

            sistemas.push_back({x, y, nome, i});
            if(i < nSistemasImportantes) importantes.push_back({x, y, nome, i});
        }

        // --- 1. Malha de Túneis Essencial (Kruskal) ---
        vector<Aresta> arestasImportantes = gerarArestas(importantes, maxTensao); // gera arestas entre sistemas importantes
        vector<Aresta> malha = kruskal(importantes, arestasImportantes);          // aplica o algoritmo de Kruskal
        ordenarArestas(malha);                                                    // ordena as arestas para exibição

        // imprime a malha final
        for(const auto& a : malha){
            // garante que o menor índice venha primeiro na saída
            if(a.idx_v < a.idx_u){
                cout << a.v << ", " << a.u << ", " << fixed << setprecision(2) << a.peso << endl;
            } else {
                cout << a.u << ", " << a.v << ", " << fixed << setprecision(2) << a.peso << endl;
            }
        }

        // --- 2. Ponto de Ressonância Gravitacional (Divisão e Conquista) ---
        Aresta zonaAlerta = closestPair(sistemas); // encontra o par de sistemas mais próximos

        // garante a ordem correta dos nomes ao exibir
        if(zonaAlerta.idx_v < zonaAlerta.idx_u){
            swap(zonaAlerta.u, zonaAlerta.v);
            swap(zonaAlerta.idx_u, zonaAlerta.idx_v);
        }

        cout << "Ponto de Ressonância: " 
             << zonaAlerta.u << ", " << zonaAlerta.v << ", " 
             << fixed << setprecision(2) << zonaAlerta.peso << endl;
        cout << endl;
    }

    return 0;
}