from helper import DeleteMinRetweet
import argparse
import sys

def create_parser():
    """
        Create an argument parser for using the program through commandline
    """
    parser = argparse.ArgumentParser(description="Deletes the tweets based on the details given by the user")
    
    ## Add the argument named 'path' for retrieving the 'credentials.json' file
    parser.add_argument("--path",
                        metavar="P",
                        type=str,
                        help="Path to the 'credentials.json' file")
    
    ## Add arguments for minimum and maximum threshold values
    parser.add_argument("--min",
                        metavar="N",
                        type=int,
                        default=-1,
                        help="Minimum threshold of the parameter, to be followed while deleting the tweets (default 100)"
                        ) 

    parser.add_argument("--max",
                        metavar="N",
                        type=int,
                        default=sys.maxsize,
                        help="Maximum threshold of the parameter, to be followed while deleting the tweets (default 150)"
                        )

    return parser


def main():
    parser = create_parser()

    args = parser.parse_args()

    # Retrieve the path to the 'credentials.json' file
    path = args.path

    # Retrieve the minimum and maximum threshold values

    min_threshold = args.min
    max_threshold = args.max

    ob = DeleteMinRetweet(path, min_threshold, max_threshold)
    tweets = ob.filter()
    ob.delete_all(tweets=tweets)


if __name__ == '__main__':
    main()
    