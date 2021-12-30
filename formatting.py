'''fmtFloat:
    Format a floating point number and return a string
    Parameters:
        floatV - Floating point number to be formatted
        places - Number of decimal places (default: 2)

    returns a string from the floating point value rounded to the number
    of deficmal places
'''
def fmtFloat(floatV, places=2):
    return str(round(floatV, places))

'''fmtTemp:
    Return the temperature in degrees Celcius or Farenheit as a formatted string
    Paramteters:
        temp - Temperature as a floating point value
        units - C for Celcius or F for Farenheit (not case sensitive; default:'c')
'''
def fmtTemp(temp, units='c'):
    if units.lower() != 'c':
        units = 'F'
        temp = temp * (9/5) + 32

    return fmtFloat(temp, 2) + ' ' + units
