#!/bin/python3
from math import sqrt # Permet d'utiliser la fonction math sqrt
import os # Permet d'utiliser des commandes linux


def plus(n1, n2):
    return (n1+n2)

def minus(n1, n2):
    return (n1-n2)

def multiplication(n1, n2):
    return (n1*n2)

def division(n1, n2):
    return (n1/n2)

def sqroot(n1):
    return (sqrt(n1))

def squarenbr(n1):
    return (n1*n1)

def firstoption(operator_free):
    num1=int(input("Saisissez un nombre : "))
    num2=int(input("Saisissez un deuxième nombre : "))
    operator=str(input("Saisissez l'opérateur : "))
    if operator=='+':
        print(str(plus(num1, num2))+"\n")
    elif operator=='-':
        print(str(minus(num1, num2))+"\n")
    elif operator=='*':
        print(str(multiplication(num1, num2))+"\n")
    elif operator=='/':
        while (num2 == 0):
            num2=int(input("Division par 0 impossible, saisissez un autre nombre : "))
            print(division(num1, num2))
    else:
        while True:
            if not operator in ['+','-','*','/']:
                operator=str(input(operator_free+"\n"+"L'opérateur saisie n'est pas correcte, veuillez réessayez : "))
            else:
                if operator=='+':
                    print(str(plus(num1,num2))+"\n")
                    break
                elif operator=='-':
                    print(str(minus(num1,num2))+"\n")
                    break
                elif operator=='*':
                    print(str(multiplication(num1,num2))+"\n")
                    break
                elif operator=='/':
                    print(str(division(num1,num2))+"\n")
                    break

def secondoption(operator_math):
    num1=int(input("Saisissez un nombre : "))
    operator=str(input("Saisissez la fonction mathématique que vous souhaitez utiliser : "))
    if operator=='sqrt':
        print(str(sqroot(num1))+"\n")
    elif operator=='**':
        print(str(squarenbr(num1))+"\n")
    else:
        while True:
            if not operator in ['sqrt', '**']:
                operator=str(input(operator_math+"\n"+"La fonction mathématique choisis est incorrecte, veuillez réessayez : "))
            else:
                if operator=='sqrt':
                    print(str(sqroot(num1))+"\n")
                    break
                elif operator=='**':
                    print(str(squarenbr(num1))+"\n")
                    break

def main():
    operator_free=("Les opérateurs disponibles sont : | + | - | / | * | ")
    operator_math=("Les fonctions mathématiques disponibles sont : | sqrt | ** | ")
    os.system('cls' if os.name == 'nt' else 'clear') #Utilise la commande cls si on est sous windows sinon clear
    print("||||||||||| Calculatrice ||||||||||||")
    print("\n")
    while True:
        choix=input("Que voulez-vous faire :"
            "\n1- "+operator_free+
            "\n2- "+operator_math+"\n"
            "3- Quitter.\n")
        if choix=='1':
            firstoption(operator_free)
        elif choix=='2':
            secondoption(operator_math)
        elif choix=='3':
            break
        else:
            while True:
                if not choix in ['1','2']:
                    choix=input("Que voulez-vous faire :"
                        "\n1- "+operator_free+
                        "\n2- "+operator_math+"\n"
                        "3- Quitter."+"\n")
                else:
                    if choix=='1':
                        firstoption(operator_free)
                    elif choix=='2':
                        secondoption(operator_math)
                    elif choix=='3':
                        break
main()
