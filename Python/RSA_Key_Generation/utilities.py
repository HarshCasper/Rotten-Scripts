class Utilities:
    def writeFile(self, filename, content):
        file_ptr = open(filename, "wb")
        file_ptr.write(content)
        file_ptr.close()

    def readFile(self, filename):
        file_ptr = open(filename, "rb")
        content = file_ptr.read()
        file_ptr.close()
        return content
