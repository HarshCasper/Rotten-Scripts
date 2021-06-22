#Only pre requirement is pip install speedtest-cli

import speedtest

st = speedtest.Speedtest()

print("Download Speed is: ",st.download()//10**6,"Mbps")
print("Upload Speed is: ",st.upload()//10**6,"Mbps")
print("Ping is: ",int(st.results.ping),"Ms")
