import requests
from bs4 import BeautifulSoup
from datetime import datetime
import emoji

def erz_parser():

    today_day = str(datetime.today().day)

    erz_url = "https://erzrf.ru/news"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    page = requests.get(erz_url, headers=headers).text

    soup = BeautifulSoup(page, features="html.parser")
    news = soup.find_all("div", {"class": "preview"})

    news_result = []

    for i in news:
        title = i.find("h3").getText()
        link = rf"https://erzrf.ru{i.find('h3').find('a')['href']}"
        day = i.find("span", {"class": "preview__date"}).getText().split()[0]

        if today_day == day:
            news_result.append(
                emoji.emojize(":white_small_square:") + f"""<a href="{link}">{title}</a>\n\n"""
            )

    if len(news_result) != 0:
        answer = emoji.emojize(":newspaper:") + " <b>Последние новости с ЕРЗ РФ:</b>\n\n"
        for i in news_result:
            answer += i
    else:
        answer = "Новостей с ЕРЗ РФ сегодня нет, ждем"

    return(answer)