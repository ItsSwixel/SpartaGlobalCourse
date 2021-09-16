import requests

response = requests.get("http://127.0.0.1:8080")
print(response.content)
response_post = requests.post("http://127.0.0.1:8080/create_info")
print(response_post.content)
response_post_data = requests.post("http://127.0.0.1:8080/create_info", data={"username": "adam", "password": "pass456"})
print(response_post_data.content)
