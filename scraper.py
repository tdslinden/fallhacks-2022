from bs4 import BeautifulSoup
import requests
# take the form data and plug it into BS4 and scrape the data


def find_Upper_Price(rent):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getPrices = soup.find_all('span', class_='result-price')
    # print(len(getPrices))
    for prices in getPrices:
        if int(prices.text.replace(',', '').replace('$', '')) <= rent:
            print(int(prices.text.replace(',', '').replace('$', '')))
      # prices = getPrices.text
        # if (prices != None and int(prices.text) <= rent):
        #   print("here")


def housing(bedroom):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getBedroom = soup.find_all('span', class_='housing')
    # print(len(getBedroom))
    for room in getBedroom:
        #prices = getPrices.text
        print(room.text.strip()[0])


find_Upper_Price(4500)
#housing(3)
