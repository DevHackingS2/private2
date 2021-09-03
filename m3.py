import os
import sys
import time

os.system("touch nomeMariahsenha1607Mariah@.txt")
os.system("nano nomeMariahsenha1607Mariah@.txt")
time.sleep(6)
os.system("touch Vocenaoviu?.txt")
os.system("nano Vocenaoviu?.txt")

os.system("clear")

nome = input("Digite Seu Nome: ")


if nome == "Mariah":
    os.system("clear")
    print("Verificando Nome...")
    time.sleep(4)
    os.system("clear")
    print("Verificado :) ")
    time.sleep(4)
    os.system("clear")
else:
    print("Desculpe, Foi enviado para a pessoa errada!")
    time.sleep(4)
    quit()

senha = input("Digite a senha: ")

if senha == "1607Mariah@":
    os.system("clear")
    print("Verificando Senha...")
    time.sleep(4)
    os.system("clear")
    print("Verificado, Liberando acesso!")
    time.sleep(4)
    os.system("clear")
    print(" -= | Feito Pelo seu Namoradinho | =- ")
    time.sleep(4)
    os.system("clear")
    os.system("rm -rf nomeMariahsenha1607Mariah@.txt")
else:
    print("Senha ou Nome incorreto(a), rode o programa novamente...")
    quit()
    

def menu():
    print(" -=====| Bem vindo {} | ====-  ".format(nome))
    print("[1] - = Textinho!")
    print("[2] - = Textinho!")
    print("[3] - = Textinho!")
    print("[4] - = Textinho!")
    print("[5] - = Textinho!")


menu()

opcoes = int(input("Digite o número: "))

while opcoes != 0:
    if opcoes == 1:
        os.system("clear")
        mim = " Está sendo Desenvolvido! "
        print(mim)
        time.sleep(0.1)
        break

    elif opcoes == 2:
        os.system("clear")
        message = "Está sendo desenvolvido"
        print(message)
        break

    elif opcoes == 3:
        print("Olhe para o lado! ")
        break
    elif opcoes == 4:
        message2 = "Nesse momento eu estou do seu lado, com muita vergonha novamente, infelizmente, pra certeza mesmo eu preciso te contar um segredo!"
    elif opcoes == 5:
        break          
    else:
        print("DIGITE O NUMERO MIZERA! ")

