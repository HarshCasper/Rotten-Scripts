from ipregistry import IpregistryClient

user = IpregistryClient("tryout")  
ipInfo = user.lookup() 
print(ipInfo)
