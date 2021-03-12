from argparse import ArgumentParser
import json
import requests
import datetime

# use github api to get details of pulls


def read(reponame):
    product_list_reponame = f"https://api.github.com/repos/{reponame}/pulls"
    response = requests.get(product_list_reponame)
    return response.json()


# save api response  in apiresp.json
def save(reponame):
    print("please wait...")
    with open('apiresp.json', 'w') as json_file:
        json.dump(read(reponame), json_file)
        print("done!")


def run(args):
    with open("apiresp.json") as f:
        jsonfile = json.load(f)

    # totle pull request
    if args.pulls:
        pass

    # all pulls in detail
    if args.activepr:
        with open("apiresp.json") as f:
            a = json.load(f)
            print("==============================================================")
            for x, i in enumerate(a):
                d1 = datetime.datetime.now().replace(microsecond=0)
                d2 = datetime.datetime.strptime(
                    i["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            #	print(i["title"]," open since :---------->",d1-d2, "\n")

                print(f"[{x+1}] :", '{:>10}'.format(i["title"]))
                print(f"opened since: [{d1-d2}]\n")
        print("===============================================================")
        print("Active pull requests: ", len(jsonfile))

    if args.verbose:
        pass

    # closed pulls
    if args.closedpr:
        pass


if __name__ == "__main__":
    parser = ArgumentParser(
        description='A command line tool for understanding the PR workflow')
    parser.add_argument('-u', '--reponame', action='store', dest='reponame', default=None,
                        help='<Required> repository name [username/reponame]', required=True)

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Shows data in verbose mode.')
    parser.add_argument('-pr', '--pulls', action='store_true',
                        help='Totle pull request.')
    parser.add_argument('-apr', '--activepr',
                        action='store_true', help='Active pull request')
    parser.add_argument('-cpr', '--closedpr',
                        action='store_true', help='Closed pull request')
    args = parser.parse_args()

    reponame = args.reponame
    save(reponame)
    run(args)
