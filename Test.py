#тестовый файл для запуска парсинга.не относится к проекту.
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url_template = "https://7days.ru/astro/horoscope/aries/today"
r=requests.get(url_template)
# print(r.status_code)
# print(r.text)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find('div',class_="horoscope-7days__content_text") 
print(vacancies_names.text)
