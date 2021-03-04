from geopy.geocoders import Nominatim
from geopy import distance
import argparse
def location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    parser = argparse.ArgumentParser()
    parser.add_argument('--firstlocation', type=str, required=True)
    parser.add_argument('--secondlocation', type=str, required=True)
    args = parser.parse_args()
    x = geolocator.geocode(args.firstlocation)
    y = geolocator.geocode(args.secondlocation)
    Loc1_lat,Loc1_lon = (x.latitude),(x.longitude)
    Loc2_lat,Loc2_lon = (y.latitude),(y.longitude)
    
    location1=(Loc1_lat,Loc1_lon)
    location2=(Loc2_lat,Loc2_lon)
    
    res = (str(distance.distance(location1, location2).km)+" Km")
    print (f"The total distance is: {res}")
if __name__ == "__main__":
    location()
    