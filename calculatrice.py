#!/bin/python3
import os # Permet d'utiliser des commandes linux


def plus(n1, n2):
    return (n1+n2)

def minus(n1, n2):
    return (n1-n2)

def multiplication(n1, n2):
    return (n1*n2)

def division(n1, n2):
    return (n1/n2)


if __name__  == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') #Utilise la commande cls si on est sous windows sinon clear
    print("||||||||||| Calculatrice ||||||||||||")
    print("Liste des opérateurs disponibles : | + | - | / | * |")
    print("\n")
    # Ajouter un choix à l'utilisateur permettant de choisir le nombre de chiffres qu'il y aura dans son calcul ?
    operator_free=("Les opérateurs disponibles sont : | + | - | / | * |")
    num1=int(input("Saisissez un nombre : "))
    num2=int(input("Saisissez un deuxième nombre : "))
    operator=input("Saisissez l'opérateur : ")
    if operator=='+':
        print(plus(num1, num2))
    elif operator=='-':
        print(minus(num1, num2))
    elif operator=='*':
        print(multiplication(num1, num2))
    elif operator=='/':
        while (num2 == 0):
            num2=int(input("Division par 0 impossible, saisissez un autre nombre : "))
            print(division(num1, num2)
    else:
        while (operator !='+' | operator !='-' | operator !='*' | operator !='/'):
            operator=str(input("L'opérateur saisie n'est pas correcte, veuillez réessayez : "+"\n"+operator_free))
