def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


notas = []

while True:
    nota = float(input("Digite uma nota: "))

    if nota == -1:
        break

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida! Digite um valor entre 0 e 10.")

if notas:
    media_final = calcular_media(notas)

    print(f"\nQuantidade: {len(notas)}")
    print(f"Média: {media_final:.2f}")
    print(f"Maior nota: {int(max(notas)) if max(notas).is_integer() else max(notas)}")
    print(f"Menor nota: {int(min(notas)) if min(notas).is_integer() else min(notas)}")
else:
    print("\nNenhuma nota válida foi cadastrada.")
