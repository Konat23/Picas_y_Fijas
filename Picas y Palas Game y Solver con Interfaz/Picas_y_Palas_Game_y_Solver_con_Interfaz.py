# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:51:53 2023

@author: Jennifer y Sebastian
"""
# Ancho - Alto - Width height
from tkinter import *
import random



########################################################
########################################################
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

#PROPIEDAD DEL CODIGO DE Konat XD
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
    List: ["Try_num", picas, palas, pepitas].
    num es el numero que el jugador ingreso, picas la cantidad de numeros acertados y bien posicionads
    palas la cantidad de numeros acertados pero mal posicionados

    """
    global var
    picas=0
    palas=0
    global Try_Num_global
    global EnviarButton
    global picas_global
    global palas_global
    
    Try_Num_global.set(Try_Num)
    print("Intento: ",Try_Num)
    print(var.get())
    print("Esperando entrada del usuario")
    EnviarButton.wait_variable(var)
    
    picas=picas_global
    palas=palas_global
    print("Score recibio: picas: ",picas,"palas: ",palas)
    
    picas=int(picas)
    palas=int(palas)
    pepitas=picas+palas; 
        
    return [Try_Num,picas,palas,pepitas]

#PROPIEDAD DEL CODIGO DE JENNIFER XD
def score_Picas_Palas_Jennifer(Master_Num,Try_Num):
    """
    Parameters
    ----------
    Master_Num : str
        Es el numero secreto que el jugador intenta adivinar.
    Try_Num : str
        Es el numero con el que el jugador esta probando a ver como le va.

    Returns
    -------
    List: ["Try_num", picas, palas, pepitas].
    num es el numero que el jugador ingreso, picas la cantidad de numeros acertados y bien posicionads
    palas la cantidad de numeros acertados pero mal posicionados

    """
    picas=0
    palas=0
    print("Intento: ",Try_Num)
    picas=input("Ingresa el numero picas: ")
    palas=input("Ingresa el numero palas: ")
    
    picas=int(picas)
    palas=int(palas)
    pepitas=picas+palas; 
        
    return [Try_Num,picas,palas,pepitas]




