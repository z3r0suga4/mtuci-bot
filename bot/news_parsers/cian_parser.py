import requests
from bs4 import BeautifulSoup
from datetime import datetime
import emoji

def cian_parser():

    cian_url = "https://www.cian.ru/magazine/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    page = requests.get(cian_url, headers=headers).text

    soup = BeautifulSoup(page, features="html.parser")
    news = soup.find_all("div", attrs={"data-web-ui-test-id": "NewsItem"})

    news_result = []

    for i in news:
        title = i.find("a").getText()
        link = i.find("a")['href']
        link = f"https://cian.ru{link}"
        day = i.find("span").getText().split()[0]

        if "сегодня" == day:
            news_result.append(
                emoji.emojize(":white_small_square:") + f"""<a href="{link}">{title}</a>\n\n"""
            )

    if len(news_result) != 0:
        answer = emoji.emojize(":newspaper:") + " <b>Последние новости с Циан:</b>\n\n"
        for i in news_result:
            answer += i
    else:
        answer = "Новостей с Циан сегодня нет, ждем"

    return(answer)