from urllib.request import urlopen
import json

url = "192.168.1.94/api/v1/stats"

with urlopen(url) as response:
    body = response.read()

data = json.loads(body)

with open("esimerkki.csv", "w") as csv:
    
    for key, value in data.items():
        csv.write(f"{key};{value}\n")

