from helper import DeleteMinRetweet


def main():
    ob = DeleteMinRetweet('credentials.json', 80, 110)
    tweets = ob.filter()
    ob.delete_all(tweets=tweets)


if __name__ == '__main__':
    main()
    