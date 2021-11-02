import config
import requests


class News:
    def __init__(self):
        self.token = config.newsapi
        self.count_of_articles = 0

    def GetCount(self):
        return self.count_of_articles

    def GetNews(self):
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=ru&category=business&apiKey={self.token}"
            )
            data = r.json()
            articles = data['articles']
            my_articles = []
            my_news = []
            for article in articles:
                my_articles.append(article['title'])
                self.count_of_articles += 1

            for i in range(self.count_of_articles):
                my_news += [my_articles[i], data['articles'][i]['url']]

            return my_news

        except Exception as ex:
            return "На сегодня нет новостей"
