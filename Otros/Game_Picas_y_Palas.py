# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:19:41 2022

@author: Sebastian
"""

import random
#import math

n=4; #El numero de decimales con el que se va jugar




def generate_Master_Number(n):
    Master_Num=""
    newNumber="x" #x Sirve para que entre al while la primera vez
    for i in range(n):
        newNumber=str(random.randint(0,9))
        while (newNumber in Master_Num): #Si el numero ya estaba, repetir la eleccion
            newNumber=str(random.randint(0,9))            
        #Cuando tenga un numero que no este repetido agregarlo al string
        Master_Num+=newNumber;
    #Cuando tenga los n numeros random, los regresa como string
    return Master_Num
            
def score_Picas_Palas(Master_Num,Try_Num):
    """    

    Parameters
    ----------
    Master_Num : str
        Es el numero secreto que el jugador intenta adivinar.
    Try_Num : str
        Es el numero con el que el jugador esta probando a ver como le va.

    Returns
    -------
    List: ["Try_num", picas, palas].
    num es el numero que el jugador ingreso, picas la cantidad de numeros acertados y bien posicionads
    palas la cantidad de numeros acertados pero mal posicionados

    """
    picas=0
    palas=0
    for number in Try_Num: #barre cada numero dado
        if number in Master_Num: #Revisa si esta en el Master
            if Try_Num.find(number)==Master_Num.find(number): #Si estan en la misma posicion
                palas+=1
            else:
                picas+=1
    return [Try_Num,picas,palas]
                    
            
        
    
def Validar_Numero(Try_Num,n):
    """
    
    Parameters
    ----------
    Try_Num : str
        Verifica si el usuario ingreso un numero con la longitud correcta y sin repetir
        
    Returns
    -------
    Truo or false

    """
    if n!=len(Try_Num):
        return False
    for number in Try_Num:
        if Try_Num.count(number)!=1:
            return False
    return True

def print_list(history):
    """
    
    Parameters
    ----------
    history : list
        Es una lista que contiene otra lista 
        [['4132', 3, 1],
         ['5162', 2, 0],
         ['1567', 0, 1]]
    Returns
    -------
    None.

    """
    
    print("Your Numbers: ")
    print("-----------------------------")
    print("Number"+"\t| Picas"+"\t| Palas")
    print("-----------------------------")
    for element in history:
        print(element[0]+"\t| "+str(element[1])+"  \t|"+str(element[2]))   


#################################################################
#               MAIN
Master_Num=generate_Master_Number(n)
#Master_Num="1234"
history=[]

Try_Num="0000"
print("Estoy pensando en un numero de cuatro cifras, ninguno de ellos se repite")
print("Ingresa 0 en cualquier momento para terminar el juego")

while Try_Num!="0":
    Try_Num=input("Ingresa un numero de cuatro cifras: ")
    Try_Num=str(Try_Num)
    if Validar_Numero(Try_Num,n)==False:
        if Try_Num=="0":
            print("No adivinaste el numero")
            continue
        else:
            print("El valor ingresado no es valido")
            continue
    
    score=score_Picas_Palas(Master_Num,Try_Num)
    history.append(score)
    print_list(history)
    
    if(score[2]==n):
        print("Correcto!!")
        break
print ("El numero era:",Master_Num)
input("Presiona enter para cerrar")



                  