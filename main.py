#THIS CODE IS FOR EDUCATIONAL PURPOSE. DO NOT TRY THIS IN ANY 3RD PARTY SERVER. WE ARE NOT PRACTICING/ALLOWING PENETRATION TESTING USING THIS CODE.
#I AM NOT RESPONSIBLE FOR ANY ACTIONS TAKEN BY THE USER OF THIS CODE.
#DO NOT TRY THIS ON RANDOM WEBSITE
#USE "HACKTHISSITE.ORG" FOR LEARNING PURPOSE.



import requests

domain = "facebook.com" #DO NOT USE ANY WEBSITE LIKE FACEBOOK, AMAZON, GOOGLE etc. THIS IS JUST FOR TESTING PURPOSE. CHANGE IT TO YOUR OWN SERVER NAME.

file = open("subdomains.txt", "r")

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("Discovered Subdomain :", url)
