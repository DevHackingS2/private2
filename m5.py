import sys
import os
import time
os.system("clear")
os.system("rm -rf m4.py")

message2 = "Arquivo sendo deletado..."
for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(5)
os.system("clear")

print("Arquivo deletado! :) ")
time.sleep(4)



def menu():
    print("-====| Escolha uma das opções |====-")
    print("-= [1] SEGREDO !  ")
    print("-= [2] Textinho ! ")
    print("-= [3] ??????? ")

menu()

opcoes = int(input("Digite algum número!: "))

while opcoes != 0:
    if opcoes == 1:
        os.system("clear")
        mim = "Eu te amo muito, o amor que sinto por você no começo foi de repente, Durante esse tempo todo eu tive certeza que é você, decidi de uma vez por todas que é com você que eu decidi compartilhar minha vida toda (Não morri não tá, queria mas não..), te ter em todos os momentos bons e ruins, porque você é a minha alma gêmea, vocẽ é a pessoa em que eu sempre sonhei... "
        for char in mim:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        break

    elif opcoes == 2:
        os.system("clear")
        message = "Está sendo desenvolvido"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        break

    elif opcoes == 3:
        break
    elif opcoes == 4:
        break
    elif opcoes == 5:
        break          
    else:
        print("DIGITE O NUMERO MIZERA! ")
        break
    menu()
