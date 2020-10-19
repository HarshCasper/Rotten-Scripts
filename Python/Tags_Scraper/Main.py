import SearchResults
from Fetch_Tags import FetchTags
import os
import urllib3


if __name__ == '__main__':

    directory = os.getcwd()

    if os.path.exists(directory + r"/KeywordsData.txt"):
        os.remove(directory + r"/KeywordsData.txt")

    query = input("Enter search query\n>> ").strip()
    results = SearchResults.FetchURLs(query)
    obj = FetchTags(results)
    alt_tag_dict, title_dict, h2_dict, h3_dict = obj.get_results()

    sorted_alt = sorted(alt_tag_dict.items(), key = lambda x : x[1], reverse = True)
    sorted_title = sorted(title_dict.items(), key = lambda x : x[1], reverse = True)
    sorted_h2 = sorted(h2_dict.items(), key = lambda x : x[1], reverse = True)
    sorted_h3 = sorted(h3_dict.items(), key = lambda x : x[1], reverse = True)

    fp = open(directory + '/KeywordsData.txt', 'w')

    fp.write("""
        TOP 20 Alternative Tag Data : {}\n\n
        TOP 20 Title Tag Data : {}\n\n
        TOP 20 H2 Tag Data : {}\n\n
        TOP 20 H3 Tag Data : {}""".format(type(sorted_alt[:20], sorted_title[:20], sorted_h2[:20], sorted_h3[:20]))

    print("Fetched KeywordsData successfully")
    fp.close()
