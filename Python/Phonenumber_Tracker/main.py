import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier


country= phonenumbers.parse(number, "CH")
service_provider= phonenumbers.parse(number , "RO")
print(geocoder.description_for_number(country, "en"))
print(carrier.name_for_number(service_provider, "en") )