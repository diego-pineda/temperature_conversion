def celsius_to_fahrenheit(celsius):
    """Celsius

    Args:
        Celsius (float): temperature in degrees celsius

    Returns:
        float: temperature in degrees Fahrenheit
        """
    fahrenheit = celsius/4*9 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    """Celsius

    Args:
        Celsius (float): temperature in degrees Celsius

    Returns:
        float: temperature in degrees Kelvin
    """
    K = celsius + 273.15
    return K

k=celsius_to_kelvin(24)
print(k)