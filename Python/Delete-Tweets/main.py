from helper import DeleteRetweet, DeleteFavorite, DeleteOld
import argparse
import sys

def create_parser():

    """
        Create an argument parser for using the 
        program through commandline
    """
    parser = argparse.ArgumentParser(description="Deletes the tweets based on \
        the details given by the user")

    # Add the argument named 'path' for retrieving the 'credentials.json' file
    parser.add_argument("--path",
                        metavar="P",
                        type=str,
                        required=True,
                        help="Path to the 'credentials.json' file")

    # Add the argument to distinguish between the parameters for filtering the tweets
    parser.add_argument('--param',
                        metavar="M",
                        type=str,
                        required=True,
                        choices=["retweet", "likes", "time"],
                        help="Parameter to be used for filtering the tweets\
                            (retweet, likes, time)."
                        )

    # Add the argument named 'count' for setting the no of tweets to be retrieved
    parser.add_argument("--count",
                        metavar="C",
                        type=int,
                        default=20,
                        required=False,
                        help="Number of tweets to be considered (Default 20)")

    # Add arguments for minimum and maximum threshold values
    parser.add_argument("--min",
                        metavar="N",
                        type=int,
                        default=0,
                        required=False,
                        help="Minimum threshold of the parameter, to be followed \
                            while deleting the tweets (default 0)"
                        )

    parser.add_argument("--max",
                        metavar="N",
                        type=int,
                        default=sys.maxsize,
                        required=False,
                        help="Maximum threshold of the parameter, to be followed \
                            while deleting the tweets (default MAXINT)"
                        )

    # Add arguments for hours and days for time based filtering
    parser.add_argument("--hours",
                        metavar="H",
                        type=int,
                        default=0,
                        required=False,
                        help="No of hours to go back from current time \
                            for filtering tweets (default 0)"
                        )

    parser.add_argument("--days",
                        metavar="D",
                        type=int,
                        default=0,
                        required=False,
                        help="No of days to go back from current time for \
                            filtering tweets (default 0)"
                        )

    parser.add_argument("--verbose",
                        action="store_true",
                        required=False,
                        help="When passed, the tweets are displayed before \
                            getting deleted"
                        )


    return parser


def main():
    """Driver method to instantiate the classes and call the relevant methods"""
    parser = create_parser()

    args = parser.parse_args()

    # Retrieve the path to the 'credentials.json' file
    path = args.path

    # Retrieve the 'count' argument
    count = args.count

    # Retrieve the method of filtering to be used
    param = args.param

    # Retrieve the minimum and maximum threshold values
    min_threshold = args.min
    max_threshold = args.max

    # Retrieve the values for the hours and days for time based filtering
    days = args.days
    hours = args.hours

    # Retrieve the verbose argument
    verbose = args.verbose

    # Instantiate relevant classes
    ob = None
    if param == 'retweet':
        ob = DeleteRetweet(path, min_threshold, max_threshold)
    elif param == 'likes':
        ob = DeleteFavorite(path, min_threshold, max_threshold)
    elif param == 'time':
        # Set the count parameter to retrieve the maximum tweets possible
        count = 200
        ob = DeleteOld(path, days, hours)

    tweets = ob.filter(count=count)

    ob.delete_all(tweets=tweets, verbose=verbose)


if __name__ == '__main__':
    main()
