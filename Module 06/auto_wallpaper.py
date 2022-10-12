"""Problem: 
    Download and change desktop wallpapers automatically    
"""
# imports
import requests
import json

# api url
api_url = "https://api.nasa.gov/planetary/apod?api_key=mrXKluARVyKYD9kKRiaGcJecAg4uOnApwiHVJo7E"

# get data
response = requests.get(api_url)
content = response.content.decode("UTF-8")

# make it into a dictonary
dict_content = json.loads(content)
image_url = dict_content['url']

# Download image
res = requests.get(image_url)

# save the image
with open("apod.png", 'wb') as image:
    image.write(res.content)
