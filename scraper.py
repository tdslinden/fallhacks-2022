from bs4 import BeautifulSoup
import requests
# take the form data and plug it into BS4 and scrape the data


def find_Upper_Price(rent):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getPrices = soup.find_all('span', class_='result-price')
    arr = []
    # print(len(getPrices))
    for prices in getPrices:
        if int(prices.text.replace(',', '').replace('$', '')) <= rent:
             arr.append(int(prices.text.replace(',', '').replace('$', '')))
      # prices = getPrices.text
        # if (prices != None and int(prices.text) <= rent):
        #   print("here")
    return arr


def housing(bedroom):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getBedroom = soup.find_all('span', class_='housing')
    arr = []
    # print(len(getBedroom))
    for room in getBedroom:
        #prices = getPrices.text
        arr.append(room.text.strip()[0])
    return arr

find_Upper_Price(4500)
#housing(3)
