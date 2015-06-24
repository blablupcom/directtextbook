from datetime import datetime
from bs4 import BeautifulSoup as bs
import unirest
import scraperwiki
from random import randint
from time import sleep
import os.path

names = {'Amazon Trade-In', 'Valore', 'Textbooks.com', 'TextbookRush', 'Textbook Recycling', 'Bookbyte'}
user_agent = {'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}

with open('eans.txt') as f:
    for url in f: # read every url from the list of urls of the file named ean
        sleep(randint(5,90))   # random sleep between requests from 5 sec to 90 sec
        try:
           pages = unirest.get(url.strip(), headers = user_agent)  # make a request to the url
        except: continue
        soup = bs(pages.raw_body)
        vendornames = soup.find_all('a', 'vendorname')   # finding all vendors tags
        for vendorname in vendornames:
            ean = url.split('=')[-1]
            name =''
            price = ''
            try:
                name = vendorname.text    # getting name of vendors
                if name in names:     # if a vendor name in the set of vendors names called names
                    todays_date = str(datetime.now()) # fix the time
                    try:
                        price = vendorname.find_next('span', 'status').strong.text  # get price for this vendor
                        print ean, name, price
                        scraperwiki.sqlite.save(unique_keys=['date'], data={"ean": ean, "name":name, "price": price, "date": todays_date }) # save data into sql database
                    except: pass
            except: pass
