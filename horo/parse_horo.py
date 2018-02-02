import requests

from bs4 import BeautifulSoup


def get_horoscope(sign, interval):
    """sign : string contains lowercase zodiac sign ex. capricon
    interval : yesterday, today, tomorrow, week, year
    """
    mail_url = 'https://horo.mail.ru/prediction/{sign}/{interval}/'
    r = requests.get(mail_url.format(sign=sign, interval=interval))
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.select_one('.article__text').text.strip()
