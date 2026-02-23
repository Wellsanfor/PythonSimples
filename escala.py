nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("digite a segunda nota:"))

media = (nota1 + nota2) / 2

print(f"\nSua média final foi {media}")

if media >= 7.0:
    print("Resultado: Aprovado(a)!")
elif media >= 5.0:
    print("Resultado: RECUPERAÇÃO . Estude mais e tente novamente!")
else: 
    print("Resultado: REPROVADO(a). Não desista, continue se esforçando e buscando melhorar!")