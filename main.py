# requests - это библиотека помогает нам работать с http запросами
# bs - это библотека позвляет нам извлекать инфомация их html
# данная библотека разбирается в тэгом ,различает от обычного текста
# она может извелачть данные из нужных нам тэгом

import requests
import csv
from bs4 import BeautifulSoup as BS
def get_html(url:str) ->str:
    response = requests.get(url)
    return response.text

# print(get_html("https://google.com/"))

def get_data(html):
    soup = BS(html , 'lxml')
    catalog = soup.find('div' , class_='catalog-list')
    cars=catalog.find_all('a' , class_='catalog-list-item')
    for car in cars:
        try:
            title = car.find('span' , 'catalog-item-caption').text.strip()
            print(title)
        except:
            title = ''
        try:
            price = car.find('span', class_='catalog-item-price').text.split()
        except:
            price = ''
        try:
            img = car.find('img',class_='catalog-item-cover-img').get('src')
        except:
            img = ''
        try:
            desc = car.find('span' , class_= 'catalog-item-descr').text.split()
        except:
            desc = ''
        data = {'title': title,'price':price,'img':img,'desc':desc}



def main():
    # url = 'https://cars.kg/offers'
    # html = get_html(url)
    # data = get_data(html)
    for page in range(1,20):
        url = f'https://cars.kg/offers{page}'
        print(f'Парсинг {page} Старницы')
        html = get_html(url)
        get_data(url)
        print(f'Парсинг {page} Завершен')

def write_csv(data:dict)->None:
    with open('cars.csv' , 'a') as csv_file:
        filednames = ['title','price','image']
        writer = csv.DictWriter(csv_file,delimiter=',',filednames=filednames)
        write.writerow(data)

main()