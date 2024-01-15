import json, requests, openai

import dotenv
dotenv.load_dotenv(verbose=True)

from openai import OpenAI

def get_weather(loc):
    """
    查询即时天气函数
    :param loc: 必须参数，字符串，城市名
    注意：中国城市的名字需要用拼音，比如查询北京的天气，需要输入'beijing'
    :return: 字符串，Weather API返回的天气信息结果，是用的JSON格式，并以字符串来表示
    """

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": loc,
        "appid": "c03927cd5a063745d54aba89401236db",
        "units": "metric",
        "lang": "zh_cn"
    }

    response =requests.get(url, params=params)
    weather = response.json()
    print(json.dumps(weather))
    return json.dumps(weather)


beijing_weather = get_weather("beijing")


client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4-0613",
    messages = [
        {"role": "system", "content": "天气信息来源是OpenWeather AIP：https://api.openweathermap.org/data/2.5/weather"},
        {"role": "system", "content": "这是今天北京的天气: {}".format(beijing_weather)},
        {"role": "user", "content": "今天北京的天气怎样，用中文回答" }
    ]
)

print(response.choices[0].message)