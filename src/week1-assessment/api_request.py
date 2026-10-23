
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

print("Status code:", response.status_code)

response.raise_for_status()

users = response.json()

print("Number of users:", len(users))
print("First three users:")

for user in users[:3]:
    print(user["name"], "-", user["email"])
