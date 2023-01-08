from nucleos import *

from solver_picas_y_palas import encontrar_picas_palas
                    
#################################################################
#               MAIN
n=4; #El numero de decimales con el que se va jugar
TodosNumeros=[]
Master_Num="8510"
TodosNumeros.append(Master_Num)
#Encontrado=encontrar_picas_palas(Master_Num)
Nopudo=[]
for i in range(5039):
    Master_Num=generate_Master_Number(4)
    while (Master_Num in TodosNumeros): 
        Master_Num=generate_Master_Number(4) 
    TodosNumeros.append(Master_Num)    

for Master in TodosNumeros:
    #print(Master)     
    encontrado=encontrar_picas_palas(Master)
    #print("Real: ",Master) 
    #print("Encontrado: ", encontrado)   
    if (encontrado[0]==""):
        print("Real: ",Master)        
        print("No pudo resolver. Elemento vacio")
        break
        
        
    for number in encontrado[0]: #barre cada numero dado
        if number not in Master: #Revisa si esta en el Master
            if(Master not in Nopudo):
                Nopudo.append(Master)
            
            print("Real: ",Master)
            print("Resuelto por: ", encontrado[1])
            print("No pudo resolver")     

print(Nopudo)   

print("Se ejecuto el verificador sin errores")  



    
