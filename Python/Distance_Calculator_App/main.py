import argparse
from geopy.geocoders import Nominatim
from geopy import distance

def location():
   """ A program to calculate distance between two geo-locations
    Parameters:
        firstlocation (str): The starting location of user
        secondlocation (str): The final location of user
    
   """
    geolocator = Nominatim(user_agent="geoapiExercises")
    parser = argparse.ArgumentParser()
    parser.add_argument('--firstlocation', type=str, required=True)
    parser.add_argument('--secondlocation', type=str, required=True)
    args = parser.parse_args()

    # calculating longitude and latitude of entered locations """
    try:
        first_location = geolocator.geocode(args.firstlocation)
        second_location = geolocator.geocode(args.secondlocation)
        Loc1_lat,Loc1_lon = (first_location.latitude),(first_location.longitude)
        Loc2_lat,Loc2_lon = (second_location.latitude),(second_location.longitude)

        location1=(Loc1_lat,Loc1_lon)
        location2=(Loc2_lat,Loc2_lon)

    # calculating and printing distance between locations in Kilometers and Miles."""

        res = ((distance.distance(location1, location2).km))
        distance_miles = float(res)*0.621371
        print (f"The total distance is: {res} Km , {distance_miles} Miles")
    except:
        print("Invalid Location")
        
if __name__ == "__main__":
    location()
    
