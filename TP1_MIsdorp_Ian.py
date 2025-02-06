import random



# Los sets al ser mutables no es necesario hacer return, ya que se pasa una referencia al objeto y se modifica el original.
def randomSet(my_set,n,a,b):
    if (b-a + 1) < n:  # Se agrega uno ya que se incluye "a" cuando se genern los numeros
        print("Rango elegido no puede generar n numeros distintos")
        return
    
    #Usamos el while con el len ya que es posible que se generen 2 numeros iguales, por lo que uno seria eliminado, y terminariamos con un my_set con menos de n elementos
    while len(my_set) < n:
        my_set.add(random.randint(a,b))

#Llena una lista con n elementos entre a y b
def randomList(myList,n,a,b):
    while n > 0:
        myList.append(random.randint(a,b))
        n -= 1

# para este problema se usara un bubble sort optimizado para que se vaya recorriendo -1 elemento por cada pasada



# Las listas al ser mutables, se pasan por referencia, por lo que no es necesario hacer un return
def bubblesort(lista):

    size = len(lista)

    # Loop externo
    for i in range(0, size - 1):

        swapped = False
        # Loop interno
        for j in range(0 , size-i-1):
            # Compara si el siguiente es menor a el actual
            if (lista[j] > lista[j+1]):
                # Corrige
                temp = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temp
                swapped = True
                # En la siguiente pasada, se vuelve al elemento que se empezo originalmente si este se cambio, sino se sigue con el siguiente que no se cambio.
        if not swapped:
            break
            

#Crea un programa que permita crear un conjunto desde cero y despues me permitaeliminar un elemento de un conjunto si está presente en el conjunto.
def add_to_set(s):
    
    value = input("Ingresar elemento al set: ")
    s.add(value) # Se agrega el valor

    while(True):
        l = input("Desea ingresar otro valor? 0.No  |")
        transformed = int(l)

        if(transformed == 0):
            break
        elif(transformed == 1):
            value = input("Ingresar elemento al set: ")
            s.add(value) # Se agrega el valor
        else:
            print("Respuesta Invalida")

def removeValue(s,removeValue):
    try:
        s.remove(removeValue)
    except KeyError:
        print(f"El elemento {removeValue} no se encuentra en el set")


def difference_in_sets(set1,set2):

    # Se puede usando   newSet = set1.difference(set2)
    newSet = set1 - set2  #? Crea un set con los elementos en el set1 que no se encuentren en el set 2

    return newSet



# Debido a que un set elimina todo los elementos repetidos, es posible pasarlos todos a un set y luego devuelta a una lista
def dteDupes(lista):
    mySet = set()
    
    #? Una forma de copiar lista a set sin usar metodo
    # for i in range(len(lista)):
    #     mySet.add(lista[i])

    mySet.update(lista) #Se actualiza el set con los elementos de la lista.
    #? Si se desea agregar la lista y no los elementos, se la debe transformar a una Tupla
    
    lista.clear() #Se vacia la lista
    for x in mySet:  # Se usa este tipo de loop ya que en un set los elementos no tienen orden, por lo que no se los pueden acceder por indice
        lista.append(x)


def esPar(numero):
    if (numero % 2) != 0 :
        return False
    return True


def factorial(numero):
    if numero == 1:  #Caso base, se deja de llenar el stack de recursividad con funciones parciales y se lo empieza a vaciar
        return 1
    else:
        return numero * factorial(numero - 1)
     
    #Dado que 1 no es par, no se requiere agregarlo como caso extra que no entra en recursividad.
    

def dupeCounter(myList,x):
    counter = 0
    for i in range(len(myList)):
        if myList[i] == x:
            counter += 1
    return counter

def sumaRecursiva(number):
    if number == 0 :
        return 0
    else:
        return number + sumaRecursiva(number - 1)
    
        
    

#Main---------------------------------------------------------------------------------------------------------------------------------------------------------

#Actividad 1
#1.Crea una función que reciba una lista de números y la ordene de menor a mayor. La función debe devolver la lista ordenada.

