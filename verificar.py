nome = input("qual é o seu nome?")
idade_texto = input("quantos anos você tem?")

idade = int(idade_texto)

if idade >= 18:
    print(f"Parabéns {nome}! Você já pode tirar sua carteira de motorista (CNH)")
    print ("Prepare as aulas de direção!🚗")

else :
    faltam = 18 - idade
    print(f"Desculpe {nome}, voce ainda não tem idade suficiente para tirar a carteira de motorista (CNH).")
    print(f"Faltam {faltam} anos para você poder tirar sua CNH. Aproveite esse tempo para estudar as regras de trânsito e se preparar para as aulas de direção!🚗")
    

print("Obrigado por usar nosso programa! Tenha um ótimo dia!😊")