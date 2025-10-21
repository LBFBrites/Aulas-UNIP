import hashlib
import json
import os

ARCHIVE = "messages.json"

#try catch patrocinado por cod3r e jonathan
def loadMessages():
    if not os.path.exists(ARCHIVE):
        return []
    with open(ARCHIVE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

#message.save
def saveMessages(message):
    with open(ARCHIVE, "w", encoding="utf-8") as f:
        json.dump(message, f, indent=2, ensure_ascii=False)

#"""""criptografia""""" perguntar pro professor se precisa usar outro tipo de criptografia ou só o hashlib basta
def cripto(text, password):
    # text + password
    combine = (text + password).encode("utf-8")
    hashObj = hashlib.sha256(combine)
    hashHex = hashObj.hexdigest()

    # embaralhar (ideia de boa pratica de arquitetura by jonathan)
    random = "".join(chr((ord(c) + len(password)) % 256) for c in text) #diferente do exercicio da primeira prova que usava ord e chr separados
    return random, hashHex

#menu
def main():
    messages = loadMessages()

    while True:
        print("\n PROTÓTIPO CRIPTOGRAFIA ")
        print("1 - Adicionar nova mensagem")
        print("2 - Listar mensagens salvas")
        print("3 - Sair")
        option = input("Escolha: ").strip()

        if option == "1":
            text = input("Digite a mensagem (máx 128 chars): ")[:128]
            password = input("Digite uma senha/chave: ")
            random, hashHex = cripto(text, password)

            record = {
                "message": text,
                "cripto": random,
                "hash": hashHex
            }
            messages.append(record)
            saveMessages(messages)
            print("\n Mensagem salva com sucesso")

        elif option == "2":
            if not messages:
                print("\nNenhuma mensagem salva ainda.")
            else:
                print("\n--- Mensagens salvas ---")
                for i, msg in enumerate(messages, 1): #enumerate dica do jonathan. usava i+= 1 antes
                    print(f"{i}. Original: {msg['message']}")
                    print(f"   Criptografada: {msg['cripto']}")
                    print(f"   Hash: {msg['hash']}\n")

        elif option == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()