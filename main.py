#Logica con python

#edad=int(input("Digita tu edad: "))

#print(edad)

#CONDICION logica simple

bandera=True
#if(edad>=18 and bandera==True):

    #print("Bienvenido a la chismosa")

#else:    
    #print("Devolvete por favor")



#Ejemplo 1- Hidroituango

'''nivelDeAgua=float(input("Digita el nivel de agua: "))

if(nivelDeAgua>0 and nivelDeAgua<200):
    print("La represe tiene poca agua")

elif(nivelDeAgua>= 200 and nivelDeAgua<450 ):
    print("la represa esta estable")     

elif(nivelDeAgua>=450):
    print("Cuidado,abra compuertas")

else:
    print("Digito un nivel invalido") '''


#Ejemplo 2 - estaciones

'''mes=input(" Digite el mes:  ").lower()
if(mes== "enero" or mes== "febrero" or mes== "marzo" ):
    print(" Estas en invierno")
elif(mes== "abril" or mes== "mayo" or  mes=="junio"):
    print(" Estas en Verano") 
elif(mes== "julio" or mes== "agosoto" or mes=="septiembre"):  
    print("Estas en Otoño")
elif(mes== "octubre" or mes=="noviembre" or mes=="diciembre"):
    print("Estas en Primavera")    

else:
    print(" ERROR!!! Digitaste mal el mes")   '''

 #Ejemplo 3- Años

'''while(True):

        edad=float(input(" Digite su edad: ")) 

        if(edad>=0 and edad<=14):
            print("Eres un niño")
        elif(edad>14 and edad<=28):
            print("Eres joven") 
        elif(edad>28 and edad<60):
            print("Eres Adulto")    
        elif(edad>=60):
            print("Eres adulto mayor")    
        else:
             print("Error!! Ingresa un número valido")'''

#Ejemplo 4- Operador Ternario 

#parametro=True

#Operador original

'''if(parametro==True):
    print("El parametro es verdadero")
else:
    print("El parametro es falso") ''' 

#Operador ternario  

'''print("El parametro es verdadero") if parametro==True else print("El parametro es falso")

#Ejemplo 2 de operador ternario

estaLloviendo=False

print("¿Está lloviendo?") if estaLloviendo==True else print("No está lloviendo")'''


