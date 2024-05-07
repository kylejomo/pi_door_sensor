import requests

# Post - Write a new todo
#api_url = "https://api.restful-api.dev/objects"
#thing = {"name": "Closed"}
#response = requests.post(api_url, json=thing)
#print("Response from Post")
#print(response.json())
#print("ID and Status Code")
#print(response.json().get("id"))
#print(response.status_code)


# Get - Get the todo just written
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
response = requests.get(api_url)
print("\n\n Get of the thing object just written")
print(response.json())


# PUT - Change the todo
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
thing = {"name": "Opened"}
response = requests.put(api_url, json=thing)
print("\n\n Response from Put")
print(response.json())
print(response.status_code)


# Get - Get the todo just changed 
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
response = requests.get(api_url)
print("\n\n Get of the thing object just written")
print(response.json())
