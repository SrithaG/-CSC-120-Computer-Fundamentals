import requests

response = requests.get('https://reddit.com')
print(response.status_code)
print(response.headers['Content-Type'])

if response.status_code == 200:
    print("SUCCESS")
else:
    print("Error")
