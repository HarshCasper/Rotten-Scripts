from googlesearch import search

def google_search_results(keyword, domain= 'com'):
	#generator function
	for links in search(keyword, tld= domain, pause= 2):
		yield links
		
def main():
	query = input("Enter your search keyword: ")
	number_of_results = int(input("Enter number of links you want: "))
	count =1
	for link in google_search_results(query):
		# final result is printed in the form [rank link]
		if count> number_of_results:
			break

		print (count,link,"\n")
		count+=1
		

if __name__ == "__main__":
	main()


