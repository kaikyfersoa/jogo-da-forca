# Jogo Da Forca (Hangman)

## Overview
O jogo da forca (Hangman) é um jogo clássico em que um jogador tenta adivinhar uma palavra, letra por letra, antes de atingir um número máximo de tentativas. Neste código em Python, o jogador tenta adivinhar uma palavra aleatória escolhida de uma lista. O jogo continua até que o jogador adivinhe a palavra ou esgote todas as suas chances.

## Código Python
```python
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
```

## Funcionamento
1. O código começa saudando o jogador e escolhendo aleatoriamente uma palavra da lista `lista_de_palavras`.
2. O jogador tem um número limitado de chances (5 no caso) para adivinhar a palavra.
3. O jogo entra em um loop principal, onde o jogador é solicitado a digitar uma letra.
4. A entrada do jogador é validada para garantir que seja uma única letra alfabética.
5. Se a letra já foi tentada antes, o jogador perde uma chance.
6. Se a letra está na palavra, ela é revelada no "mistério" (lista `misterio`).
7. As letras tentadas são armazenadas na lista `repetidas` para evitar repetições.
8. O jogo continua até que o jogador adivinhe a palavra ou esgote todas as chances.
9. No final, uma mensagem informa se o jogador ganhou ou perdeu.

