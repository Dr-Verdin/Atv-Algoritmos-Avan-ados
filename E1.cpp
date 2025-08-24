#include <iostream>
#include <string>
#include <map>

using namespace std;

struct Node{
    int id;
    string diag;
    Node *left;
    Node *right;

    // Construtor
    Node(int i, string d) : id(i), diag(d), left(nullptr), right(nullptr) {}
};

int countHerDiabetes(Node *root){
    if(!root) return 0;
    int count = 0;

    if (root->diag == "sim" && (root->left || root->right) && (root->left->diag == "sim" || root->right->diag == "sim"))
        count++;

    count += countHerDiabetes(root->left);
    count += countHerDiabetes(root->right);

    return count;
}

int main(){
    int nCases;
    cin >> nCases;

    for(int i = 0; i < nCases; i++){
        // Montagem da árvore genealógica
        int nFamily;
        cin >> nFamily;

        map<int, Node*> nodes;
        for(int j = 0; j < nFamily; j++){
            int id, l, r;
            string diag;
            cin >> id >> diag >> l >> r;

            if(nodes.find(id) == nodes.end())
                nodes[id] = new Node(id, diag);
            else
                nodes[id]->diag = diag;

            if(l != -1){
                if(nodes.find(l) == nodes.end())
                    nodes[l] = new Node(l, "");
                nodes[id]->left = nodes[l];
            }
            if(r != -1){
                if(nodes.find(r) == nodes.end())
                    nodes[r] = new Node(r, "");
                nodes[id]->right = nodes[r];
            }
        }

        Node* root = nodes[1];

        //Contagem de pessoas cujo o pai/mãe tenha diabetes:
        int count = countHerDiabetes(root);
        cout << count << endl;
    }


    return 0;
}