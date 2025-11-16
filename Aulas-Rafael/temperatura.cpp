#include <iostream>
#include <vector>
using namespace std;


string avaliarTemperatura(float ambiente, float desejada) {
    if (ambiente < desejada - 0.5)
        return "Aquecer";
    else if (ambiente > desejada + 0.5)
        return "Resfriar";
    else
        return "Manter temperatura atual";
}

float calcularMedia(const vector<float>& temps) {
    float soma = 0;
    for (float t : temps)
        soma += t;
    return soma / temps.size();
}

int main() {
    float ambiente, desejada;
    int opcao;

    vector<float> temperaturaDesejada; 

    do {
        cout << "\n*** Controle de Temperatura da Casa ***\n";
        cout << "1 - Ajustar temperatura de um comodo\n";
        cout << "0 - Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        if (opcao == 1) {
            cout << "\nTemperatura ambiente atual (°C): ";
            cin >> ambiente;

            cout << "Temperatura desejada para o comodo (°C): ";
            cin >> desejada;

            temperaturaDesejada.push_back(desejada);

            string action = avaliarTemperatura(ambiente, desejada);

            cout << "\n>>> Resultado: ";
            if (action == "Aquecer")
                cout << "Aquecedor LIGADO (Ambiente frio demais)\n";
            else if (action == "Resfriar")
                cout << "Ar-condicionado LIGADO (Ambiente quente demais)\n";
            else
                cout << "Temperatura ideal! Nenhuma acao necessaria.\n";
        }
        else if (opcao != 0) {
            cout << "Opcao invalida!\n";
        }

    } while (opcao != 0);

  
    if (!temperaturaDesejada.empty()) {
        float media = calcularMedia(temperaturaDesejada);
        cout << "\n*** Relatorio Final ***\n";
        cout << "Temperatura media desejada da casa: " << media << " °C\n";

        if (media < 20)
            cout << "Temperatura baixa.\n";
        else if (media > 26)
            cout << "Temperatura alta.\n";
        else
            cout << "Temperatura equilibrada.\n";
    }

    cout << "\nEncerrando o sistema...\n";

    return 0;
}