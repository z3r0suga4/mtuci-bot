import requests
import time
from bs4 import BeautifulSoup
import emoji

def rbk_parser():

    rbk_url = "https://realty.rbc.ru/short_news"
    page = requests.get(rbk_url).text

    soup = BeautifulSoup(page, features="html.parser")
    news = soup.find_all("div", {"class": "js-news-feed-item"})

    is_news_today = 0
    today_news = []
    today_news_answer = ""

    for i in news:
        headline = (i.find("span", {"class": "item__title"}).getText().strip())
        link = i.find("a", {"class": "item__link"})['href']
        news_date = (i.find("span", {"class": "item__category"}).getText().strip())
        if len(news_date.split(",")) == 1:
            is_news_today += 1
            today_news.append(
                    emoji.emojize(":white_small_square:") + f"""<a href="{link}">{headline}</a>\n\n"""
                    )

    if is_news_today > 0:
        today_news_answer = emoji.emojize(":newspaper:") + " <b>Новости с РБК за сегодня:</b>\n\n"
        for i in today_news:
            today_news_answer += i
        return(today_news_answer)
    else:
        today_news_answer = "Новостей на РБК за сегодня нет, ждем"
        return(today_news_answer)