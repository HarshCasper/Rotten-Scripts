class GURL(object):
	def __init__(self, query, limit = 100, filetype = 'html', timeperiod = 'w', safemode = 'active'):
		self.base_url = "https://google.com"
		self.query = query.replace(' ', '+')
		self.limit = limit
		self.filetype = filetype
		self.timeperiod = timeperiod
		self.safemode = safemode
		self.url = None

	def generate(self):
		self.url = self.base_url + "/search?q={0}&num={1}&as_filetype='{2}'&as_qdr={3}&safe={4}".format(
			self.query, self.limit, self.filetype, self.timeperiod, self.safemode)
		print("GENERATED URL : '{}'".format(self.url))

	def get_url(self):
		return self.url


if __name__ == '__main__':

	obj = GURL('SLoP')
	obj.generate()