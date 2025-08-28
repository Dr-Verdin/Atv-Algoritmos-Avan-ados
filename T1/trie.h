#ifndef TRIE_H
#define TRIE_H

#include <unordered_map>
#include <string>

using namespace std;

// Classe Nó da Trie
class TrieNode{
public:
    bool isEnd;                                 // indica se o nó for o fim da palavra
    unordered_map<char, TrieNode*> children;    // mapeia um caracter char para o próximo nó

    TrieNode() : isEnd(false) {}
};

// Classe Trie
class Trie {
private:
    TrieNode *root;                     // raiz da Trie
    void deleteNode(TrieNode* node);    // liberar memória

public:
    Trie();                                 // inicializa a Trie
    ~Trie();                                // libera memória

    void insert(const string& word);        // insere uma palavra letra por letra 
    bool isWord(const string& word);        // retorna true se a palavra existe inteira
    bool isPrefix(const string& prefix);  // retorna true se um prefixo existe
};

#endif    