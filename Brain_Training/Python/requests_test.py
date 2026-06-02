import requests
import json
def newsupdate():
    # url= "https://www.google.com"
    query= input("What type of news you are interested in: ")
    url = f"https://newsdata.io/api/1/latest?apikey=pub_072640b42b09427f8bf8130b69b1087f&q={query}"
    r = requests.get(url)
    news = json.loads(r.text)
    print(news,type(news))
    for article in news["results"]:
        print("source_name: ",end=": ")
        print(article["source_name"])
        print("Description: ", end=": ")
        print(article["description"])
        print("Link to read details: ", end=": ")
        print(article["link"])
        print("-------------------------------------------")

def weatherupdate():
    weatherapikey='4572f8cea58e0ac000da9509d9620f40'
    city= input("Please insert your city name: ")
    # state = input("Please insert your state name: ")
    country = input("Please insert your country name: ")
    met=int(input("Please select metric of your choice: \n1. Celsius \n2.Fahrenheit \n  "))
    if met==1:
        mtrics="metric"
    elif met ==2:
        mtrics="imperial"
    else:
        print("Please select metric value between given options again..")
        exit(0)
    limit=5
    # lat=22.5744
    # long=88.3629
    exclude='hourly,daily,alerts'
    # print(f"For {city} latitude and longitude is: {lat}&{long} respectively")
    # lat_long_url= f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={weatherapikey}"
    weatherurl= f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={mtrics}&APPID={weatherapikey}"
    # req = requests.get(lat_long_url)
    # lat_long_details=json.loads(req.text)
    # print(lat_long_details)
    req_w= requests.get(weatherurl)
    rj=json.loads(req_w.text)
    # print(req_json)
    print(f"Latitude: {rj["coord"]["lat"]} and Longitude: {rj["coord"]["lon"]}")
    # print(rj["main"])
    print(f"---------Temperature details of {city},{country}---------")
    print(f"Current temperature:{rj["main"]["temp"]}")
    print(f"Feels Like:{rj["main"]["feels_like"]}")
    print(f"Today's minimum temperature:{rj["main"]["temp_min"]}")
    print(f"Today's maximum  temperature:{rj["main"]["temp_max"]}")
    print(f"Current humidity:{rj["main"]["humidity"]}")


if __name__=='__main__':
    newsupdate()
    # weatherupdate()