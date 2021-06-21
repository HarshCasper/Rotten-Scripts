from utils import SelectFiles, OrganizeFiles


def main():
    """Creates objects for SelectFiles and OrganizeFiles and calls \
        the driver code"""

    ob = SelectFiles()
    files = ob.filter()
    organize = OrganizeFiles(files)
    organize.organize()


if __name__ == "__main__":
    main()
