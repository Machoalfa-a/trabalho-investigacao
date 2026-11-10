
import os
import time


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def escrever(texto, velocidade=0.02):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()


def linha():
    print("=" * 56)


def titulo():
    limpar_tela()
    linha()
    print("              ARQUIVO 13")
    print("       SISTEMA DE INVESTIGACAO")
    linha()
    print()


def apresentacao():
    titulo()

    escrever("???: Finalmente... voce chegou.", 0.04)
    time.sleep(0.8)

    escrever("\nMeu nome e Detetive Nadya Gorette.", 0.03)
    escrever("Trabalho na Divisao de Casos Nao Resolvidos.", 0.03)

    time.sleep(1)

    escrever("\nDurante anos, investiguei crimes que ninguem", 0.02)
    escrever("conseguiu explicar. Mas existe um caso...", 0.02)
    escrever("um caso que nem eu consegui resolver.", 0.03)

    time.sleep(1)

    linha()
    escrever("CASO 001: O MISTERIO DO QUARTO 217", 0.04)
    linha()

    escrever("\nHa treze anos, uma pessoa desapareceu dentro", 0.02)
    escrever("de um hotel durante uma noite de tempestade.", 0.02)

    escrever("\nCinco pessoas estavam no edificio.", 0.03)
    escrever("Cinco historias diferentes.", 0.03)
    escrever("E uma delas nao pode ser verdadeira.", 0.04)

    time.sleep(1)

    escrever("\nDETETIVE NADYA GORETTE: Preciso de alguem em quem confiar.", 0.03)
    escrever("Alguem que saiba observar, pensar e questionar.", 0.03)

    nome = input("\nAntes de continuar, qual e o seu nome? ").strip()

    if not nome:
        nome = "Investigador"

    time.sleep(0.5)

    escrever(f"\nDETETIVE NADYA GORETTE: Certo, {nome}.", 0.04)
    escrever("A partir de agora, voce faz parte da investigacao.", 0.03)

    time.sleep(1)

    escrever("\nMas vou deixar uma coisa bem clara...", 0.04)
    escrever("Nem todos que parecem culpados sao criminosos.", 0.03)
    escrever("E nem todos que parecem inocentes estao falando a verdade.", 0.03)

    time.sleep(1)

    escrever("\nDETETIVE NADYA GORETTE: Esta preparado para descobrir a verdade?", 0.03)
    input("\nPressione ENTER para continuar...")

    menu_principal(nome)


def menu_principal(nome):
    while True:
        titulo()

        print(f"Investigador: {nome}")
        print("\nO que deseja fazer?")
        print("\n[1] Conhecer o caso")
        print("[2] Aprender como jogar")
        print("[3] Iniciar investigacao")
        print("[0] Sair do jogo")

        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "1":
            conhecer_caso()

        elif opcao == "2":
            regras()

        elif opcao == "3":
            iniciar_investigacao(nome)

        elif opcao == "0":
            escrever("\nDETETIVE NADYA GORETTE: Nos vemos em breve, investigador.")
            escrever("A verdade sempre deixa rastros...")
            break

        else:
            print("\nOpcao invalida. Tente novamente.")
            time.sleep(1)


def conhecer_caso():
    titulo()

    escrever("RELATORIO CONFIDENCIAL - CASO 001\n", 0.03)

    print("Local: Hotel Montenegro")
    print("Horario do desaparecimento: 23h47")
    print("Suspeitos: 5")
    print("Evidencias confirmadas: 0")
    print("Status: CASO ARQUIVADO")

    escrever("\nO antigo relatorio termina com uma frase:", 0.03)
    escrever('"NAO CONFIE NO DEPOIMENTO DAS 23H47."', 0.04)

    input("\nPressione ENTER para voltar ao menu...")


def regras():
    titulo()

    print("COMO JOGAR\n")
    print("1. Investigue os locais disponiveis.")
    print("2. Converse com os suspeitos.")
    print("3. Recolha pistas e leia os documentos.")
    print("4. Compare as evidencias com os depoimentos.")
    print("5. Descubra quem esta mentindo.")
    print("6. Acuse um suspeito somente quando tiver provas.")

    escrever("\nDETETIVE NADYA GORETTE: Nao tenha pressa.", 0.03)
    escrever("Uma acusacao errada pode mudar tudo.", 0.03)

    input("\nPressione ENTER para voltar ao menu...")


def iniciar_investigacao(nome):
    titulo()

    escrever("23h47 - HOTEL MONTENEGRO\n", 0.04)

    escrever("A chuva bate contra as janelas.", 0.03)
    escrever("O corredor esta vazio.", 0.03)
    escrever("Uma porta permanece entreaberta: QUARTO 217.", 0.03)

    escrever(f"\nDETETIVE NADYA GORETTE: {nome}, voce esta no comando.", 0.03)

    print("\nO que deseja investigar?")
    print("\n[1] Examinar o quarto")
    print("[2] Falar com o seguranca")
    print("[3] Examinar o corredor")
    print("[0] Voltar ao menu")

    opcao = input("\nEscolha uma opcao: ").strip()

    if opcao == "1":
        escrever("\nVoce encontra uma fotografia rasgada sobre a mesa.")
        escrever("No verso, ha um horario escrito: 23h17.")
        escrever("Nova pista encontrada: FOTOGRAFIA RASGADA.")

    elif opcao == "2":
        escrever("\nSEGURANCA: Ninguem entrou depois das dez da noite.")
        escrever("Ele evita olhar diretamente para voce.")
        escrever("O depoimento foi registrado.")

    elif opcao == "3":
        escrever("\nVoce encontra marcas de lama perto da escada.")
        escrever("Alguem passou por ali durante a tempestade.")
        escrever("Nova pista encontrada: MARCAS DE LAMA.")

    elif opcao == "0":
        return

    else:
        escrever("\nOpcao invalida.")
        time.sleep(1)
        return

    input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    apresentacao()
