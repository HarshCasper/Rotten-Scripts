class Utilities:
	def writeFile(self, filename, content):
		fd = open(filename, "wb")
		fd.write(content)
		fd.close()

	def readFile(self, filename):
		fd = open(filename, "rb")
		content= fd.read()
		fd.close()
		return content