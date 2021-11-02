import requests
import bs4


class joker:
    def __init__(self):
        self.link = "http://anekdotme.ru/random"

    def GetJoke(self):
        try:
            str = ''
            s = requests.get(self.link)
            data = bs4.BeautifulSoup(s.text, "html.parser")
            data = data.select('.anekdot_text')
            for x in data:
                s = (x.getText().strip())
                z = str + s + '\n\n'
            return '\U0001F923 \U0001F923 \U0001F923 \n' + s
        except Exception as ex:
            return 'Анекдот не найден'
