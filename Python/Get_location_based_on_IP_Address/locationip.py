from ipregistry import IpregistryClient

client = IpregistryClient("tryout")  
ipInfo = client.lookup() 
print(ipInfo)
