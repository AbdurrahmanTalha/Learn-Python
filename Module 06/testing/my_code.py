import requests

api_uri = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


def get_response(url):
    return requests.get(url)


if __name__ == "__main__":
    res = get_response(api_uri)
    print(res)
