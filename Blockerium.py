import time;
from datetime import datetime as dt;

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com","facebook.com","www.instagram.com"]

while True:
     if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,0):
          print("Working hours...")
          with open(hosts_path,'r+') as file:
               content = file.read()
               for website in websiteList:
                    if website in content:
                         pass
                    else:
                         file.write(redirect + " " + website+ "\n")
     else:
          with open (hosts_path,'r+') as file:
               content = file.readlines()
               file.seek(0)
               for line in content:
                    if not any(website in line for website in websiteList):
                         file.write(line)
               file.truncate()
          print("Relaxing hours begins..")
     time.sleep(5)
     # while True:
     # if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,0):
     #      print("Working hours...")
     #      with open(hosts_path,'r+') as file:
     #           content = file.read()
     #           for website in websiteList:
     #                if website in content:
     #                     pass
     #                else:
     #                     file.write(redirect + " " + website+ "\n")
     # else:
     #      with open (hosts_path,'r+') as file:
     #           content = file.readlines()
     #           file.seek(0)
     #           for line in content:
     #                if not any(website in line for website in websiteList):
     #                     file.write(line)
     #           file.truncate()
     #      print("Relaxing hours begins..")
     # # time.sleep(5)
