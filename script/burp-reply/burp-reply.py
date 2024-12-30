import argparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError




def parse_burp_request(file_path):
    """
    Read a burp request from file
    """

    with open(file_path, 'r') as file:
        lines = file.readlines()

    import pdb; pdb.set_trace()
    method, url, protocol = lines[0].strip().split(" ")
    headers = {}
    body = None
    in_body = False

    for line in lines[1:]:
        line = line.strip()
        if not line:
            in_body = True
            continue
        if in_body:
            body = line
        else:
            header_name, header_value = line.split(": ", 1)
            headers[header_name] = header_value

    return method, url, headers, body, protocol

def send_request(method, url, headers, body, protocol):
    """
    Send burp request
    """
    import pdb; pdb.set_trace()
    req = Request(url, method=method, headers=headers)
    if body:
        body = body.encode('utf-8')
        with urlopen(req, data=body) as response:
            print("[*] Burp Response")
            
            print(f"Response Code: {response.getcode()}")
            print("Response Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print("\nResponse Body:")
            print(response.read().decode('utf-8'))
def main():
    parser = argparse.ArgumentParser(description="Burp request reply")
    
    parser.add_argument("url",
                        help="Destination Url")
    
    parser.add_argument("burpfile",
                        help="Request file (BURP)")
    

    args = parser.parse_args()
    method, path, headers, body, protocol = parse_burp_request(args.burpfile)
    print("==================")
    print("Burp File")
    print("==================")
    print("")

    print(f"Method: {method}")
    print(f"Url: {args.url}{path}")
    print(f"Headers: {headers}")
    send_request(method, f"{args.url}{path}", headers, body, protocol)

if __name__=="__main__":
    main()