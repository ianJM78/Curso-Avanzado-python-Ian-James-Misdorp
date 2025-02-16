

# Seria mas facil si se usaria el equivalente a un "stuct" o @dataclass para almacenar cada entrada la cual tendria el valor y el tipo. Esto permitiria que se puean tenes "keys" iguales sin que se sobreescriban


def Converter(temp_dict : dict[int , str]) -> dict[float , str]:
    """
    Packs inputs into a dictionary and depending on the type of temperature, applies a transformation, then adds it to a dictionary

    Parameters:
    kwargs[int , str] a dictionary of pair of int and str

    Returns:
        dict[flaot , str]: a dictionary with the converted values
    """
    convertedValues = dict()

    for temperature,tempType in temp_dict.items():

        if  tempType.upper() == "FAHRENHEIT":
            function = lambda t : (t - 32) * (5/9)
            convertedValues[ function(temperature)] = "CELSIUS"
        
        else:
            function = lambda t : (t * (9/5)) + 32
            convertedValues[ function(temperature)] = "FAHRENHEIT"
    
    return convertedValues





#? Main 

test_data = {
    100: "FAHRENHEIT",  # Should convert to 37.78°C
    0: "CELSIUS",       # Should convert to 32°F
    -40: "FAHRENHEIT",  # Should convert to -40°C (same value)
    25: "CELSIUS"       # Should convert to 77°F
}

result = Converter(test_data)  

print(result)



