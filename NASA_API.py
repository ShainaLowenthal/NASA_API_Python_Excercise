
import requests
import json
import urllib.request
import csv


response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2016-02-02&api_key=cT2Zapk1WaCGLDtMPb3hryVaYj0WqrFPxEQgq5CU")

print(response.status_code)

for item in response.json()['photos']:
    source = item['img_src']
    name = source[source.rfind("/"):]
    response = requests.get(source)
    with open("/Users/shainalowenthal/Desktop/NASA"+name, "wb") as image:
        image.write(response.content)
print("done")

