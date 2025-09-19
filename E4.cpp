#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

// Função DFS para ordenação topológica
void dfs(int idx, const vector<vector<int>>& adj, vector<bool>& visitado, stack<int>& s) {
    visitado[idx] = true;
    for (int idxNew = 0; idxNew < adj[idx].size(); ++idxNew) {
        if (adj[idx][idxNew] && !visitado[idxNew]) {
            dfs(idxNew, adj, visitado, s);
        }
    }
    s.push(idx);
}

vector<int> ordTopologica(const vector<vector<int>>& adj){
    int n = adj.size();
    vector<bool> visitado(n, false);
    stack<int> s;

    for (int i = 0; i < n; ++i) {
        if (!visitado[i]) dfs(i, adj, visitado, s);
    }

    vector<int> ordem;
    while (!s.empty()) {
        ordem.push_back(s.top());
        s.pop();
    }
    return ordem;
}

int main(){
    int nTestes;
    cin >> nTestes;

    // Tabela de produtividade dos heróis
    map<string, double> niveisProd = {{"Lenda", 2.0}, {"Mestre", 1.5}, {"Cavaleiro", 1.2}, {"Aventureiro", 1.0}, {"Aprendiz", 0.75}};

    for(int i = 0; i < nTestes; i++){
        int nHerois, nQuests;
        cin >> nHerois >> nQuests;

        // Leitura dos heróis:
        vector<pair<string, string>> listaHerois;   // (nome, nivel)
        for(int j = 0; j < nHerois; j++){
            string heroi, nivel;
            cin >> heroi >> nivel;

            listaHerois.push_back({heroi, nivel});
        }

        cin.ignore();   // limpar buffer antes de getline

        // Leitura das Quests e dependências
        vector<pair<int, int>> listaQuests;                                 // (id, tempoExec)
        vector<vector<int>> matrizDpQuests(nQuests, vector<int>(nQuests, 0));
        for(int j = 0; j < nQuests; j++){
            string linhaQuest;
            getline(cin, linhaQuest);
            istringstream ss(linhaQuest);

            int id, tempoExec, dp;
            ss >> id >> tempoExec;
            listaQuests.push_back({id, tempoExec});

            while(ss >> dp){
                // marca 1 na matriz de dependencias
                if(dp != 0){
                    matrizDpQuests[id-1][dp-1] = 1;
                }
            }
        }

        // Ordenação Topológica das quests
        vector<int> ordemQuests = ordTopologica(matrizDpQuests);

        // Inicializa o tempo livre de cada heroi
        vector<double> tempoLivreHeroi(nHerois, 0);
        vector<double> tempoConcluidoQuest(nQuests, 0);
        vector<vector<int>> questsPorHeroi(nHerois); // quais quests cada herói fez

        // Algoritmo guloso
        for(int q : ordemQuests){
            int tempoBase = listaQuests[q].second;

            // calcular tempo mínimo devido às dependências
            double tempoMinimoParaQuest = 0;
            for(int i = 0; i < nQuests; i++){
                if(matrizDpQuests[i][q]) // i antes de q
                    tempoMinimoParaQuest = max(tempoMinimoParaQuest, tempoConcluidoQuest[i]);
            }

            double menorFim = 1e9;
            int heroiEscolhido = -1;

            for(int h = 0; h < nHerois; h++){
                double tempoInicio = max(tempoLivreHeroi[h], tempoMinimoParaQuest);
                double tempoFim = tempoInicio + tempoBase / niveisProd[listaHerois[h].second];
                if(tempoFim < menorFim){
                    menorFim = tempoFim;
                    heroiEscolhido = h;
                }
            }

            // Atualiza
            tempoLivreHeroi[heroiEscolhido] = menorFim;
            tempoConcluidoQuest[q] = menorFim;
            questsPorHeroi[heroiEscolhido].push_back(q+1); // armazenar ID da quest
        }

        // Saída
        cout << fixed << setprecision(2);
        for(int h = 0; h < nHerois; h++){
            sort(questsPorHeroi[h].begin(), questsPorHeroi[h].end());
            cout << listaHerois[h].first << " = {";
            for(size_t k = 0; k < questsPorHeroi[h].size(); k++){
                cout << questsPorHeroi[h][k];
                if(k+1 < questsPorHeroi[h].size()) cout << ",";
            }
            cout << "}\n";
        }

        double tempoTotal = *max_element(tempoLivreHeroi.begin(), tempoLivreHeroi.end());
        cout << "Tempo mínimo: " << tempoTotal << endl;

    }

    return 0;    
}