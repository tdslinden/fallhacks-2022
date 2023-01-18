# from unittest import result
# from email.utils import getaddresses
# from socket import getnameinfo
from bs4 import BeautifulSoup
import requests
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        upper_price = request.form['max_price']
        address = request.form['city']
        bedroom = request.form['bed']
        output(find_Upper_Price(upper_price), get_Name(),
               get_date(), get_address(address), bed(bedroom))
        return redirect(url_for('output'))
    else:
        return (render_template('index.html'))
# take the form data and plug it into BS4 and scrape the data


@app.route('/output')
def output():
    return render_template('output.html')


html_text = requests.get('https://vancouver.craigslist.org/search/apa')
soup = BeautifulSoup(html_text.content, 'lxml')
# ---test---
# houses = soup.find('h3', class_='result-heading')
# print(houses)
# card = result.find('div' ,class_='result-info')
# address = card.find('span', class_='result-hood').text
# print(address)


def find_Upper_Price(rent):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getPrices = soup.find_all('span', class_='result-price')
    arr = []
    # print(len(getPrices))
    for prices in getPrices:
        if int(prices.text.replace(',', '').replace('$', '')) <= int(rent):
            arr.append(int(prices.text.replace(',', '').replace('$', '')))
     # prices = getPrices.text
        # if (prices != None and int(prices.text) <= rent):
        #   print("here")
    return arr


def bed(bedroom):
    html_text = requests.get(
        'https://vancouver.craigslist.org/search/apa?sort=date&')
    soup = BeautifulSoup(html_text.content, 'lxml')
    getBedroom = soup.find_all('span', class_='housing')
    arr = []
    # print(len(getBedroom))
    for room in getBedroom:
        # prices = getPrices.text
        if int(room.text.strip()[0]) < int(bedroom):
            arr.append(room.text.strip()[0])
    return arr


def get_address(addr):
    address_All = soup.find_all('span', class_='result-hood')

    arr_add = []
    if (addr != ''):
        for address in address_All:
            address = address.text
            if addr in address:
                arr_add.append(addr)

    return (arr_add)

    # for address in addresses:
    #     print(address)


def get_Link():
    arr_link = []
    link_All = soup.find_all('a', class_='result-image gallery')
    for link in link_All:
        arr_link.append(link['href'])
    return arr_link

def get_Name():
    names = soup.find_all('a', class_='result-title hdrlnk')
    i = 0

    arr_name = []
    while (i < len(names)):
        name = names[i]
        arr_name.append(name.text)
        i += 1
    return (arr_name)


def get_date():
    upload_dates = soup.find_all('time', class_='result-date')
    arr_date = []
    for date in upload_dates:
        # print(date.text)
        arr_date.append(date.text)
        # return(date.text)
    return (arr_date)


def output(price, name, date, address, bed):
    # print(name)
    arr = []
    link_All = get_Link()
    html = """"""
    i = 0
    arr.append(len(price))
    arr.append(len(name))
    arr.append(len(price))
    arr.append(len(name))
    arr.append(len(date))
    arr.append(len(address))
    arr.append(len(bed))
    # print(len(price) + len(name) + len(date) + len(address) + len(bed))
    while (i < min(arr)):
        p = str(price[i])
        n = str(name[i])
        d = str(date[i])
        a = str(address[i])
        b = str(bed[i])
        # html += f"""
        # <td> {p} </td>
        # <td> {n} </td>
        # <td> {d} </td>
        # <td> {a} </td>
        # <td> {b} </td>
        # """
        # new_tag = soup.new_tag('a', href='http://www.example.com')

        soup = BeautifulSoup(open('templates/output.html'), 'html.parser')
        td_tag1 = soup.new_tag('td')
        td_tag1.append(f"${p}")
        td_tag2 = soup.new_tag('td')
        td_tag2.append(f"{n}")
        td_tag3 = soup.new_tag('td')
        td_tag3.append(f"{d}")

        a_tag = soup.new_tag('a', href=f'{link_All[i]}')
        a_tag.append(f"{a}")
        
        td_tag4 = soup.new_tag('td')
        td_tag4.append(a_tag)
        
        td_tag5 = soup.new_tag('td')
        td_tag5.append(f"{b}")

        tr_tag = soup.new_tag('tr')
        tr_tag.append(td_tag1)
        tr_tag.append(td_tag2)
        tr_tag.append(td_tag3)
        tr_tag.append(td_tag4)
        tr_tag.append(td_tag5)
        soup.div.append(tr_tag)
        soup.div.append(soup.new_tag("br"))
        with open("templates/output.html", "w") as file:
            file.write(str(soup))
        i += 1
    # soup = BeautifulSoup(open('templates/output.html'), 'html.parser')
    # div_tag = soup.new_tag("div")
    # div_tag.append(html)
    # soup.div.append(div_tag)
    # with open("templates/output.html", "w") as file:
    #     file.write(str(soup))
    # soup = BeautifulSoup(html)
    # title = soup.find('title')
    # meta = soup.new_tag('meta')
    # meta['content'] = "text/html; charset=UTF-8"
    # meta['http-equiv'] = "Content-Type"
    # title.insert_after(meta)


if __name__ == "__main__":
    app.run(debug=True)
