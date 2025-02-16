
"""
Ejercicio 1: Calculadora de Descuentos
Crea una función que calcule el precio final de un producto después de aplicar un descuento.
Requisitos:
La función debe recibir el precio original y el porcentaje de descuento.
Debe retornar el precio final después del descuento.
Incluye un docstring que describa la función, sus parámetros y el valor de retorno.

"""



#TODO: Queria poder pasar el numero como parametro, y que devuelva un error que se podia tratar fuera de la funcion, pero para ello es necesario la creacion de una clase para manejar un error, lo cual no termino de entender

def get_number(): # -> int or float
    """
    Ensure that the input is either an integer or a float.

    Returns:
    int, float: Depending on the input.
    """

    while True:
        number = input("Value:")
        try:
            number = int(number) #Se intenta convertir a un int primero
            return number
        except ValueError: #En el caso de no serlo, se prueba si es un float
            
            try:
                number = float(number)
                return number
            except ValueError:
                print("El input no es un int ni un float. Porfavor ingrese un numero valido\n")


def discount(a,b): # -> float or int
    """
    Takes the amount and the discount precentage and applies the discount

    Args:
        a (int , float): Amount 
        b (int , float): discount percentage
    
    Returns:
        int , float: The resulting amount after the discount
    """
    return  a - (a * (b/100))



#? MAIN


# Se consigue el monto
print("Input the desiered amount")
amount = abs(get_number())   # Se transforma a positivo.

# Se consigue el porcentaje del descuento
while True:
    print("Input the desiered discount percentage to be applied.")
    percentage = get_number()
    if (percentage < 0) or (percentage > 100):
        print("Invalid amount, the percentage must be between 0 and 100\n")
    else:
        break

print(f"Amount: {amount} \nPercentage: {percentage}")

print(f"The value after the discount is {discount(amount,percentage)}")









