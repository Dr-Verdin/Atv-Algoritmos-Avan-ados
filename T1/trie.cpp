#include "trie.h"

// Inicializa a Trie
Trie::Trie(){
    root = new TrieNode();
}

// Libera memória da Trie 
Trie::~Trie(){
    deleteNode(root);
}

// Função auxiliar para liberar memória da Trie
void Trie::deleteNode(TrieNode *node){
    for(auto& pair : node->children) deleteNode(pair.second);
    delete node;
}

// Insere uma palavra nova na Trie letra por letra
void Trie::insert(const string& word){
    TrieNode *curr = root;
    for(char c : word){
        if(!curr->children.count(c)) curr->children[c] = new TrieNode();
        curr = curr->children[c];
    }
    curr->isEnd = true;
}

// Busca de palavra na Trie
bool Trie::isWord(const string& word){
    TrieNode *curr = root;
    for(char c : word){
        if(!curr->children.count(c)) return false;
        curr = curr->children[c];
    }
    return curr->isEnd;
}

// Busca um prefixo na Trie
bool Trie::isPrefix(const string& prefix){
    TrieNode *curr = root;
    for(char c : prefix){
        if(!curr->children.count(c)) return false;
        curr = curr->children[c];
    }
    return true;
}