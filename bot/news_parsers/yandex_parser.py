import requests
from bs4 import BeautifulSoup
import emoji

def yandex_parser():

    yandex_url = "https://realty.ya.ru/journal/category/news/"

    # Создаем сессию
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    # Получаем главную страницу, чтобы получить cookies
    response = session.get(yandex_url,  headers=headers)

    # Если сайт использует cookies для идентификации, они сохранятся в session
    # Теперь можно отправить запрос с сессией и cookies
    response = session.get(yandex_url, headers=headers)

    # Парсим страницу с BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    news = soup.find_all("li", {"class" : "Stack__item--3lIJi"})

    title_classes="Actionable__container--2lWIt Link__root--1lcJQ Link__neutral--36czI MediumPreviewPostRightText__titleLink--kMFOY"
    span_classes="ResettingMarkupTextStyles__root--pISsj Text__gray--2Nf-t Text__body5--1P4EW Text__blockModel--3gAQF MediumPreviewPostRightText__date--HwgNv"

    news_result = []

    for i in news:

        title = i.find("a", class_=title_classes)
        if title is not None:
            link = title['href']
            link = f"https://realty.ya.ru{link}"
            title = title.getText()
            news_time = i.find("span", class_=span_classes)
            if news_time is not None:
                news_time = news_time.getText()
            
            if len(news_time.split(":")) == 2:
                news_result.append(
                emoji.emojize(":white_small_square:") + f"""<a href="{link}">{title}</a>\n\n"""
            )
        
    if len(news_result) != 0:
        answer = emoji.emojize(":newspaper:") + " <b>Новости с Я.Недвижимость за сегодня:</b>\n\n"
        for i in news_result:
            answer += i
    else:
        answer = "Новостей с Я.Недвижимость сегодня нет, ждем"

    return(answer)