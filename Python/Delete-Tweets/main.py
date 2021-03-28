from helper import DeleteRetweet, DeleteFavorite
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
                        required=True,
                        help="Path to the 'credentials.json' file")
    
    ## Add the argument to distinguish between the parameters for filtering the tweets
    parser.add_argument('--param',
                        metavar="M",
                        type=str,
                        required=True,
                        help="Parameter to be used for filtering the tweets (retweet, likes, time)."
                        )

    ## Add arguments for minimum and maximum threshold values
    parser.add_argument("--min",
                        metavar="N",
                        type=int,
                        default=0,
                        required=False,
                        help="Minimum threshold of the parameter, to be followed while deleting the tweets (default 100)"
                        ) 

    parser.add_argument("--max",
                        metavar="N",
                        type=int,
                        default=sys.maxsize,
                        required=False,
                        help="Maximum threshold of the parameter, to be followed while deleting the tweets (default 150)"
                        )

    ## Add arguments for hours and days for time based filtering
    parser.add_argument("--hours",
                        metavar="N",
                        type=int,
                        default=1,
                        required=False,
                        help="No of hours to go back from current time for filtering tweets (default 1)"
                        ) 

    parser.add_argument("--days",
                        metavar="N",
                        type=int,
                        default=0,
                        required=False,
                        help="Maximum threshold of the parameter, to be followed while deleting the tweets (default 1)"
                        )


    return parser


def main():
    """Driver method to instantiate the classes and call the relevant methods"""
    parser = create_parser()

    args = parser.parse_args()

    # Retrieve the path to the 'credentials.json' file
    path = args.path

    # Retrieve the minimum and maximum threshold values
    min_threshold = args.min
    max_threshold = args.max

    # Retrieve the values for the hours and days for time based filtering
    days = args.days
    hours = args.hours

    # Retrieve the parameter to be used
    param = args.param


    # Instantiate relevant classes
    ob = None
    if param == 'retweet':    
        ob = DeleteRetweet(path, min_threshold, max_threshold)
    elif param == 'likes':
        ob = DeleteFavorite(path, min_threshold, max_threshold)
    elif param == 'time':
        pass

    tweets = ob.filter()
    ob.delete_all(tweets=tweets)


if __name__ == '__main__':
    main()
    