# Function that takes either a celsius or fahrenheit temperature and converts it to the other temperature scale.

def convert_temperature(temperature, scale):
    if scale == 'c':
        return (temperature - 32) * 5/9
    elif scale == 'f':
        return (temperature * 9/5) + 32
    else:
        return "Invalid scale. Please enter either 'c' or 'f'."