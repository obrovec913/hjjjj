from bs4 import BeautifulSoup
import json
import requests


re = open('Japanese Diapers Shop _ Lowest Prices in Europe + Free Shipping.html', encoding="utf-8").read()


soup = BeautifulSoup(re, 'lxml')
quotes = soup.find_all('div', class_='product-element-top')
iten = []
for pr in quotes:
    url = pr.find('a').get('href')
    res = requests.get(url).text
    d = url.split('/')
    with open(f"sr\\{d[-2]}.html", 'w', encoding='utf-8')as  fi:
        fi.write(res)

    sou = BeautifulSoup(res, 'lxml')
    quo = sou.find_all('div', class_='summary-inner')
    for i in quo:
        he = i.find('h1').text
        p = i.find('p').text
        o = i.find('div',  class_='woocommerce-product-details__short-description').text
        iten.append({"heading": he, "price":p, "description":o})

    print("шаг")        


with open("products.json", 'w', encoding='utf-8')as  fi:
    json.dump(iten, fi, indent=3, ensure_ascii=False)
