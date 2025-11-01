import random
import time

moedas = 10
tentativas = 5 


#numero gerado pelo computador
n_Mago = random.randint(1, 20)
#tempin de espera
time.sleep(1)

#o que a poção faz
def funcao_pocao():
    pergunta_pocao = input("Você deseja usar a poção ganha? (Y/n):")
    print('\033[3;30m' + "A poção faz com que você tenha mais sorte em escolher o numero" + '\033[0m')
    if pergunta_pocao.lower() == "y":
        print('\033[3m'  +"Você usou a poção a chance de voce acertar o numero diminui" + '\033[0m')
        resposta = int(input("Escolha um numero de 1 a 10: "))
        #numero gerado pelo computador atualizado
        n_Mago = random.randint(1, 10)
    #acerto
    elif resposta == n_Mago:
        print('\033[1;33m' + "Você acertou o numero" + '\033[0m')
    #erro
    elif resposta != n_Mago:
        print("Você errou, mas pode tentar continuar")
    #escolha de não
    elif pergunta_pocao.lower() == "n":
        n_Mago = random.randint(1, 20)
    return n_Mago
        

print('\033[3;32m' + "Voce encontrou um mago secreto" + '\033[0m')
print("\n" + '\033[3m' + "ele pede para voce escolher um numero de 1 a 20")

#resposta input()
time.sleep(0.60)
resposta = int(input("Escolha um numero de 1 a 20: "))

#tentativas
while tentativas >= 0 and moedas >= 0:
    if resposta == n_Mago:
       print("\033[1;32m" + "Você adivinhou! O adivinho te entrega uma poção da sorte! 🍀" + "\033[0m")
       n_Mago = funcao_pocao()
       moedas += 5
       resposta = int(input("Escolha um numero de 1 a 20: "))
    else:
        print("Você errou o número, " + '\033[1;31m' + "infelizmente pra você, " + '\033[3;32m' + "felizmente pro mago 😈" + '\033[0m')
        moedas -= 2
        tentativas -= 1
        if tentativas > 0:
            resposta = int(input("Escolha outro número de 1 a 20: "))
        else:
            print("\033[1;31mSuas tentativas acabaram... o mago desaparece rindo 👻\033[0m")

print(f"\n\033[1;33mFim de jogo! Você terminou com {moedas} moedas.\033[0m")


        