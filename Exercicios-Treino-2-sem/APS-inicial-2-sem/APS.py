import hashlib
import json
import os

ARCHIVE = "messages.json"


def loadMessages():
    if not os.path.exists(ARCHIVE):
        return []
    with open(ARCHIVE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def saveMessages(messages):
    with open(ARCHIVE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

def cripto(text, password):
    combine = (text + password).encode("utf-8")
    hashObj = hashlib.sha256(combine)
    hashHex = hashObj.hexdigest()

    random = "".join(chr((ord(c) + len(password)) % 256) for c in text)
    return random, hashHex

def decripto(criptoText, password):
    original = "".join(chr((ord(c) - len(password)) % 256) for c in criptoText)
    return original

def main():
    messages = loadMessages()

    while True:
        print("\n PROTÓTIPO CRIPTOGRAFIA ")
        print("1 - Adicionar nova mensagem")
        print("2 - Listar mensagens salvas")
        print("3 - Sair")
        print("4 - Descriptografar mensagem")  # nova opção
        option = input("Escolha: ").strip()

        if option == "1":
            user = input("Digite o nome do usuário: ").strip()
            text = input("Digite a mensagem (máx 128 chars): ")[:128]
            password = input("Digite uma senha/chave: ")
            random, hashHex = cripto(text, password)

            record = {
                "user": user,
                "message": text,
                "cripto": random,
                "hash": hashHex
            }
            messages.append(record)
            saveMessages(messages)
            print("\nMensagem salva com sucesso!")

        elif option == "2":
            if not messages:
                print("\nNenhuma mensagem salva ainda.")
            else:
                print("\n Mensagens salvas ")
                for i, msg in enumerate(messages, 1):
                    user = msg.get("user", "Desconhecido")
                    print(f"{i}. Usuário: {user}")
                    print(f"   Criptografada: {msg['cripto']}")
                    print(f"   Hash: {msg['hash']}\n")
                print("(* Para ver o texto original, use a opção 4.)")

        elif option == "4":
            if not messages:
                print("\nNenhuma mensagem para descriptografar.")
                continue

            users = sorted(set(msg["user"] for msg in messages))
            print("\n--- Usuários disponíveis ---")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user}")

            try:
                userChoice = int(input("\nEscolha o ID do usuário: "))
                if userChoice < 1 or userChoice > len(users):
                    print("ID de usuário inválido.")
                    continue
            except ValueError:
                print("Digite um número válido.")
                continue

            selectedUser = users[userChoice - 1]
            userMessages = [m for m in messages if m["user"] == selectedUser]

            if not user_messages:
                print("\nEsse usuário não tem mensagens salvas.")
                continue

            print(f"\n--- Mensagens do usuário: {selectedUser} ---")
            for i, msg in enumerate(userMessages, 1):
                print(f"{i}. Criptografada: {msg['cripto']}")
                print(f"   Hash: {msg['hash']}\n")

            try:
                msgChoice = int(input("Escolha o ID da mensagem: "))
                if msgChoice < 1 or msgChoice > len(userMessages):
                    print("ID inválido.")
                    continue
            except ValueError:
                print("Digite um número válido.")
                continue

            msg = userMessages[msgChoice - 1]
            password = input("Digite a senha/chave: ").strip()
            decrypted = decripto(msg["cripto"], password)

            print("\nMensagem original:")
            print(decrypted)

        elif option == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()