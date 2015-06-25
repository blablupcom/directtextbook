from bs4 import BeautifulSoup as bs
from datetime import datetime
import unirest
import scraperwiki
from random import randint
from time import sleep
import re

names = ['Amazon Trade-In', 'Valore', 'Textbooks.com', 'TextbookRush', 'Textbook Recycling', 'Bookbyte']
user_agent = {'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}

def takeprice(name):
    textbook = ''
    try:
         textbook = soup.find( text=re.compile('{}'.format(name)))
    except: pass
    price = ''
    if textbook:
        try:
             price = textbook.find_next('td', attrs={'align': 'right'}).text.split('$')[-1]
        except:pass
    return price.strip()

with open('eans.txt') as f:
    for url in f: # read every url from the list of urls of the file named ean
        sleep(randint(5,90))   # random sleep between requests from 5 sec to 90 sec
        try:
           pages = unirest.get(url.strip(), headers = user_agent)  # make a request to the url
        except: continue
        soup = bs(pages.raw_body)
        ean = url.split('=')[-1]
        todays_date = str(datetime.now()) # fix the time
        price_amaz = takeprice(names[0])
        price_val = takeprice(names[1])
        price_txcom = takeprice(names[2])
        price_txt = takeprice(names[3])
        price_rec = takeprice(names[4])
        price_bkb = takeprice(names[-1])
        print price_amaz, price_val, price_txcom, price_txt, price_rec, price_bkb
        scraperwiki.sqlite.save(unique_keys=["ean"], data={"ean": ean.strip(), 'date': todays_date, 'Amazon Trade-In': price_amaz, 'Valore': price_val, 'Textbookscom': price_txcom, 'TextbookRush':  price_txt, 'Textbook Recycling':price_rec, 'Bookbyte': price_bkb })
