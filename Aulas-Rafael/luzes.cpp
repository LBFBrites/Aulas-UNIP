#include <iostream>
#include <string>
using namespace std;

void ligarLuz(bool luzes[], int indice);
void desligarLuz(bool luzes[], int indice);
void mostrarEstado(const bool luzes[], const string comodos[]);
void apagaTodas(bool luzes[]);

int main() {

    string comodos[4] = {"Sala", "Cozinha", "Quarto", "Banheiro"};

    bool luzes[4] = {false, false, false, false};

    int opcao;

    do {
        cout << "\n=== Controle de Iluminacao ===\n";
        cout << "1 - Sala\n";
        cout << "2 - Cozinha\n";
        cout << "3 - Quarto\n";
        cout << "4 - Banheiro\n";
        cout << "5 - Mostrar estado das luzes\n";
        cout << "0 - Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 && opcao <= 4) {
            int indice = opcao - 1;
            int acao;

            cout << "\n--- " << comodos[indice] << " ---\n";
            cout << "1 - Ligar luz\n";
            cout << "2 - Desligar luz\n";
            cout << "Escolha: ";
            cin >> acao;

            if (acao == 1)
                ligarLuz(luzes, indice);
            else if (acao == 2)
                desligarLuz(luzes, indice);
            else
                cout << "Acao invalida!\n";
        }
        else if (opcao == 5) {
            mostrarEstado(luzes, comodos);
        }
        else if (opcao != 0) {
            cout << "Opcao invalida!\n";
        }

    } while (opcao != 0);

 
    apagaTodas(luzes);

    cout << "\n=== Estado final das luzes ===\n";
    mostrarEstado(luzes, comodos);

    cout << "\nTodas as luzes foram apagadas. Encerrando...\n";

    return 0;
}


void ligarLuz(bool luzes[], int indice) {
    luzes[indice] = true;
    cout << "Ligar \n";
}

void desligarLuz(bool luzes[], int indice) {
    luzes[indice] = false;
    cout << "Desligar \n";
}

void mostrarEstado(const bool luzes[], const string comodos[]) {
    for (int i = 0; i < 4; i++) {
        cout << comodos[i] << ": " 
             << (luzes[i] ? "Ligada" : "Desligada") << endl;
    }
}

void apagaTodas(bool luzes[]) {
    for (int i = 0; i < 4; i++) {
        luzes[i] = false;
    }
}