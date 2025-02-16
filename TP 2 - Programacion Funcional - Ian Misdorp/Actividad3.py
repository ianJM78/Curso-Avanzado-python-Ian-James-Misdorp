
"""
Ejercicio 3: Verificación de Palíndromos
Escribe una función que determine si una palabra o frase es un palíndromo.
Requisitos:
La función debe recibir una cadena de texto.
Debe retornar
True
si es un palíndromo y
False
en caso contrario.

"""






def palindrome_cheque(word : str) -> bool:
    """
    Cheques to see if the string is a palindrome or

    Args:
        word (str): The string to be chequed

    Returns:
        bool: Depending if the string is a palindrome or not
    """

    word = word.lower() # to avoid cases where the letters at mirrored length from the middle are the same, but one is uppercase and the other lowercase
    word = word.replace(" ","") #Removes all spaces between words, to avoid them unintentionaly messing up the function results

    # Set the left and right pointers
    i= 0
    j = len(word) - 1

    while i <= j:  # While they are not on the same letter (the <= avoids the pointers missing eachother )
        
        # If the the word mirrored over the middle is different, then its not a palindrome
        if word[i] != word[j]:
            return False
        
        #Move the pointer one closer to the middle
        i += 1
        j -= 1
    
    return True  #If we get to the end of the loop, it's a palindrome





#? MAIN

word = input("Enter the word you wish to cheque is a palindrome or not: ")

if palindrome_cheque(word):
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} isn't a palindrome")


