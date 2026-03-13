palavra = "rocket raccoon"
palavra = palavra.upper()
letras_acertadas = ["_", "_", "_", "_", "_", "_", "-", "_", "_", "_", "_", "_", "_", "_"]
acertou = False

def mostrar_letras_acertadas():
    for letra in letras_acertadas:
        print(letra, end=" ")

print("Duvido você adivinhar a palavra secreta >:)")
while(not acertou):
    # mostar as letras acertadas
    mostrar_letras_acertadas()

    print("")
    chute = input("Digite uma letra: ")
    indice = 0
    for letra in palavra:
        if chute.upper() == letra:
            letras_acertadas[indice] = letra
        indice = indice + 1

    if letras_acertadas.count("_") == 0:
        print("Parabéns!!! Você acertou a palavra :))")
        mostrar_letras_acertadas()
        acertou = True
