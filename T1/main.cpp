#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

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
vector<string> readWords(int n) {
    vector<string> words;
    words.reserve(n);

    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        words.push_back(word);
    }
    return words;
}

int main() {
    int lines = readInt(1, 50);
    int columns = readInt(1, 50);
    vector<vector<char>> wordSearch = readWordSearch(lines, columns);

    int nWords = readInt(1, 50000);
    vector<string> words = readWords(nWords);



    return 0;
}