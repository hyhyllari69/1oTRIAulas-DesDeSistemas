# Importação da biblioteca
import random
# Sorteio número aleatório
numero = random.randint (0,10)

tentativas = 1
while (tentativas <= 3):
    print("Tentativa:", tentativas)
    chute = int(input("Digite o seu chute (0 a 10):"))
    
    if chute == numero:
        print("Parabéns, você é foda <3")
        break
    else:
        print("Erroukkkk </3")
    tentativas = tentativas + 1
    print("Fim do Jogo XD")