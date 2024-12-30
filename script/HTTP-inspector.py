import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)


def search_missing_headers(headers):
    suggested_headers = ["content-security-policy", "permissions-policy", "referrer-policy", "strict-transport-security", "x-content-type-options"]
    for sgst_header in suggested_headers:
        if sgst_header not in headers:
            print("Missing security header: "+Fore.YELLOW+sgst_header)

def check_http_methods(url, headers):
    allowed_method = []

    response = requests.delete(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("DELETE")

    response = requests.get(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("GET")
    

    response = requests.post(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("POST")

    response = requests.put(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("PUT")

    response = requests.patch(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("PATCH")
    
    response = requests.head(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("HEAD")

    response = requests.options(url, headers=headers)
    if response.status_code!=405:
        allowed_method.append("OPTIONS")

    
    
    print("Allowed HTTP methods: "+Fore.GREEN+",".join(allowed_method))



    



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


#url = input("Url: ")
#cookie = input("Cookie (Default: ''): ")

url = sys.argv[1]
cookie = sys.argv[2] if len(sys.argv)>2 else ""

if cookie:
    headers["Cookie"] = cookie

print("===========================================")
print("\tGetting headers...")
print("===========================================")

response = requests.get(url, headers=headers, verify=False)
for header in response.headers:
    print(f"{header}: "+Fore.GREEN+f"{response.headers[header]}")

print("")
print("===========================================")
print("\tChecking security headers...")
print("===========================================")

search_missing_headers(response.headers)

print("")
print("===========================================")
print("\tChecking HTTP allowed methods...")
print("===========================================")

check_http_methods(url, headers)


print("")
print("===========================================")
print("\tRobots file...")
print("===========================================")

parsed_url = urlparse(url)
host = parsed_url.netloc
response = requests.get(parsed_url.scheme+"://"+parsed_url.netloc+"/robots.txt", headers=headers, verify=False)

print(response.text)

