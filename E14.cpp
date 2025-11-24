#include <iostream>
#include <string>
#include <limits>
#include <vector>

using namespace std;

string kmp(const string &s, bool proper = true) {
    int n = s.size();

    if (n == 0) return "";

    vector<int> pi(n, 0);           // o tamanho do maior prefixo que é também sufixo da string inteira
    for (int i = 1; i < n; ++i) {
        int j = pi[i-1];
        while (j > 0 && s[i] != s[j]) j = pi[j-1];

        if (s[i] == s[j]) ++j;

        pi[i] = j;
    }

    int k = pi[n-1];    // pega o maior prefixo-sufixo da string

    if (proper && k == n) k = (k > 0 ? pi[k-1] : 0);
    
    return s.substr(0, k);
}

int main(){
    int nCasos;
    cin >> nCasos;

    for(int i = 0; i < nCasos; i++){
        string polimero;
        cin >> polimero;

        cout << kmp(polimero) << "\n";
    }
}


    