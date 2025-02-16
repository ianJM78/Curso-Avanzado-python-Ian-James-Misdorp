import math



"""
Ejercicio 5: Generador de Números Primos
Escribe una función que genere una lista de números primos hasta un número dado.
Requisitos:
La función debe recibir un número entero positivo.
Debe retornar una lista con todos los números primos hasta ese número.
Incluye en el docstring una explicación sobre qué es un número primo.

"""



def allPrimes(n : int) -> list[int]:
    """
    Gets all prime numbers up to "n"


    Args:
        n (int): The upper limit of which to find primes

    Returns:
        list[int]: a list of all primes up to the "n"
    """

    primesList = list()
    
    for x in range(2,n):
        flag = True
        for y in range(2,int(math.sqrt(x) + 1)):  # By definition, we check if it's divisible up to the largest number that squared is smaller than the n range
            if x % y == 0:
                flag = False
                break
        if flag is True:
            primesList.append(x)
    
    return primesList




#? MAIN


#Get the upper limit and ensure its a integer
while True:
    user_input = input("Input the desired upper limit to find all primes: ")
    try:
        user_input = int(user_input)
        break
    except ValueError:
        print("Number must be an integer")

prime_list = allPrimes(user_input)
print(prime_list)


