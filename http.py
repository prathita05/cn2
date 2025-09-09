import requests

def http_client():
    url = "https://httpbin.org/get"
    post_url = "https://httpbin.org/post"

    try:
        # GET request
        response_get = requests.get(url)
        print("GET Request:")
        print("Status Code:", response_get.status_code)
        print("Headers:", response_get.headers)
        print("Body:", response_get.text[:200], "\n")  # printing first 200 chars

        # POST request
        payload = {"name": "Prathita", "msg": "Hello from CN Lab"}
        response_post = requests.post(post_url, data=payload)
        print("POST Request:")
        print("Status Code:", response_post.status_code)
        print("Headers:", response_post.headers)
        print("Body:", response_post.text[:200])

    except Exception as e:
        print("Error:", e)

http_client()

