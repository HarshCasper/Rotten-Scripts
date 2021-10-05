import sys

from pytz import timezone, country_timezones
from datetime import datetime, timedelta
import argparse
import pytz

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    "--location", action="store", type=str, required=False, help="Enter the location"
)
my_parser.add_argument(
    "--country", action="store", type=str, required=False, help="Enter the country code"
)

args = my_parser.parse_args()
location = args.location
country = args.country

if not location and (not country):
    print("Please enter either location or the country code")
    sys.exit()

if country:
    code = country_timezones(country)
    timezone = pytz.timezone(code[0])
    datetimeFinder = datetime.now(timezone)
    print("Time in " + str(timezone) + ": " + datetimeFinder.strftime("%H:%M:%S"))

if location:
    timezone = pytz.timezone(location)
    datetimeFinder = datetime.now(timezone)
    print("Time in " + location + ": " + datetimeFinder.strftime("%H:%M:%S"))
