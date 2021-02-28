from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="geoapiExercises")
         
place1 = geolocator.geocode(input("1st Location: "))
place2 = geolocator.geocode(input("2nd Location: "))
 
 
Loc1_lat,Loc1_lon = (place1.latitude),(place1.longitude)
Loc2_lat,Loc2_lon = (place2.latitude),(place2.longitude)
 
location1=(Loc1_lat,Loc1_lon)
location2=(Loc2_lat,Loc2_lon)
 
res = (str(distance.distance(location1, location2).km)+" Km")
 
# result.set(res)
print(f"The total distance is: {res}")