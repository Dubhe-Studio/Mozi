import requests
import json
from khl.card import CardMessage, Card, Module


def get_weather(city: str):
    x = requests.get('https://query.asilu.com/weather/baidu/?city=' + city)
    y = json.loads(x.text)
    city = y['city']
    weather1 = y['weather'][0]
    weather2 = y['weather'][1]
    weather3 = y['weather'][2]
    weather4 = y['weather'][3]
    weather5 = y['weather'][4]
    card_message = CardMessage(Card(
        Module.Header(text=city + "的天气情况如下"),
        Module.Section(text=weather1['date']+'\t'+weather1['weather']+'\n温度：'+weather1['temp']+'\t风向：'+weather1['wind']),
        Module.Section(text=weather2['date']+'\t'+weather2['weather']+'\n温度：'+weather2['temp']+'\t风向：'+weather2['wind']),
        Module.Section(text=weather3['date']+'\t'+weather3['weather']+'\n温度：'+weather3['temp']+'\t风向：'+weather3['wind']),
        Module.Section(text=weather4['date']+'\t'+weather4['weather']+'\n温度：'+weather4['temp']+'\t风向：'+weather4['wind']),
        Module.Section(text=weather5['date']+'\t'+weather5['weather']+'\n温度：'+weather5['temp']+'\t风向：'+weather5['wind'])
    ))
    return card_message
