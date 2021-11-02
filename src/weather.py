from config import open_weather_token
import datetime
import requests


class open_weather:
    def __init__(self):
        self.token = open_weather_token

    def get_weather(self, city):
        try:
            code_to_smile = {
                "Clear": "Ясно \U00002600",
                "Clouds": "Облачно \U00002601",
                "Rain": "Дождь \U00002614",
                "Drizzle": "Дождь \U00002614",
                "Thunderstorm": "Гроза \U000026A1",
                "Snow": "Снег \U0001F328",
                "Mist": "Туман \U0001F32B"
            }

            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.token}&units=metric"
            )
            data = r.json()
            city = data['name']
            cur_temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
            length_daytime = datetime.datetime.fromtimestamp(data['sys']['sunset']) - \
                             datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            temp_feels = data['main']['feels_like']
            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Посмотри в окно, не пойму что там за погода!"

            return (f"\U0001F30C{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\U0001F30C\n"
                    f"Погода в городе: {city}\n{wd}\nТемпература: {cur_temp} C°\nТемпуратура ощущается: {temp_feels} C°\n"
                    f"Влажность: {humidity}%\nВетер: {wind} м/c\n"
                    f"Восход солнца: {sunrise}\nЗакат солнца: {sunset}\n"
                    f"Продолжительность дня: {length_daytime}"
                    )
        except Exception as ex:
            return "На сегодня нет прогноза погоды"
