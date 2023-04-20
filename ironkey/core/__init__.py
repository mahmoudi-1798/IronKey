import requests

response = requests.get("https://httpbin.org/ip")

print(f"Your Ip is {format(response.json()['origin'])}")