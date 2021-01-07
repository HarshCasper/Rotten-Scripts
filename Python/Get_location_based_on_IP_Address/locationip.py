#import geocoder
# = geocoder.ipinfo('42.106.238.166')
#print(g.latlng)

#from requests import get
#import json

#url = 'http://ipinfo.io/json'
#response = get(url)
#data = json.loads(response.text)

#city = data['city']
#region = data['region']
#country = data['country']
#postal = data['postal']
#timezone = data['timezone']
#ip = data['ip']

#print("ip:", ip)
#print("city:", city)
#print("region:", region),
#print("country:", country)
#print("postal:", postal)
#print("timezone:", timezone)

from ipregistry import IpregistryClient

client = IpregistryClient("tryout")  
ipInfo = client.lookup() 
print(ipInfo)