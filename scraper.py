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

    arr_add = [len(address_All)]
    if(addr != ''):
        for address in address_All:
            address = address.text
            if addr in address:
                arr_add.append(address)
    print(arr_add)
    return(arr_add)



    # for address in addresses:
    #     print(address)

def get_Name():
    names = soup.find_all('a', class_='result-title hdrlnk')
    arr_name = [len(names)]
    for name in names:
        arr_name.append(name)
    print(name.text.strip())
    return(arr_name)

def get_date():
    upload_dates = soup.find_all('time', class_='result-date')
    arr_date = [len(upload_dates)]
    for date in upload_dates:
        # print(date.text)
        arr_date.append(date.text)
        # return(date.text)
    print(arr_date)
    return(arr_date)




get_address("vancouver")
# get_address("vancouver")
  
get_Name()
get_date()