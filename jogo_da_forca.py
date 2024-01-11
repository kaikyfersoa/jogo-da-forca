import random as rd

print("Welcome to the Hangman game!")
lista_de_palavras = ["banana", "melancia", "apicultor", "paraguai", "mingau"]
chances = 5
palavra = rd.choice(lista_de_palavras)
entrada = ""
misterio = ["_"] * len(palavra)
repetidas = []
advinha = list(palavra)

while chances > 0 and "_" in misterio:
    entrada = input("Diga uma letra: ").lower()

    if len(entrada) != 1 or not entrada.isalpha():
        print("Por favor, digite apenas uma letra válida.")
        continue

    for i in repetidas:
        if entrada == i:
            chances -= 1

    acerto = False
    for i in range(len(advinha)):
        if advinha[i] == entrada:
            misterio[i] = entrada
            acerto = True

    repetidas.append(entrada) if entrada not in repetidas else ...

    if not acerto:
        chances -= 1

    print(f"{' '.join(misterio)}, restam {chances} chances para você!")

if "_" not in misterio:
    print(f"Parabéns, você ganhou! A palavra é: {palavra}")
else:
    print(f"Você perdeu. A palavra era: {palavra}")
