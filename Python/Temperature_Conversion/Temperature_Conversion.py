""" TEMPERATURE CONVERSION """

#to convert from one scale to another
def convert(f_scale, temp, to_scale):
    converted = temp
    degree = ""

    # from celsius 
    if(f_scale == 1):
        degree = "°C"
        #to Fahrenheit
        if(to_scale == 2):
            converted = 9.0/5.0 * temp + 32
            degree = "°F"
        #to Kelvin
        if(to_scale == 3):
            converted += 273.15
            degree = "K"

    #from Fahrenheit
    elif f_scale == 2:
        degree = "°F"
        if(to_scale != 2):
            #to celsius
            converted = (temp-32)*5.0/9.0
            degree = "°C"
            #to kelvin
            if(to_scale == 3):
                converted += 273.15
                degree = "K"

    #from Kelvin
    else:
        degree = "K"
        if(to_scale != 3):
            #to Celsius
            converted -= 273.15
            degree = "°C"
            #to Fahrenheit
            if(to_scale == 2):
                converted = 9.0/5.0 * converted + 32
                degree = "°F"
    return str(converted)+degree

#driver code
def main():
    print("Convert from:")
    print("Choose a scale:\n1.Celsius\n2.Fahrenheit\n3.Kelvin")
    from_scale = int(input())
    temperature = float(input("\nEnter the temperature: "))
    print("Convert to:")
    print("Choose a scale:\n1.Celsius\n2.Fahrenheit\n3.Kelvin")
    to_scale = int(input())
    res=convert(from_scale, temperature, to_scale)
    print(res)

if __name__ == '__main__':
    main()
