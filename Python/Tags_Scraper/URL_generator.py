class GURL:
    """
    GURL is Google URL generator class which has 2 methods and constructor which takes in the query
    but has got 4 other parameters as well, Generate: which generates
    URL and get_url : which returns the string of generated url
    """
    def __init__(self, query, limit=100, filetype='html', timeperiod='w', safemode='active'):
        """
        This is the constructor which takes the query string and converts it into a parameterised
        google accepted URL.
        """
        self.base_url = "https://google.com"
        self.query = query.replace(' ', '+')
        self.limit = limit
        self.filetype = filetype
        self.timeperiod = timeperiod
        self.safemode = safemode
        self.url = None

    def generate(self):
        """ This method 
        """
        self.url = self.base_url + "/search?q={0}&num={1}&as_filetype='{2}'&as_qdr={3}&safe={4}".format(self.query, self.limit, self.filetype, self.timeperiod, self.safemode)
        print("GENERATED URL : '{}'".format(self.url))

    def get_url(self):
        """ This method returns the generated URL in a string format """
        return self.url


if __name__ == '__main__':

    OBJ = GURL('SLoP')
    OBJ.generate()
