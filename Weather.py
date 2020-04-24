import json, requests

KEY_API = "61c0bbaf230b82b8d2da8e18c5cf2996"

async def _weather(ctx, message = None):
    if message == None:
        req = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Bordeaux,fr&appid={}".format(KEY_API))
    else:
        message.replace(" ", "%20")
        req = requests.get("https://api.openweathermap.org/data/2.5/weather?q={},fr&appid={}".format(message, KEY_API))
            
    result = req.json()

    if "weather" in result:
        weather = result["weather"][0]["main"]
        temperature = int(result["main"]["temp"]) - 273.15
        temperature_feel = int(result["main"]["feels_like"]) - 273.15
        city = result["name"]
        await ctx.send("Weather is {}, temperature is {:.2f}°C but feel like {:.2f}°C, in {}".format(weather, temperature, temperature_feel, city))
    else:
        req = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(message, KEY_API))
        result = req.json()
        if "weather" in result:
            weather = result["weather"][0]["main"]
            temperature = int(result["main"]["temp"]) - 273.15
            temperature_feel = int(result["main"]["feels_like"]) - 273.15
            city = result["name"]
            await ctx.send("Weather is {}, temperature is {:.2f}°C but feel like {:.2f}°C, in {}".format(weather, temperature, temperature_feel, city))
        else:
            await ctx.send("La ville {} n'existe pas".format(message))