#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include "trie.h"
using namespace std;

int dx[8] = {-1, -1, -1, 0,  0,  1, 1, 1};
int dy[8] = {-1, 0, 1, -1,  1, -1,  0, 1};

// Função para busca das palavras no caça palavras
void searchWordSearch(vector<vector<char>> wordSearch, int i, int j, Trie &trie, set<string> &found){
    // passo 2: checar se com a letra atual ela faz alguma das palavras partindo para alguma das 8 direções
    for(int dir = 0; dir < 8; dir++){
        int x = i;
        int y = j;
        string current = "";

        while(x >= 0 && x < wordSearch.size() && y >= 0 && y < wordSearch[0].size()){
            current += wordSearch[x][y];

            if(!trie.isPrefix(current)) break; // não tem palavra nessa direção

            if(trie.isWord(current)){
                found.insert(current);  // adiciona em palavras encontradas
            }

            x += dx[dir];
            y += dy[dir];
        }
    }
}

// Função para ler e validar um número inteiro em um intervalo
int readInt(int min, int max) {
    int valor;
    while (true) {
        cin >> valor;
        if (valor >= min && valor <= max) {
            return valor;
        }
        cout << "Valor inválido! Digite novamente." << endl;
    }
}

// Função para ler a grade de letras maiúsculas
vector<vector<char>> readWordSearch(int lines, int columns) {
    vector<vector<char>> wordSearch(lines, vector<char>(columns));

    for (int i = 0; i < lines; i++) {
        string line;
        while (true) {
            cin >> line;
            bool isValid = true;

            if ((int)line.size() != columns) {
                isValid = false;
            } else {
                for (char c : line) {
                    if (!isupper(c)) {
                        isValid = false;
                        break;
                    }
                }
            }

            if (!isValid) {
                cout << "Erro! A linha deve ter exatamente " 
                     << columns << " letras maiúsculas." << endl;
            } else {
                for (int j = 0; j < columns; j++) {
                    wordSearch[i][j] = line[j];
                }
                break;
            }
        }
    }
    return wordSearch;
}

// Função para ler a lista de palavras
void readWords(int n, Trie& trie) {
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        for (char &c : word) c = toupper(c);
        trie.insert(word);
    }
}

int main() {
    // Ler entrada
    int lines = readInt(1, 50);
    int columns = readInt(1, 50);
    vector<vector<char>> wordSearch = readWordSearch(lines, columns);

    int nWords = readInt(1, 50000);
    Trie trie;
    readWords(nWords, trie);

    set<string> found;  // para armazenar as palavras encontradas

    // Percorrer o caça palavra em busca das palvras
    for(int i = 0; i < lines; i++){ 
        for(int j = 0; j < columns; j++){
            searchWordSearch(wordSearch, i, j, trie, found);
        }
    }

    // Imprimir saída
    cout << (int)found.size() << endl;
    for (auto& w : found) {
        cout << w << endl;
    }

    return 0;
}