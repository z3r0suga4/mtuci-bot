import requests
import time
from datetime import datetime
import emoji
from bs4 import BeautifulSoup

def irn_parser():

    irn_url = "https://www.irn.ru/news/"
    page = requests.get(irn_url).text

    soup = BeautifulSoup(page, features="html.parser")
    news = soup.find_all("a", {"class": "post-list-item"}, href=True)

    today_date = datetime.today().strftime('%Y-%m-%d')
    today_news = []
    today_news_answer = emoji.emojize(":newspaper:") + " <b>Новости за сегодня с IRN:</b>\n\n"

    for i in news:
        title = i.find("div", {"class" : "post-list-item-link"}).getText().strip()
        link = f"https://www.irn.ru{i['href']}"

        news_page = requests.get(link).text
        news_soup = BeautifulSoup(news_page, features="html.parser")
        time = news_soup.find("meta", {"property" : "article:published_time"}).get('content')
        
        published_time = time[:10]

        if published_time == today_date:
            today_news.append(emoji.emojize(":white_small_square:") + f"""<a href="{link}">{title}</a>\n\n""")
        else:
            break

    if len(today_news) != 0:
        for i in today_news:
            today_news_answer += i
    else:
        today_news_answer = "Новостей на IRN за сегодня нет, будем ждать"

    return(today_news_answer)