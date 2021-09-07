import requests

request_bbc = requests.get("https://www.google.co.uk")

print("-------- Status Codes ---------")
print(request_bbc.status_code)
print("--------- Content ---------")
input()
print(request_bbc.content)
