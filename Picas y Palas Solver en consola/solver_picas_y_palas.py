
"""
Created on Mon Oct 10 21:19:41 2022

@author: Jennifer 
"""

from nucleos import score_Picas_Palas
from nucleos import generate_Master_Number
#import math
import random
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


def encontrar_numero(history, numeros, Master_Num):
    
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
                        
#################################################################
#               MAIN

##################################################################

Master_Num=generate_Master_Number(4)
numeros=encontrar_picas_palas(Master_Num)
respuesta=encontrar_numero(numeros[2], numeros[0],Master_Num)
print("--------FINAL-------")
print("Respuesta:",respuesta[0])
print("Numero de pasos: ",len(respuesta[1]))
#print(respuesta[1])
#print("Lista negra:", respuesta[2]) 


'''
TodosNumeros=[]
Master_Num="8510"
TodosNumeros.append(Master_Num)
#Encontrado=encontrar_picas_palas(Master_Num)
Nopudo=[]
subhistory=[]
for i in range(5039):
    Master_Num=generate_Master_Number(4)
    while (Master_Num in TodosNumeros): 
        Master_Num=generate_Master_Number(4) 
    TodosNumeros.append(Master_Num)  


pasos=[]
for Master in TodosNumeros:
    #print(Master) 
    
    numeros=encontrar_picas_palas(Master)
    respuesta=encontrar_numero(numeros[2], numeros[0],Master)
    p=[Master,len(respuesta[1])]
    pasos.append(p)
    #print("Real: ",Master) 
    #mprint("Respuesta: ", respuesta[0],"\n")
    if (respuesta[0]==""):
        print("Real: ",Master)        
        print("No pudo resolver. Elemento vacio")
        break
        
    if (respuesta[0]!= Master): #Revisa la respuest es igual al Master
        Nopudo.append(Master)
        print("Real: ",Master)
        print("Respuesta: ", respuesta[0])
        print("No pudo resolver","\n") 

print(len(pasos))
'''

    

#pruebas del solver

'''
    Master_Num="1453"
    #Master_Num="9850"
    numeros=encontrar_picas_palas(Master_Num)
    respuesta=encontrar_numero(numeros[2], numeros[0])
    print("--------FINAL-------")
    print("Real: ",Master_Num)
    print("Historial:",numeros[2])
    print("Respuesta:",respuesta[0])
    print("Numero de pasos: ",len(respuesta[1]))
    #print("Lista negra:", respuesta[2])
    
    
    
    #se usa para probar algunas cosas xd

    picas_dif_0=0
    for Master in TodosNumeros:   
         encontrado=encontrar_picas_palas(Master) 
         subhistory=encontrado[2]
         b=0
         c=0
         for h in subhistory:
             tamaño=len(subhistory)
             if(h[1]==0):
                 if(h[2]==0):
                     b+=1
                 else:
                     c+=1
         if(c>0):
             picas_dif_0+=1
             print(Master)
             
    print("Picas diferentes a 0",picas_dif_0)  
'''


#       Este codigo se uso para testear que encontrara las pepitas sin errores


     



    
