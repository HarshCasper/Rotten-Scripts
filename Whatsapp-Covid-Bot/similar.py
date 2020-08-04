#Imports
import difflib

#In case a location entered by the user fails to exist, this function is used to provide a list of places that are similar to the one entered.
#Locations whose similarity is more than 65% are returned.
#difflib, is a framework in Python, here is used for determining how close 2 strings are. 
#It returns a value between 0 and 1, 1 being the same, 0 being completely different

def similar_locations(locations, cases_loc):
    similar = ""
    for loc in locations:
        if difflib.SequenceMatcher(None, cases_loc, loc).ratio() >= 0.65:
            similar += loc + "\n"
    return(similar.strip("\n"))
