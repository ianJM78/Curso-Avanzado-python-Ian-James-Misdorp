
"""
Ejercicio 6: Gestión de Inventario
Crea una función que actualice el inventario de una tienda.
Requisitos:
La función debe recibir un diccionario representando el inventario y una lista de productos vendidos.
Debe actualizar las cantidades en el inventario y retornar el inventario actualizado.
Incluye en el docstring un ejemplo de entrada y salida.
    
"""




def Gestion(inventory : dict[str,int], sold : list[str]) -> dict[str,int]:
    """
    Function that receives a dictionary with the store's inventory and a list of sold items.

    Args:
        inventory (dict[str, int]):  Dictionary containing the store's inventory.
        sold (list[str]):  List of sold items.

    Returns:
        inventory (dict[str, int]):  Dictionary with the updated inventory.
    
    """
    
    for element in sold:
        if element not in inventory.keys():
            print(f"The element {element} isn't in stock")
        elif inventory[element] < 1:
            print(f"The stock for {element} has run out")
        else:
            inventory[element] -= 1

    return inventory








#? MAIN

# Example cases
inventory = {"apples": 10, "bananas": 0, "oranges": 5}
sold = ["apples", "bananas", "grapes", "apples", "oranges"]

updated_inventory = Gestion(inventory, sold)
print(updated_inventory)  

