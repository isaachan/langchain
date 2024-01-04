import requests
import json
import openai

def get_weather(loc):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": loc,
        "appid": "c03927cd5a063745d54aba89401236db",
        "units": "metric",
        "lang": "zh_cn"
    }

    response = requests.get(url, params=params)

    data = response.json()
    return json.dumps(data)



response = openai.ChatCompletion.create(
    model = "chatglm3-6b",
    messages = [
        {"role": "user",
         "content": "请问你知道OpenWeather吗？"}
    ]
)