def score_Picas_Palas_v0(Master_Num,Try_Num):
    """
    Parameters
    ----------
    Master_Num : str
        Es el numero secreto que el jugador intenta adivinar.
    Try_Num : str
        Es el numero con el que el jugador esta probando a ver como le va.

    Returns
    -------
    List: ["Try_num", picas, palas, pepitas].
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
    pepitas=picas+palas; 
    return [Try_Num,picas,palas,pepitas]

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
    return None

########################################################
########################################################

n=4; #El numero de decimales con el que se va jugar
Master_Num=""       
    

def create_cuencos():
    #Cuenco_A=["1","2","3","4"]
    #Cuenco_B=["5","6","7","8"]
    #Cuenco_C=["9","0"]
    Cuenco_A=generate_Master_Number(4)
    
    Num=""
    newNum="x" #x Sirve para que entre al while la primera vez
    for i in range(4):
        newNum=str(random.randint(0,9))
        while (newNum in Num or newNum in Cuenco_A): #Si el numero ya estaba o si ya estaba en el cuenco A, repetir la eleccion
            newNum=str(random.randint(0,9))                     
        Num+=newNum;
    Cuenco_B=Num
    
    Num=""
    newNum="x" #x Sirve para que entre al while la primera vez
    for i in range(2):
        newNum=str(random.randint(0,9))
        while (newNum in Num or newNum in Cuenco_A or newNum in Cuenco_B): #Si el numero ya estaba o si ya estaba en el cuenco A o B, repetir la eleccion
            newNum=str(random.randint(0,9))                     
        Num+=newNum;

    Cuenco_C=Num
    return [Cuenco_A,Cuenco_B,Cuenco_C]

#Solvers de distintas situaciones
#CONOCIENDO EL ESTADO DE 2 NUMEROS (seguro de que ambos esten o que ambos no esten), BUSCA 1 NUMERO EN UN CUENCO DE 4 ESPACIOS
def solver1(known1,known2,cuenco,Master_Num):
    
    subhistory=[]
    Try_Num=cuenco[0:2]+known1+known2
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
   
    Try_Num=known1+known2+cuenco[1:3]
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
     
    if (subhistory[0][3]==3 or subhistory[0][3]==1):
        if (subhistory[1][3]==3 or subhistory[1][3]==1):
            return [cuenco[1],subhistory]
        elif(subhistory[1][3]==2 or subhistory[1][3]==0):
            return [cuenco[0],subhistory]  
    elif(subhistory[0][3]==2 or subhistory[0][3]==0):
        if (subhistory[1][3]==3 or subhistory[1][3]==1):
            return [cuenco[2],subhistory]
        elif(subhistory[1][3]==2 or subhistory[1][3]==0):
            return [cuenco[3],subhistory]   
    else:
        print("Error solver1")
                 
#CONOCIENDO EL ESTADO DE 1 NUMEROS, BUSCA 3 NUMERO EN UN CUENCO DE 4 ESPACIOS
def solver2(known1,cuenco,Master_Num):    
    subhistory=[]
    Try_Num=cuenco[0:3]+known1
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
   
    if (subhistory[0][3]==3):
        Try_Num=known1+cuenco[1:4]
        score=score_Picas_Palas(Master_Num,Try_Num)
        subhistory.append(score)
        
        
        if (subhistory[1][3]==3):
            Try_Num=cuenco[0:2]+known1+cuenco[3]
            score=score_Picas_Palas(Master_Num,Try_Num)
            subhistory.append(score)  
            
            if (subhistory[2][3]==3):
                return [cuenco[0]+cuenco[3]+cuenco[2],subhistory]
            else:
                return [cuenco[0]+cuenco[3]+cuenco[1],subhistory]
        else:
            return [cuenco[1:4],subhistory]        
        
    elif(subhistory[0][3]==4):
        return [cuenco[0:3],subhistory] 
    else:
        print("Error solver 2")
        
    
#CONOCIENDO EL ESTADO DE 2 NUMEROS(que si estan), BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIOS
def solver3v1(known1,known2,cuenco,Master_Num):    
    subhistory=[]
    Try_Num=cuenco[0:2]+known2+known1 #Elegir los dos primeros del cuenco
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)

    if (subhistory[0][3]==2 ):
        return [cuenco[2]+cuenco[3],subhistory] #Serian los que no elegi
    elif(subhistory[0][3]==3 ):
        Try_Num=cuenco[1:3]+known2+known1 #Elegir el segundo y tercero del cuenco (se cambia el orden de known)
        score=score_Picas_Palas(Master_Num,Try_Num)
        subhistory.append(score)
        if(subhistory[1][3]==2):
            return [cuenco[0]+cuenco[3],subhistory]            
        elif(subhistory[1][3]==3):
            Try_Num=known2+known1+cuenco[1]+cuenco[3]
            score=score_Picas_Palas(Master_Num,Try_Num)
            subhistory.append(score)
            if(subhistory[2][3]==2):
                return [cuenco[0]+cuenco[2],subhistory]
            elif(subhistory[2][3]==4):#Solo me puede dar 4 o 2
                return [cuenco[1]+cuenco[3],subhistory]
        elif(subhistory[1][3]==4):
            return [cuenco[1]+cuenco[2],subhistory]    
        else:
            print("Error solver 3v1")
    elif(subhistory[0][3]==4):
        return [cuenco[0]+cuenco[1],subhistory] #Serian los que elegi
    else:
        print("Error al resolver CONOCIENDO EL ESTADO DE 2 NUMEROS, BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIO V1")       
       
#CONOCIENDO EL ESTADO DE 2 NUMEROS(que NO estan), BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIOS
def solver3v2(known1,known2,cuenco,Master_Num):    
    subhistory=[]
    Try_Num=cuenco[0:2]+known1+known2 #Elegir los dos primeros del cuenco
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)

    if (subhistory[0][3]==0 ):
        return [cuenco[2]+cuenco[3],subhistory] #Serian los que no elegi
    elif(subhistory[0][3]==1):
        Try_Num=cuenco[1:3]+known2+known1 #Elegir el segundo y tercero del cuenco (se cambia el orden de known)
        score=score_Picas_Palas(Master_Num,Try_Num)
        subhistory.append(score)
        if(subhistory[1][3]==0):
            return [cuenco[0]+cuenco[3],subhistory]            
        elif(subhistory[1][3]==1):
            Try_Num=known2+known1+cuenco[1]+cuenco[3]
            score=score_Picas_Palas(Master_Num,Try_Num)
            subhistory.append(score)
        
            if(subhistory[2][3]==0):
                return [cuenco[0]+cuenco[2],subhistory]
            elif(subhistory[2][3]==2):#Solo me puede dar 4 o 2
                return [cuenco[1]+cuenco[3],subhistory]
            else:
                print("error2")
        elif(subhistory[1][3]==2):
            return [cuenco[1]+cuenco[2],subhistory]
        else:
            print("error 1")
    elif(subhistory[0][3]==2):
        return [cuenco[0]+cuenco[1],subhistory] #Serian los que elegi
    else:
        print("Error al resolver CONOCIENDO EL ESTADO DE 2 NUMEROS, BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIO V2") 

#CONOCIENDO EL ESTADO DE 2 NUMEROS(UNO que NO esta y UNO que SI esta), BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIOS
def solver3v3(known1,known2,cuenco,Master_Num):    
    subhistory=[]
    Try_Num=cuenco[0:2]+known1+known2 #Elegir los dos primeros del cuenco
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)

    if (subhistory[0][3]==1 ):
        return [cuenco[2]+cuenco[3],subhistory] #Serian los que no elegi
    elif(subhistory[0][3]==2):
        Try_Num=cuenco[1:3]+known2+known1 #Elegir el segundo y tercero del cuenco (se cambia el orden de known)
        score=score_Picas_Palas(Master_Num,Try_Num)
        subhistory.append(score)
        if(subhistory[1][3]==1):
            return [cuenco[0]+cuenco[3],subhistory]            
        elif(subhistory[1][3]==2):
            Try_Num=known2+known1+cuenco[1]+cuenco[3]
            score=score_Picas_Palas(Master_Num,Try_Num)
            subhistory.append(score)
        
            if(subhistory[2][3]==1):
                return [cuenco[0]+cuenco[2],subhistory]
            elif(subhistory[2][3]==3):#Solo me puede dar 4 o 2
                return [cuenco[1]+cuenco[3],subhistory]
            else:
                print("error2")
        elif(subhistory[1][3]==3):
            return [cuenco[1]+cuenco[2],subhistory]
        else:
            print("error 1")
    elif(subhistory[0][3]==3):
        return [cuenco[0]+cuenco[1],subhistory] #Serian los que elegi
    else:
        print("Error al resolver CONOCIENDO EL ESTADO DE 2 NUMEROS, BUSCA 2 NUMERO EN UN CUENCO DE 4 ESPACIO V3")
#Cada color representa cada uno de los caminos que podria tomar despues de los primeros dos intentos (anexo)

#VERDE
def verde(cuencoG,cuencoP,Master_Num): #cuencoG es el cuenco grande que contiene 2 pepitas
    correctos=cuencoP
    solucion=solver3v1(cuencoP[0],cuencoP[1],cuencoG,Master_Num)
    correctos+=solucion[0]
    return  [correctos,solucion[1]]

def morado(cuencoG1,cuencoG2,cuencoP,Master_Num): #cuencoG1 es el que no tienen ninguna pepita
    correctos=""
    subhistory=[]
    Try_Num=cuencoG1[0:3]+cuencoP[0] #Elegir los 3 primeros del cuenco grande vacio y uno del cuenco pequeño
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
    if (subhistory[0][3]==1):
        solucion=solver2(cuencoP[0],cuencoG2,Master_Num)
        correctos=cuencoP[0]+solucion[0]
        
    elif(subhistory[0][3]==0):
        solucion=solver2(cuencoP[1],cuencoG2,Master_Num)
        correctos=cuencoP[1]+solucion[0]
        
    else:
        print("Errror codigo morado")
        
    subhistory+=solucion[1]
    return [correctos,subhistory]

def rosado(cuencoG1,cuencoG2,cuencoP,Master_Num):
    correctos=cuencoP
    subhistory=[] 
    solucion1=solver1(cuencoP[0],cuencoP[1],cuencoG1,Master_Num)
    solucion2=solver1(solucion1[0],cuencoP[0],cuencoG2,Master_Num)
    subhistory+=solucion1[1]+solucion2[1]
    correctos+=solucion1[0]+solucion2[0]
    return [correctos,subhistory]

def celeste(cuencoG1,cuencoG2,cuencoP,Master_Num): #G2 contiene 2 pepitas y G1 contiene 1 pepita
    correctos=""
    subhistory=[]
    
    Try_Num=cuencoG2[1]+cuencoG2[2]+cuencoG2[0]+cuencoP[0]
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
    
    Try_Num=cuencoG2[2]+cuencoG2[0]+cuencoG2[1]+cuencoP[1]
    score=score_Picas_Palas(Master_Num,Try_Num)
    subhistory.append(score)
    if (subhistory[0][3]>subhistory[1][3]): #Si se reduce la cantidad de pepitas en el segundo try
        correctos+=cuencoP[0]      
    elif(subhistory[0][3]<subhistory[1][3]):#Si se aumenta la cantidad de pepitas en el segundo try
        correctos+=cuencoP[1]

    solucion1=solver3v3(cuencoP[0],cuencoP[1],cuencoG2,Master_Num)
    correctos+=solucion1[0]
    solucionfinal=solver1(correctos[0],correctos[1],cuencoG1,Master_Num)
    
    correctos+=solucionfinal[0]
    subhistory+=solucion1[1]+solucionfinal[1] #concatenamos los historiales
    return [correctos, subhistory]

def rojo(cuencoG1,cuencoG2,cuencoP,Master_Num): #G1 es el que tiene una pepita y G2 el que tiene 3 pepitas
    correctos=""
    subhistory=[]
    solucion1=solver1(cuencoP[0],cuencoP[1],cuencoG1,Master_Num) 
    solucion2=solver2(solucion1[0],cuencoG2,Master_Num)
    correctos+=solucion1[0]+solucion2[0]
    subhistory+=solucion1[1]+solucion2[1]
    
    return [correctos, subhistory]

def piel(cuencoG1,cuencoG2,cuencoP,Master_Num):
    correctos=""
    subhistory=[]
    solucion1=solver3v2(cuencoP[0],cuencoP[1],cuencoG1,Master_Num)
    correctos+=solucion1[0]
    solucion2=solver3v1(correctos[0],correctos[1],cuencoG2,Master_Num)
    correctos+=solucion2[0]
    subhistory+=solucion1[1]+solucion2[1]
    
    return [correctos, subhistory]

def encontrar_picas_palas(Master_Num):
    history=[]
    cuencos=create_cuencos()
    encontrados=["",[]]

    cuencoP=cuencos[2]

    score=score_Picas_Palas(Master_Num,cuencos[0])
    history.append(score)
    score=score_Picas_Palas(Master_Num,cuencos[1])
    history.append(score)

    c1=history[0][3]
    c2=history[1][3]
    chivo=""
    #verde
    if ((c1==2 and c2==0)^(c2==2 and c1==0)):
        chivo="verde"
        if (c1==2):
            encontrados=verde(cuencos[0], cuencoP, Master_Num)
        else:
            encontrados=verde(cuencos[1], cuencoP, Master_Num)
    #morado
    if ((c1==3 and c2==0)^(c2==3 and c1==0)):        
        chivo="morado"
        if (c1==3):
            encontrados=morado(cuencos[1], cuencos[0], cuencoP, Master_Num)
        else:
            encontrados=morado(cuencos[0], cuencos[1], cuencoP, Master_Num)
    #azul
    if ((c1==4)^(c2==4)):
        chivo="azul"
        if (c1==4):
            encontrados=[cuencos[0],[]]
        else:
            encontrados=[cuencos[1],[]]
    #rosada
    if (c1==1 and c2==1):
        chivo="rosada"
        encontrados=rosado(cuencos[0], cuencos[1], cuencoP, Master_Num)
        
    #celeste
    if ((c1==1 and c2==2) or (c1==2 and c2==1)):
        chivo="celeste"
        if (c1==1 and c2==2):
            encontrados=celeste(cuencos[0], cuencos[1], cuencoP, Master_Num)
        else:
            encontrados=celeste(cuencos[1], cuencos[0], cuencoP, Master_Num)

    #rojo
    if ((c1==1 and c2==3) or (c1==3 and c2==1)):
        chivo="rojo"
        if (c1==1 and c2==3):
            encontrados=rojo(cuencos[0], cuencos[1], cuencoP, Master_Num)
            
        else:
            encontrados=rojo(cuencos[1], cuencos[0], cuencoP, Master_Num)
        
    #piel
    if (c1==2 and c2==2):
        chivo="piel"
        encontrados=piel(cuencos[0], cuencos[1], cuencoP, Master_Num)
        
    history+=encontrados[1]       
    
    #print("\nResuelto por: ", chivo)
    #print("Real",Master_Num)
    #print("Encontrado",encontrados[0])
    #print("Historial: ", encontrados[1])
    return [encontrados[0], chivo, history]

#UBICAR PALAS
def encontrar_ubicacion_palas(subhistory, numeros, respuesta):
    indice=[]
    for h in subhistory: 
        if(h[1]==0):
            if(h[2]!=0):
                indice.append(h) #GUARDA LOS HISTORIALES QUE TIENEN PICAS=0 Y PALAS DIFERENTE DE 0

    if(len(indice)!=0): #ENTRA AQUI SI HAY ALGUN DATO EN EL HISTORY QUE TENGA PICAS=0 Y PALAS DIF DE 0
        for ind in indice: #recorre todos los historiales en los que haya palas con picas=0
            try1=ind[0]  
            for i in range(4):  #recorre todo el número del historial
                if(try1[i] in numeros): #comprobar cuales son las palas y definirlas en la respuesta
                    respuesta[i]=try1[i]
                    
    return respuesta

#DESCARTAR POSICIONES PARA NUMEROS - LISTA NEGRA
def descatar_posiciones(subhistory, numeros, lista_negra):
    indice2=[]
    for h in subhistory:
        if(h[1]!=0):
            if(h[2]==0):
                indice2.append(h) #GUARDA LOS HISTORIALES QUE TIENEN PICAS DIFERENTE DE 0 Y PALAS=0
    if(len(indice2)!=0):
        for ind in indice2:
            try1=ind[0]
            for i in range(4):
                if(try1[i] in numeros):
                   lista_negra[int(try1[i])][i]="X"
    return lista_negra

#Ubicar un numero teniendo en cuenta que no puede ir en las otras 3 posiciones
def posicioar_con_los_descartes(lista_negra,numeros, respuesta):
    
    for i in range(4):   
        A=lista_negra[int(numeros[i])][0]
        B=lista_negra[int(numeros[i])][1]
        C=lista_negra[int(numeros[i])][2]
        D=lista_negra[int(numeros[i])][3]
        
        if(((not A=="X") and B=="X" and C=="X" and D=="X") or (A=="X" and (not B=="X") and C=="X" and D=="X") or (A=="X" and B=="X" and (not C=="X") and D=="X") + (A=="X" and B=="X" and C=="X" and not(D=="X"))):
            if(A is None):
                respuesta[0]=numeros[i]
            elif(B is None):
                respuesta[1]=numeros[i]   
            elif(C is None):
                respuesta[2]=numeros[i] 
            elif(D is None):
                respuesta[3]=numeros[i]   

                    
    return respuesta

#Si 3 numeros niegan la posicion, entonces el ultimo es la posicion
def por_negacion(lista_negra,numeros, respuesta):
    for i in range(4):   
        A=lista_negra[int(numeros[0])][i]
        B=lista_negra[int(numeros[1])][i]
        C=lista_negra[int(numeros[2])][i]
        D=lista_negra[int(numeros[3])][i]
        
        if(((not A=="X") and B=="X" and C=="X" and D=="X") or (A=="X" and (not B=="X") and C=="X" and D=="X") or (A=="X" and B=="X" and (not C=="X") and D=="X") + (A=="X" and B=="X" and C=="X" and not(D=="X"))):
            if(A is None):
                respuesta[i]=numeros[0]
            elif(B is None):
                respuesta[i]=numeros[1]   
            elif(C is None):
                respuesta[i]=numeros[2] 
            elif(D is None):
                respuesta[i]=numeros[3]                       
    return respuesta


#si ya ubico un número, poner X en esa posicion para los demaás
def ponerX_por_ubicar_un_numero(subhistory, numeros, lista_negra, respuesta):
     
    for i in range(4): 
        respaldo1=numeros
        if(respuesta[0] is not None or respuesta[1] is not None or respuesta[2] is not None or respuesta[3] is not None):
            if (respuesta[i] is not None):
                respaldo1=respaldo1.replace(respuesta[i], '')
                lista_negra[int(respaldo1[0])][i]="X"
                lista_negra[int(respaldo1[1])][i]="X"
                lista_negra[int(respaldo1[2])][i]="X"
                
                lista=[0,1,2,3]
                lista.remove(i)
                
                lista_negra[int(respuesta[i])][lista[0]]="X"
                lista_negra[int(respuesta[i])][lista[1]]="X"
                lista_negra[int(respuesta[i])][lista[2]]="X"
            
    return lista_negra

def picas_cuando_hay_palas(subhistory, numeros, lista_negra, respuesta):
    indice1=[]
    for h in subhistory:
        if(h[1]!=0):
            if(h[2]==1):
                indice1.append(h) #GUARDA LOS HISTORIALES QUE TIENEN PICAS DIFERENTE DE 0 Y PALAS=1
    for i in range(4):
        if(len(indice1)!=0):
            if(respuesta[0] is not None or respuesta[1] is not None or respuesta[2] is not None or respuesta[3] is not None):
                if (respuesta[i] is not None):
                    for ind in indice1:
                        if(respuesta[i]==ind[0][i]): #SI LO QUE COOCEMOS ESTÁ EN EL INDICE Y EN LA MISMA POSICION LO QUE SABEMOS ES LA PALA
                            try1=ind[0]
                            try1=try1.replace(respuesta[i], 'X') 
                            for j in range(4):
                                if(try1[j] in numeros):
                                   lista_negra[int(try1[j])][j]="X"  #si sabemos cual es la pala sabemos que la otra es la pica y que por lo tanto ese numero no va ahi
                                   
                        elif(respuesta[i] in ind[0]): #SI LO QUE CONOCEMOS ESTA EN EL INDICE PERO NO EN LA MISMA POSICIÓN LO QUE SABEMOS ES LA PICA
                             try1=ind[0]
                             try1=try1.replace(respuesta[i], 'X')   
                             if(ind[1]==1):
                                 for j in range(4):
                                     if(try1[j] in numeros):
                                         respuesta[j]=try1[j]  #si sabemos cual es la pica sabemos que la otra es la pala asi que la ubicamos en la respuesta
    return [lista_negra, respuesta]

def picas_cuando_hay_palasv2(subhistory, numeros, lista_negra, respuesta): 
    indice1=[]
    A=respuesta[0] is not None
    B=respuesta[1] is not None
    C=respuesta[2] is not None
    D=respuesta[3] is not None
    
    for h in subhistory:
        if(h[1]!=0):
            if(h[2]==2):
                indice1.append(h) #GUARDA LOS HISTORIALES QUE TIENEN PICAS DIFERENTE DE 0 Y PALAS=2
    for i in range(4):
        for k in range(4):
            if(len(indice1)!=0):
                if((not A and (not B) and C and D) or (not A and B (not C) and D) or (not A and B and C and (not D)) or (A and (not B) and (not C) and D) or (A and (not B) and C and (not D)) or (A and B and (not C) and (not D))):
                    if (respuesta[i] is not None and respuesta[k] is not None):
                        if(respuesta[i]!=respuesta[k]): #si no evaluo la misma con la misma xd
                            for ind in indice1:
                                if(respuesta[i]==ind[0][i] and respuesta[k]==ind[0][k]): #SI LO QUE COOCEMOS ESTÁ EN EL INDICE Y EN LA MISMA POSICION LO QUE SABEMOS ES LA PALA
                                    try1=ind[0]
                                    try1=try1.replace(respuesta[k], 'X') 
                                    try1=try1.replace(respuesta[i], 'X') 
                                    for j in range(4):
                                        if(try1[j] in numeros):
                                           lista_negra[int(try1[j])][j]="X"  #si sabemos cual es la pala sabemos que la otra es la pica y que por lo tanto ese numero no va ahi                                       
                        
    return lista_negra


def encontrar_numero(history, numeros):
    Master_Num="0000"
    respuesta=[None, None, None, None]
    lista_negra=[]
    for i in range(10):
        lista_negra.append([None, None, None, None])  
    score=[]
    Try_Num=""
    subhistory=history
    p=[]
    #Revisar si con los analisis que tengo se puede encontrar el resultado
    
    for i in range(10):
        respuesta=encontrar_ubicacion_palas(subhistory, numeros, respuesta) 
        lista_negra=descatar_posiciones(subhistory, numeros,lista_negra)
        respuesta=posicioar_con_los_descartes(lista_negra,numeros, respuesta)
        respuesta=por_negacion(lista_negra,numeros, respuesta)
        lista_negra=ponerX_por_ubicar_un_numero(subhistory, numeros, lista_negra, respuesta)
        
        p=picas_cuando_hay_palas(subhistory, numeros, lista_negra, respuesta)
        lista_negra=p[0]
        respuesta=p[1]
        
        
    #si no se encuentra el resultado ir probando con numeros hasta dar con el o hasta tener suficiente informacion para que las funciones creadas sirvan
    while(respuesta[0] is None or respuesta[1] is None or respuesta[2] is None or respuesta[3] is None):
        randomlista=[0,1,2,3]
        lista=[5, 5, 5, 5]
        for i in range(4):
            if(respuesta[i] is not None):
                indi=numeros.index(respuesta[i])
                lista[i]=indi
                randomlista.remove(indi)
        
        newNumber=7 
        for i in range(4):
            b=0
            newNumber=random.choice(randomlista)
            while (newNumber in lista and b==0): #Si el numero ya estaba, repetir la eleccion
                newNumber=random.choice(randomlista)  
                if(5 not in lista):
                    b+=1
            #Cuando tenga un numero que no este repetido agregarlo a la lista
            if(lista[i]==5):
                lista[i]=newNumber

        Try_Num=numeros[lista[0]]+numeros[lista[1]]+numeros[lista[2]]+numeros[lista[3]] #Cambiar de posición los números para ver que pasa
        score=score_Picas_Palas(Master_Num,Try_Num)
        subhistory.append(score)
        for i in range(10):
            respuesta=encontrar_ubicacion_palas(subhistory, numeros, respuesta) 
            lista_negra=descatar_posiciones(subhistory, numeros,lista_negra)
            respuesta=posicioar_con_los_descartes(lista_negra,numeros, respuesta)
            respuesta=por_negacion(lista_negra,numeros, respuesta)
            lista_negra=ponerX_por_ubicar_un_numero(subhistory, numeros, lista_negra, respuesta)
            p=picas_cuando_hay_palas(subhistory, numeros, lista_negra, respuesta)
            lista_negra=p[0]
            respuesta=p[1]
 
    #CASO ESPECIAL - CUANDO SE ENCUENTRAN LOS CUATRO NUMEROS DE UNA VEZ - COLOR AZUL
    '''
    if (len(subhistory)==2):

        if(respuesta[0] is None): #si no se ubico ninguna pala quiere decir que hay 2 3 o 4 picas 
            
            Try_Num=numeros[2]+numeros[0]+numeros[3]+numeros[1] #Cambiar de posición los números para ver que pasa
            score=score_Picas_Palas(Master_Num,Try_Num)
            subhistory.append(score)
            respuesta=encontrar_ubicacion_palas(subhistory, numeros) #evaluar si se resolvio
            lista_negra=descatar_posiciones(subhistory, numeros)
            '''
    
    respuesta_final=""
    respuesta_final=respuesta_final.join(respuesta) #CONVIERTE LA LISTA DE LA RESPUESTA EN STRING
    return [respuesta_final, subhistory, lista_negra]
                        

######################################################
#INTERFAZ
########################################################
########################################################
# EL JUGADOR ADIVINA EL NUMERO / playerguess
def isplayerguessing():
    Master_Num=generate_Master_Number(4)
    print(Master_Num)
    #Este boton funciona asi solo para isplayerguessing
    def codigobotoncomprobar(): # al presionar el boton, se revisa la entrada del usuario
        global intentos
        intentos+=1
        Try_Num=Numero_user.get()
        Numero_user.delete(0, 'end') #Eliminar texto del entry 
        #print("Se obtuvo: ", Try_Num)
        score=score_Picas_Palas_v0(Master_Num,Try_Num)
        Numero=Label(playerguessframe2, text=score[0])
        Numero.grid(column=0, row=intentos+1)
        Picas=Label(playerguessframe2, text=score[1])
        Picas.grid(column=1, row=intentos+1)
        Palas=Label(playerguessframe2, text=score[2])
        Palas.grid(column=2, row=intentos+1)
        
        if Validar_Numero(Try_Num,4)==False: # si no es valido lo adiverte al usuario
            Numero.configure(bg="red")
            Picas.configure(bg="red",text="x")
            Palas.configure(bg="red",text="x")
            Label(playerguessframe2,text="Numero invalido").grid(column=3, row=intentos+1)
            return
            
        if score[2]==4: #Gano el juego
            Numero.configure(bg="green")
            Picas.configure(bg="green")
            Palas.configure(bg="green")
            Label(playerguessframe2,text="Correcto!").grid(column=3, row=intentos+1)
            Comprobarbutton.destroy()
            Rendirsebutton.destroy()
    
    def codigobotonrendirse(): #al presionar el boton, revela al usuario la respuesta y quita botnes
        global intentos
        intentos+=1
        score=score_Picas_Palas_v0(Master_Num,Master_Num)
        Numero=Label(playerguessframe2, text=Master_Num, bg="yellow")
        Numero.grid(column=0, row=intentos+1)
        Picas=Label(playerguessframe2, text=score[1], bg="yellow")
        Picas.grid(column=1, row=intentos+1)
        Palas=Label(playerguessframe2, text=score[2], bg="yellow")
        Palas.grid(column=2, row=intentos+1)
        Label(playerguessframe2,text="Respuesta").grid(column=3, row=intentos+1)
        Comprobarbutton.destroy()
        Rendirsebutton.destroy()
    def codigobotonresetear():
        playerguessMainframe.destroy()
        isplayerguessing()
        
        
    MenuFrame.destroy() #Quitar menu cuando se abra este modo de juego
    playerguessMainframe=Frame(raiz) #frame principal del juego
    playerguessMainframe.pack()
    
    playerguessframe=Frame(playerguessMainframe) # Creamos un frame

    #empaquetar en el frame del juego
    playerguessframe.pack(fill="x")

    #configurar el espacio del frame
    playerguessframe.config(bg="white", width=500,height=500) #la riz se adaptara al frame     

    #Entrada de texto
    Label(playerguessframe, text="Por favor ingrese un número de 4 cifras: ",bg="white").pack()
    #myLable.place(anchor=N)

    #Try_Num=StringVar()
    #Entrada del usuario
    Numero_user=Entry(playerguessframe,fg="red")
    Numero_user.pack()
    
    #Botones de juego
    Buttons=Frame(playerguessframe,bg="white",pady=5)
    Buttons.pack()
    
    #Numero_user.bind("<Return>",codigobotoncomprobar)    
    Comprobarbutton=Button(Buttons, text="Comprobar",command=codigobotoncomprobar)
    Comprobarbutton.grid(column=0, row=0)
    Rendirsebutton=Button(Buttons, text="Rendirse",command=codigobotonrendirse)
    Rendirsebutton.grid(column=1, row=0)
    Resetearbutton=Button(Buttons, text="Resetear",command=codigobotonresetear)
    Resetearbutton.grid(column=2, row=0)
    
    #####RESULTADO##########
    Label(playerguessframe, text="RESULTADO: ",bg="white").pack()

    # otro frame para los resultados
    playerguessframe2=Frame(playerguessMainframe)
    playerguessframe2.pack(fill="x")

    label=Label(playerguessframe2, text="Numero").grid(column=0, row=0)
    label=Label(playerguessframe2, text="Picas").grid(column=1, row=0)
    label=Label(playerguessframe2, text="Palas").grid(column=2, row=0)
    
    #Frame para botones finales
    playerguessframefinal=Frame(playerguessMainframe,bg="white", pady=5)
    playerguessframefinal.pack(fill="x")
    def goMenu():
        playerguessMainframe.destroy()
        menucreate()
        
    #Boton de regresar al menu    
    Button(playerguessframefinal,text="Menú Principal",command=goMenu).pack()


########################################################
# EL PC ADIVINA EL NUMERO
def ispcguessing():
    def goMenu():
        #var.set(1-var.get()) #para desatastacar el programa de el codigo score
        pcguessMainframe.destroy()
        menucreate()
        
    def codigobotonresetear():
        pcguessMainframe.destroy()
        ispcguessing()
        var.set(1-var.get()) #para desatastacar el programa de el codigo score
        #global intentos
        #intentos=0
        
    #Este codigo se ejecutara para cuando el pc adivine
    def empezarbutton():
        
        
        def addnumbers():
            global intentos
            
            global picas_global
            global palas_global
            
            var.set(1)
            intentos+=1
            
            picas_global=picasEntry.get()
            palas_global=palasEntry.get()
            Try_pic=picasEntry.get()
            Try_pal=palasEntry.get()
            
            picasEntry.delete(0, 'end') #Eliminar texto del entry 
            palasEntry.delete(0, 'end')
            
            print("Se obtuvo: Picas:", Try_pic, "Palas: ", Try_pal)
            
            #Modificar Linea anterior asi que #CREA UNA LINEA DE LABELS Y LAS UBICA DONDE VAN
            Numero=Label(tablaframe, text=Try_Num_global.get())
            Numero.grid(column=0, row=intentos)
            picas=Label(tablaframe, text=Try_pic)
            picas.grid(column=1, row=intentos)
            palas=Label(tablaframe, text=Try_pal)
            palas.grid(column=2, row=intentos)
            
            
            #MODIFICA LA LINEA DE TRABAJO         
            Numero=Label(tablaframe, textvariable=Try_Num_global)#Esta se crea
            Numero.grid(column=0, row=intentos+1) 
            picasEntry.grid(column=1, row=intentos + 1) #Las demas se modifican
            palasEntry.grid(column=2, row=intentos + 1)
            EnviarButton.grid(column=3, row=intentos + 1)
            
                   
            
            
        
        
        
        global Try_Num_global
        global var
        var = IntVar() #avisa a score cuando continuar
        global EnviarButton
        Try_Num_global=StringVar()
        terminadocheck=False
        
        
        
        global intentos
        intentos=0
        EmpezarButton.destroy() #eliminar el boton de empezar
        
        label=Label(tablaframe, text="Numero").grid(column=0, row=0)
        label=Label(tablaframe, text="Picas").grid(column=1, row=0)
        label=Label(tablaframe, text="Palas").grid(column=2, row=0)
        
        Numero=Label(tablaframe, textvariable=Try_Num_global)
        Numero.grid(column=0, row=1)
        picasEntry=Entry(tablaframe)
        picasEntry.grid(column=1, row=1)  
        palasEntry=Entry(tablaframe)
        palasEntry.grid(column=2, row=1)
        
        EnviarButton=Button(tablaframe,text="Enviar", command=lambda: [addnumbers(),var.set(1-var.get())])        
        EnviarButton.grid(column=3, row=1)
        
        ResetButton=Button(pcguessframe,text="Resetear",command=codigobotonresetear)
        ResetButton.pack()        
        
        
        numeros=encontrar_picas_palas("0000"); #llama a la funcion que encuentra las pepitas
        print("Ya se cuales son las pepitas: ", numeros[0])
        respuesta=encontrar_numero(numeros[2], numeros[0])
        print("ya se la respuesta: "+respuesta[0])
        
        terminadocheck=True
        
        #Numero.destroy() # No se por que esta linea no funciona
        picasEntry.destroy()
        palasEntry.destroy()
        EnviarButton.destroy()
        
        RespuestaLabel=Label(pcguessframe, text=("Respuesta: "+respuesta[0]) )        
        RespuestaLabel.pack()
        
        
        
        
        
    
    MenuFrame.destroy() #Quitar menu cuando se abra este modo de juego
    pcguessMainframe=Frame(raiz,bg="white") #frame principal del juego
    pcguessMainframe.pack(fill="x")
    
    pcguessframe=Frame(pcguessMainframe) # Creamos un frame

    #empaquetar en el frame del juego
    pcguessframe.pack(fill="x")

    #configurar el espacio del frame
    pcguessframe.config(bg="white", width=500,height=500) #la riz se adaptara al frame     

    #Entrada de texto
    Label(pcguessframe, text="Piensa en un numero de 4 cifras diferentes. intentare adivinarlo",bg="white").pack()
    
        
    EmpezarButton=Button(pcguessframe,text="Empezar",command=empezarbutton)    
    EmpezarButton.pack()
    tablaframe=Frame(pcguessframe)
    tablaframe.pack(fill="x")
    MenuButton=Button(pcguessframe,text="Menú Principal",command=goMenu)
    MenuButton.pack()
    
    
    
######################################################## 
# MENU PRINCIPAL

def menucreate():
    global MenuFrame
    MenuFrame=Frame(raiz)
    MenuFrame.pack(fill="x")
    Button(MenuFrame, text="Player guess the Number",command=isplayerguessing).pack()
    Button(MenuFrame, text="PC guess the Number",command=ispcguessing).pack()
    

intentos=0                  
#Master_Num="1234"
raiz=Tk()
raiz.title("Picas y Palas - El juego")
#raiz.resizable(0,0) #impiide cambiar el tamaño 
#raiz.geometry("500x500")
raiz.iconbitmap("imagenes/logo.ico") #logo de arriba a la izquierda 
raiz.config(bg="white")
myLable=Label(raiz, text="PICAS Y PALAS",font=(18),bg="white")
myLable.pack(fill="x")


menucreate()




raiz.mainloop()