# l = [24, 5, 45, 75, 8, 20, 100, 75, 37, 15]
# print(f"Lista sin ordenar {l}")
# bubblesort(l)
# print(f"Lista despues de ordenar {l}")

# #?Actividad 2
# s = set()
# add_to_set(s)

# r = input("Ingresar numero a remover: ")
# removeValue(s,r)

# while True:
#     l = input("Desea remover otro valor?  1.Si | 0.No")
#     transformed = int(l)
#     if(transformed == 0):
#         break
#     elif(transformed == 1):
#         r = input("Ingresar numero a remover: ")
#         removeValue(s,r)
#     else:
#         print("Respuesta invalida")

#? Actividdad 3
#Dados dos conjuntos de números, escribe un programa para encontrar los números que faltan en el segundo conjunto en comparación con el primero y viceversa.


#Creo dos set vacios usando los constructores de la clase
# setA = set()
# setB = set()


# # lleno las listas usando la libreria random
# randomSet(setA,10,0,20)
# randomSet(setB,10,0,20)
# print(f"Set 1 : {setA} \n\nSet 2 : {setB} ")


# while True:
#     choice = input("De cual lista desea encontrar los valores que no se encuentran en la segunda?\n1.set A \n2. set B\n...:")
    
#     if choice.isdigit(): #Si es un digito int
#         choice = int(choice)
#         if choice == 1 :
#             final = difference_in_sets(setA,setB)
#             print(f"La differencia entre los sets A - B es:\n{final}")
#             break
#         elif choice == 2 :
#             final = difference_in_sets(setB,setA)
#             print(f"La differencia entre los sets B - A es:\n{final}")
#             break

#     print("Respuesta invalida, ingresar nuevamente\n")


# #! Actividad 4
# #Escriba un programa en Python para eliminar todos los duplicados de una lista de cadenas dada y devolver una lista de cadenas únicas.

# myList = []

# for i in range(20):
#     myList.append(random.randint(0,15))

# print(f"{myList} \n")
# dteDupes(myList)
# print((f"{myList}\n"))


# #! Actividad 5

# #Crea una función llamada factorial que reciba un número entero positivo y devuelva su factorial. Ejemplo: factorial(4) debe devolver 24.

# while True:
#     choice = input("Ingresar un numero par para poder tomar su factorial\n")

#     if choice.isdigit():

#         choice = int(choice)
#         flag = esPar(choice)

#         if flag:
#             number = factorial(choice)
#             print(f"El factorial del numero {choice} es: {number}")
#             break
#         else:
#             print("Numero ingresado no es par, porfavor intentar devuelta")
    
#     else:  # Si no es un digito(int)
#         print("Entrada invalida, porfavor ingresar un numero valido\n")

#!ACtividad 6

#Crea una función llamada contar_ocurrencias que reciba una lista y un elemento, y devuelva cuántas veces aparece ese elemento en la lista.

# lista = []
# randomList(lista,10,0,20)

# while True:
#     choice = input("Ingresar un numero par para poder tomar su factorial\n")

#     if choice.isdigit():
#         choice = int(choice)
#         counter = dupeCounter(lista,choice)
#         print(f"El numero {choice} aparece {counter} veces en la lista\n")

#     else:
#         print("Entrada invalida, ingresar nuevamente\n")

#! Actividad 7

#Crea una función recursiva llamada suma_recursiva que reciba un número n y devuelva la suma de los primeros n números naturales.


while True:

    choice = input("Ingrese el numero entero positivo \n")

    if choice.isdigit():

        
        choice = int(choice)
        if choice > 0:   #Si es positivo

            suma = sumaRecursiva(choice)
            print(f"La suma de los primeros {choice} numeros naturales es: {suma}\n")
            break
        else:
            
            print("Ingreso invalido, porfavor ingresar un numero positivo\n")
    else:
        print(f"Ingreso invalido. ingresar un entero positivo\n")













