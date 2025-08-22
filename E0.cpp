/* seu programa deve permitir o cadastro de produtos, associando a cada
um deles um código e o respectivo preço por quilograma */

#include <iostream>
#include <string>
#include <iomanip>
#include <map>

using namespace std;

int main(){
    //  Cadastrar novos produtos:
    int nCadastros;
    cin >> nCadastros;

    map<string, float> inventario;

    for(int i = 0; i < nCadastros; i++){
        string codigo;
        float precoKg;

        cin >> codigo >> precoKg;

        auto item = inventario.find(codigo);

        if(item != inventario.end()){
            cout << "Produto com código " << codigo << " já cadastrado." << endl;
        } else {
            inventario[codigo] = precoKg;
        }
    }

    // Registro das compras:
    while(true){
        int nItens;
        cin >> nItens;

        if(nItens == -1){
            break;
        }

        float totalCompra = 0.00;

        for(int i = 0; i < nItens; i++){
            string codigo;
            float peso;

            cin >> codigo >> peso;

            auto item = inventario.find(codigo);

            if(item != inventario.end()){
                float precoKg = item->second;
                totalCompra += peso*precoKg;
            } else {
                cout << "Produto com código " << codigo << " não cadastrado." << endl;
            }
        }

        cout << fixed << setprecision(2) << "R$" << totalCompra << endl;
    }

    return 0;
}