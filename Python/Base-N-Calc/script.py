# Base-N Calculator

def Con_Base_X_to_Dec(num, base_x):
    # Converting the integeral part
    # Extract integerals in reverse order
    integeral_part = str(int(num))[::-1]
    i=0
    res = 0
    for number in integeral_part:
        # Convert each number to decimal
        element = int(number) * (base_x**i)
        # Add element to result
        res += element
        i+=1

    # Converting the decimal part
    decimal_part = str(num)
    # Extract decimal part using string manipulation
    decimal_part = decimal_part[decimal_part.index(".")+1:]
    i = -1
    for decimal in decimal_part:
        # Convert each number to decimal
        element = int(decimal) * (base_x**i)
        # Add element to result
        res += element
        i += -1

    # Return total result
    return res


def Con_Dec_to_Base_Y(num, base_y):
    # Converting the integeral part
    integeral_part = int(num)
    res_int = []
    while int(integeral_part) != 0:
        # Divide number by base
        integeral_part = integeral_part / base_y
        # Get the remainder
        element = (integeral_part - int(integeral_part)) * base_y
        # Append element
        res_int.append(str(int(element)))
    # Numbers are arranged from LCM to HCM
    res_int = res_int[::-1]

    # Converting the decimal part
    decimal_part = num - int(num)
    res_dec = []
    while (decimal_part != 0):
        # Multiply decimal part by base
        decimal_part = (decimal_part - int(decimal_part)) * base_y
        # Check if not duplicated, for no infinite loops
        if str(int(decimal_part)) in res_dec:
            break
        # Append element
        res_dec.append(str(int(decimal_part)))

    # Organize result
    if len(res_dec) == 0:
        # If result has decimal numbers
        res = res_int
    else:
        # If not
        res = res_int + ["."] + res_dec

    # Return grouped result
    return " ".join(res)


def main():
    num = input("Enter Number > ")
    base_x = input("Enter Base-X > ")
    base_y = input("Enter Base-y > ")
    # <----- Validation ----->
    # Validate Number
    try:
        num = float(num)
    except:
        print("Invalid Input/s\n")
        main()
    # Validate Base X
    try:
        base_x = int(base_x)
    except:
        print("Invalid Input/s\n")
        main()
    # Validate Base Y
    try:
        base_y = int(base_y)
    except:
        print("Invalid Input/s\n")
        main()
    # If same bases are entered
    if base_x == base_y or base_x<2 or base_y<2:
        print("Invalid Input/s\n")
        main()
        return
    # <----- check base x value ----->
    if base_x == 10:
        Result = Con_Dec_to_Base_Y(num, base_y)
    if base_y == 10:
        Result = Con_Base_X_to_Dec(num, base_x)
    else:
        Result = Con_Base_X_to_Dec(num, base_x)
        Result = Con_Dec_to_Base_Y(Result, base_y)

    print("\nResult: {}\n".format(Result))
    main()


# Start Checkpoint
if __name__ == "__main__":
    main()
