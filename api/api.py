import datetime
import requests
from decouple import config

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY2 = config("API_KEY_WEATHER")


URL_7DAYS = "http://api.weatherapi.com/v1/forecast.json?key="+API_KEY2+"&q=Bangkok&days=7"
response_7Days=requests.get(URL_7DAYS).json()


def responseTest(country):
    URL = "http://api.weatherapi.com/v1/forecast.json?key="+API_KEY2+"&q="+country+"&days=7"
    result=requests.get(URL).json()
    return result

def resultToDay(result):
    resultToDay_json = {
        "location": {
            "name": result["location"]["name"], 
            "country": result["location"]["country"], 
            "localtime": result["location"]["localtime"] 
        },
        "current":{
            "temp_c": result["current"]["temp_c"], # องศา c
            "temp_f": result["current"]["temp_f"] # องศา f
        },
        "condition": {
            "text": result["current"]["condition"]["text"] # สภาพอากาศ
        },
        "uv": result["current"]["uv"], # รังสี uv
        "wind_kph": result["current"]["wind_kph"], # แรงลม
        "wind_dir": result["current"]["wind_dir"], # ทิศทางลม
        "humidity": result["current"]["humidity"], # ความชื้น
        "cloud": result["current"]["cloud"], # เมฆปกคลุม
        "hour": [
            {
                "time": result["forecast"]["forecastday"][0]["hour"][9]["time"],
                "temp_c": result["forecast"]["forecastday"][0]["hour"][9]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][0]["hour"][9]["temp_f"],
                "condition" : result["forecast"]["forecastday"][0]["hour"][9]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][0]["hour"][12]["time"],
                "temp_c": result["forecast"]["forecastday"][0]["hour"][12]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][0]["hour"][12]["temp_f"],
                "condition" : result["forecast"]["forecastday"][0]["hour"][12]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][0]["hour"][15]["time"],
                "temp_c": result["forecast"]["forecastday"][0]["hour"][15]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][0]["hour"][15]["temp_f"],
                "condition" : result["forecast"]["forecastday"][0]["hour"][15]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][0]["hour"][18]["time"],
                "temp_c": result["forecast"]["forecastday"][0]["hour"][18]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][0]["hour"][18]["temp_f"],
                "condition" : result["forecast"]["forecastday"][0]["hour"][18]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][0]["hour"][21]["time"],
                "temp_c": result["forecast"]["forecastday"][0]["hour"][21]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][0]["hour"][21]["temp_f"],
                "condition" : result["forecast"]["forecastday"][0]["hour"][21]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][1]["hour"][0]["time"],
                "temp_c": result["forecast"]["forecastday"][1]["hour"][0]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][1]["hour"][0]["temp_f"],
                "condition" : result["forecast"]["forecastday"][1]["hour"][0]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][1]["hour"][3]["time"],
                "temp_c": result["forecast"]["forecastday"][1]["hour"][3]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][1]["hour"][3]["temp_f"],
                "condition" : result["forecast"]["forecastday"][1]["hour"][3]["condition"]["text"]
            },
            {
                "time": result["forecast"]["forecastday"][1]["hour"][6]["time"],
                "temp_c": result["forecast"]["forecastday"][1]["hour"][6]["temp_c"],
                "temp_f": result["forecast"]["forecastday"][1]["hour"][6]["temp_f"],
                "condition" : result["forecast"]["forecastday"][1]["hour"][6]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][1]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][1]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][1]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][1]["hour"][0]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][2]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][2]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][2]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][2]["hour"][0]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][3]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][3]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][3]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][3]["hour"][0]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][4]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][4]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][4]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][4]["hour"][0]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][5]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][5]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][5]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][5]["hour"][0]["condition"]["text"]
            },
            {
                "day": result["forecast"]["forecastday"][6]["hour"][0]["time"],
                "weathermin": result["forecast"]["forecastday"][6]["day"]["mintemp_c"],
                "weathermax": result["forecast"]["forecastday"][6]["day"]["maxtemp_c"],
                "condition" : result["forecast"]["forecastday"][6]["hour"][0]["condition"]["text"]
            }
        ]
    }
    return resultToDay_json
