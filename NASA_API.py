
import requests
import json
import urllib.request
import csv


response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2016-02-02&api_key=DEMO_KEY")

print(response.status_code)

print(response.json())

def MetaCSV():
    fieldnames = list(response.json()['photos'][0].keys())
    fieldnames=fieldnames+['camera_id',"camera_name","camera_rover_id","camera_full_name"]
    with open('/Users/shainalowenthal/Desktop/meta.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in response.json()['photos']:
            item['camera_id']=item['camera']['id']
            item['camera_name']=item['camera']['name']
            item['camera_rover_id']=item['camera']['rover_id']
            item['camera_full_name']=item['camera']['full_name']
            writer.writerow(item)
           
    print("done1")



def dwnldImg():
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2016-02-02&api_key=DEMO_KEY")
    source = response.json()['photos']
    for item in source:
        source = item['img_src']
        name = source[source.rfind("/"):]
        response = requests.get(source)
        with open("/Users/shainalowenthal/Desktop/NASA"+name, "wb") as image:
            image.write(response.content)
    print("done2")


def main():
    MetaCSV()
    dwnldImg()



if __name__== "__main__":
    main()



