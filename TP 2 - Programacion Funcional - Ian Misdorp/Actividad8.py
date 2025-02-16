

"""
Ejercicio 8: Cálculo de Estadísticas
Crea una función que calcule la media, mediana y moda de una lista de números.
Requisitos:
La función debe recibir una lista de números.
Debe retornar un diccionario con la media, mediana y moda.
Incluye en el docstring una explicación de cada estadística y un ejemplo de uso.
Trabajo
"""

def bubblesort(lista : list[int]) -> None:
    """
    Sorts a list of integers using the bubble sort algorithm.

    Args:
        lista (list[int]): A list of integers to be sorted.

    Returns:
        None: Modified by reference
    """

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



def Mean_Median_Mode(numberSet : list[int]) -> dict[str,float]:

    """
    Calculates the mean, median, and mode of a given list of integers.

    Args:
        numberSet (list[int]): A list of integers for which to calculate the mean, median, and mode.

    Returns:
        dict[str, float]: A dictionary containing the following:
            - "mean": The average of the numbers in the list (float).
            - "median": The middle value of the sorted list. If the list has an even number of elements, the average of the two middle numbers is returned (float).
            - "mode": The most frequent number in the list. If there are multiple modes, it returns the first one found (int).
    
    """

    number_count = dict()  # Used to find the Mode of the list
    counter = 0

    for i in range(len(numberSet)):
        if numberSet[i] in number_count.keys():
            number_count[numberSet[i]] += 1
        else:
            number_count[numberSet[i]] = 1

        counter += numberSet[i] # User for calculating the mean or average
    
    Average = (counter / len(numberSet))

    #Used to get the Mode using the dictionary we got
    max_value = 0
    mode_value = None
    for key, value in number_count.items():
        if value > max_value:
            max_value = value
            mode_value = key


    bubblesort(numberSet)  # We do a bubblesort to be able to calculate the Median
    lenght = len(numberSet)
    if lenght % 2 == 0:  # Even number of elements
        median_value = (numberSet[lenght//2 - 1] + numberSet[lenght//2]) / 2   #? Lo saque del chat, trate de usar abs() +-1, pero dependiendo de el decimal, tiraba para arriba o abajo y no funcionaba
    else:  # Odd number of elements
        median_value = numberSet[lenght//2]

    final_dict = {"Mean" : Average , "Mode" : mode_value , "Median" : median_value}

    return final_dict



#? MAIN

numbers = [10, 20, 20, 30, 30, 30, 40, 50, 50]
print(Mean_Median_Mode(numbers)) 

