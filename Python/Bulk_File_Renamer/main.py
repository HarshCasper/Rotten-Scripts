from utils import SelectFiles, OrganizeFiles

def main():
    ob = SelectFiles()
    files = ob.filter()
    # print(files)
    organize = OrganizeFiles(files)
    organize.organize()

if __name__ == '__main__':
    main()
    