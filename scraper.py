#from unittest import result

# from email.utils import getaddresses
# from socket import getnameinfo
from bs4 import BeautifulSoup
import requests

# take the form data and plug it into BS4 and scrape the data

html_text = requests.get('https://vancouver.craigslist.org/search/apa')
soup = BeautifulSoup(html_text.content, 'lxml')
# ---test---
# houses = soup.find('h3', class_='result-heading')
# print(houses)
# card = result.find('div' ,class_='result-info')
# address = card.find('span', class_='result-hood').text
# print(address)

def get_address(addr):
    address_All = soup.find_all('span', class_='result-hood')

    arr = [len(address_All)]

    for address in address_All:
        address = address.text
        if addr in address:
            arr.append(address)
    return(arr)
    


    # for address in addresses:
    #     print(address)

def get_Name():
    names = soup.find_all('a', class_='result-title hdrlnk')
    for name in names:
        print(name.text.strip())

def get_date():
    upload_dates = soup.find_all('time', class_='result-date')
    for date in upload_dates:
        # print(date.text)
        return(date.text)






print(get_address("vancouver"))
# get_address("vancouver")
  
# get_Name()
# print(get_date())