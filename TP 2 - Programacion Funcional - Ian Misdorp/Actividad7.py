



"""
Ejercicio 7: Validación de Contraseñas
Escriba un programa de Python para convertir una lista de string en una nueva lista con listas de caracteres utilizando map.
Requisitos:
input : ["hola","adios"]output: [["h","o","l","a"] , ["a","d","i","o","s"]]

"""


def char_list(word : str) -> list[str]:
    """
    Function that receives a word and returns a list with each character of the word.

    Args:
        word (str): Word to be converted to a list of characters.

    Returns:
        list[str]: List with each character of the word.
    """
    
    lista = list()

    for i in range(len(word)):
        lista.append(word[i])
    return lista



#? Main

words = ["apple", "banana", "cherry", "orange", "grape", "strawberry", "blueberry", "kiwi", "mango", "pineapple"]

while True:
    choice = input("Do you want to enter a word? (y/n): ")
    choice = choice.lower()
    if choice == "y":
        word = input("Enter a word: ")
        words.append(word)
    elif choice == "n":
        break
    else:
        print("Invalid input, try again.")


list_of_lists = list(map(char_list,words)) # We apply the function to every element in the list, and create a list out of the iterable of the map function, that contains lists of chars.