import random

nome = input("Qual é o seu nome, jogador(a)? ")

numero_secreto = random.randint(1, 20)
tentativas = 0
acertou = False

print(f"\n--- 🎲 DESAFIO DE ADIVINHAÇÃO, {nome.upper()}! 🎲 ---")
print("Tente adivinhar o número que eu pensei (entre 1 e 20).")

while not acertou:
    chute = int(input("\nQual o seu palpite? "))
    tentativas += 1 

    if chute == numero_secreto:
        print(f"🎉 PARABÉNS, {nome}! Você acertou em {tentativas} tentativas!")
        acertou = True 
    elif chute < numero_secreto:
        print("Muito baixo! Tente um número maior. ⬆️")
    else:
        print("Muito alto! Tente um número menor. ⬇️")

print("\nObrigado por jogar!")