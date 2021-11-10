# imports
import sys
import os
import requests as rq

# stores the available subdomains
available_subdomains = []


def readTextFile(textFilename):
    """This function is used to read all the subdomains from file"""
    global available_subdomains

    inputFile = open(os.path.join(sys.path[0], textFilename), "r")
    available_subdomains = inputFile.read().splitlines()

    inputFile.close()\
    
def findSubdomains(userDomain, available_subdomains, size):
    """This function is used to find possible subdomains"""
    subdomains = []
    for i, subdomain in enumerate(available_subdomains):
        # generate a url with the current subdomain
        url = f"https://{subdomain}.{userDomain}"
        try:
            # try to connect with the url
            rq.get(url)
        except rq.ConnectionError:
            # an error occured
            print(".", end=" ")
            pass
        else:
            # the url returned a response i.e. it can be used
            subdomains.append(subdomain)
            print("+", end=" ")

        if i + 1 == size:
            break

    return subdomains


def writeTextFile(possibleSubdomains):
    """This function is used to write the possible subdomain in output.txt file"""
    # open a new file to write the corrected text
    outputFile = open(os.path.join(sys.path[0], "output.csv"), "w")

    # this writes text to the new output.txt file
    outputFile.write("\n".join(possibleSubdomains))

    outputFile.close()


def main():
    """This is the main function"""

    print("--------------------------------------------------")
    print("Subdomain Finder Program.")
    print("--------------------------------------------------")

    userDomain = input("Enter your domain: ")

    print("\nCheck for ____ subdomains. [Max size: 1000]")

    size = int(input("Enter size: "))

    if size > 1000:
        print("\nInvalid size entered. Exiting the program ......")
        print("--------------------------------------------------")
        return

    subdomainFile = "available_subdomains.txt"
    readTextFile(subdomainFile)

    possibleSubdomains = findSubdomains(userDomain, available_subdomains, size)

    writeTextFile(possibleSubdomains)

    print("\n")
    print("--------------------------------------------------")
    print("Check the output.csv file for possible subdomains.")
    print("--------------------------------------------------")
    return


# call to the main function
main()
