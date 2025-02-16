




def charCounter(string : str) -> dict[str , int]:
    """
    Creates a dictionary with the character count of the given string.

    Args:
        string (str): The line of text to analyze.

    Returns:
        dict[str, int]: Dictionary with {character: count}.
    """

    # Modify the string to avoid edge cases
    string = string.lower()
    string = string.replace(" ","")

    #create the dictionary
    dictionary = dict()

    for char in string:
        if char in dictionary.keys(): # .keys() returns an iterable with all the keys in the dictionary
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    return dictionary



#? MAIN

string = input("Enter the text you wish to performe a char count on: ")

final_dict = charCounter(string)

print(final_dict)   