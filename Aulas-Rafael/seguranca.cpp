#include <iostream>
#include <vector>
#include <string>
using namespace std;

void armarSistema(bool &armado, vector<string> &log);
void desarmarSistema(bool &armado, vector<string> &log);
void verificarSensores(bool porta, bool janela, bool movimento);
void acionarAlarme(bool porta, bool janela, bool movimento, bool armado, vector<string> &log);
void registrarEvento(vector<string> &log, const string &evento);
void mostrarLog(const vector<string> &log);

int main() {
    bool sistemaArmado = false;

    bool portaAberta = false;
    bool janelaAberta = false;
    bool movimentoDetectado = false;

    vector<string> logEventos;

    int opcao;

    do {
        cout << "\n***** Sistema de Segurança da Casa *****\n";
        cout << "1 - Armar sistema\n";
        cout << "2 - Desarmar sistema\n";
        cout << "3 - Verificar status dos sensores\n";
        cout << "4 - Acionar alarme\n";
        cout << "5 - Mostrar log de eventos\n";
        cout << "0 - Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch (opcao) {
        case 1:
            armarSistema(sistemaArmado, logEventos);
            break;

        case 2:
            desarmarSistema(sistemaArmado, logEventos);
            break;

        case 3:
            cout << "\n*** Ajuste de sensores (simulação) ***\n";
            cout << "A porta esta aberta? (1=Sim, 0=Não): ";
            cin >> portaAberta;

            cout << "A janela esta aberta? (1=Sim, 0=Não): ";
            cin >> janelaAberta;

            cout << "Movimento detectado? (1=Sim, 0=Não): ";
            cin >> movimentoDetectado;

            verificarSensores(portaAberta, janelaAberta, movimentoDetectado);
            break;

        case 4:
            acionarAlarme(portaAberta, janelaAberta, movimentoDetectado, sistemaArmado, logEventos);
            break;

        case 5:
            mostrarLog(logEventos);
            break;

        case 0:
            cout << "\nEncerrando sistema...\n";
            registrarEvento(logEventos, "Sistema desligado");
            break;

        default:
            cout << "Opcao invalida!\n";
        }

    } while (opcao != 0);

    return 0;
}


void registrarEvento(vector<string> &log, const string &evento) {
    log.push_back(evento);
}

void armarSistema(bool &armado, vector<string> &log) {
    if (!armado) {
        armado = true;
        cout << "Armando sistema...\n";
        registrarEvento(log, "Sistema armado");
    } else {
        cout << "O sistema já está armado.\n";
    }
}

void desarmarSistema(bool &armado, vector<string> &log) {
    if (armado) {
        armado = false;
        cout << "Desarmando sistema...\n";
        registrarEvento(log, "Sistema desarmado");
    } else {
        cout << "O sistema já está desarmado.\n";
    }
}

void verificarSensores(bool porta, bool janela, bool movimento) {
    cout << "\n*** Status dos Sensores ***\n";
    cout << "Porta: " << (porta ? "ABERTA" : "Fechada") << endl;
    cout << "Janela: " << (janela ? "ABERTA" : "Fechada") << endl;
    cout << "Sensor de Movimento: " << (movimento ? "MOVIMENTO DETECTADO" : "Nenhum movimento") << endl;
}

void acionarAlarme(bool porta, bool janela, bool movimento, bool armado, vector<string> &log) {
    cout << "\n*** Verificando Ameaças ***\n";

    if (!armado) {
        cout << "Alarme NÃO acionado. O sistema esta desarmado.\n";
        registrarEvento(log, "Tentativa de acionar alarme com sistema desarmado");
        return;
    }

    if (porta || janela || movimento) {
        cout << "ALARME DISPARADO!\n";

        if (porta) registrarEvento(log, "Alarme: Porta aberta detectada");
        if (janela) registrarEvento(log, "Alarme: Janela aberta detectada");
        if (movimento) registrarEvento(log, "Alarme: Movimento detectado");

    } else {
        cout << "Nenhuma ameaça detectada.\n";
        registrarEvento(log, "Verificação sem ameacas");
    }
}

void mostrarLog(const vector<string> &log) {
    cout << "\n***** LOG DE EVENTOS *****\n";
    if (log.empty()) {
        cout << "Nenhum evento registrado\n";
        return;
    }

    for (size_t i = 0; i < log.size(); i++) {
        cout << i + 1 << ". " << log[i] << endl;
    }
}