import requests
import json
import math

def convert(kelvinTemp):
    kelvinToCelcius = kelvinTemp - 273.15
    celciusToFahr = kelvinToCelcius * (9/5) + 32
    roundedFahr = math.floor(celciusToFahr)
    return roundedFahr

api_key = "7e0c8d811cd1042cbe82463db009527c"

basic_url = "http://api.openweathermap.org/data/2.5/weather?"

#Enter a city name
cityName = input("Enter city you wish to see weather for: ")

#Get URL from location enteredsa
completeUrl = basic_url +"q=" + cityName + "&appid="+api_key

#get response object from URL
response = requests.get(completeUrl)

#convert json object into python format
jsonToPython = response.json()
apiInfo = json.loads(response.content)
#print(jsonToPython)

if jsonToPython["cod"] != "404":
    #store value of "main"
    y = apiInfo["main"]

    current_temp = y["temp"]
    feels_like = y["feels_like"]
    min_temp = y["temp_min"]
    max_temp = y["temp_max"]
    pressure = y["pressure"]
    humidity = y["humidity"]

    convertedCurrentTemp = convert(current_temp)
    convertedFeelsLike = convert(feels_like)
    convertedMin = convert(min_temp)
    convertedMax = convert(max_temp)

    print("Current Temperature: " + str(convertedCurrentTemp) +
    "\n Feels like: " + str(convertedFeelsLike) +
    "\n Low temperature: " + str(convertedMin) +
    "\n High Temperature: " + str(convertedMax)+
    "\n Pressure: " + str(pressure) +
    "\n Humidity: " + str(humidity))
else:
    print("City not found")




