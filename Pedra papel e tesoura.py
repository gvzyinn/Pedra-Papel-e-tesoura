import random

opcoes = ["pedra", "papel", "tesoura"]

pontos_jogador = 0
pontos_computador = 0
historico = []


def descobrir_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"

    if (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        return "jogador"

    return "computador"


while True:
    jogador = input("\nEscolha pedra, papel ou tesoura: ").lower().strip()

    if jogador not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue

    computador = random.choice(opcoes)
    resultado = descobrir_vencedor(jogador, computador)

    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if resultado == "jogador":
        print("Você venceu esta rodada!")
        pontos_jogador += 1

    elif resultado == "computador":
        print("O computador venceu esta rodada!")
        pontos_computador += 1

    else:
        print("Empate!")

    historico.append(
        f"Você: {jogador} | Computador: {computador} | Resultado: {resultado}"
    )

    print(f"\nPlacar — Você: {pontos_jogador} | Computador: {pontos_computador}")

    continuar = input("\nDeseja jogar novamente? (s/n): ").lower().strip()

    if continuar != "s":
        break

print("\n--- Fim de jogo ---")
print(f"Placar final — Você: {pontos_jogador} | Computador: {pontos_computador}")

print("\nHistórico das rodadas:")
for rodada in historico:
    print(rodada)