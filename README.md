# Telegram Bot
**Возможности бота:**   
- <b>Новости</b>
- <b>Анекдот</b>
- <b>Прогноз погоды</b>
- <b>Курс рубля</b>
- <b>Спам по номеру телефона с использованием impulse</b>
- <b>Администрирование бота: дополнительные возможности у роли администратора</b>
## Как запустить?
**Установить необходимые библиотеки** </br>
>pip install aiogram bs4 requests scapy wget argparse colorama humanfriendly
</br>

**config.py установить свои значения**

```css
# Write there your telegram bot token
token = ''
# API key from https://openweathermap.org/
open_weather_token = ''
# API key from https://newsapi.org/
newsapi = ''
# Write there your city
your_city = 'Moscow'
```
- <b>token = </b> - ввести токен своего бота в телеграмме</br>
- <b>open_weather_token = </b> - ввести свой API key, который можно получить на сайте: https://openweathermap.org/\</br>
- <b>newsapi = </b> - ввести свой API key, который можно получить на сайте https://newsapi.org/\</br>
- <b>your_city = </b> - указать свой город для получения прогноза погоды\</br>
