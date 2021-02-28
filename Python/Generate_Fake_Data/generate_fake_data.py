from faker import Faker
import numpy as np
country = {'English': "en_US", 'Hindi': "hi_IN"}


def show_methods():
    print("These are the types of random data you can generate: \n")
    methods = list(fake.__dict__.keys())
    for met in methods:
        print(met)
    return methods


if __name__ == '__main__':
    coun = input(
        "Select the language of data you want English(0) or Hindi(anything other than 0)")
    if(coun == '0'):
        fake = Faker(country['English'])
    else:
        fake = Faker(country['Hindi'])

    method = show_methods()
    cols = []

    while True:
        col_name = input(
            "Enter the type of data in the same as shown above \n")
        if col_name not in method:
            print("No such data type available \n")
        else:
            cols.append(col_name)
        contd = input(
            "Do you want more types of data? press 1 for yes and anything for no \n")
        if contd != '1':
            break
    struct = []
    for i in range(len(cols)):
        struct.append([])
    if len(col_name) == 0:
        print("Sorry no data type available \n")
    else:
        n = int(input("Enter the number of rows you want \n"))
        for _ in range(n):
            for i in range(len(cols)):
                struct[i].append(getattr(fake, str(cols[i]))())
        arr = np.array(struct)
        print("Congrate Data has been generated \n")
        filename = input("Enter the name of the file \n")
        np.savez(filename)
        print("Done Succesfully")
