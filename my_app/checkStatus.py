import requests

url = "https://tahayagizguler.tech"

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
else:
    print("Failure!")