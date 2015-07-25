#J. van der Linde
#Steam Marketplace Price Watcher
#Last updated 2015-07-24

import urllib
import re
import time
import sched
import sys
import datetime

#==============================================================
#As a user, the lines below are all you need to change
appid = '570'                   #570 is DOTA2
item_name = 'Faceless%20Rex'    #Item name as found in web URL
ideal_price = 20                #Ideal price in USD
check_timeout = 10              #Delay between checks in seconds
#Don't mess with anything below this line unless you're a programmer
#==============================================================

lowest_recorded = 999999999

def getPrices():
    global lowest_recorded
    url = 'http://steamcommunity.com/market/priceoverview/?currency=1&appid=' + appid + '&market_hash_name=' + item_name
    regex_pattern = re.compile('\"lowest_price\":.*?([0-9]+\.[0-9]*)', re.IGNORECASE|re.DOTALL)
    page = urllib.urlopen(url).read()

    regex_matches = regex_pattern.findall(page)
    price = float(regex_matches[0])
    if price < lowest_recorded:
        lowest_recorded = price

    if (price <= ideal_price):
        print "Lowest Price: USD$ " + str(price) + "\t<===== Lower than your ideal price! Buy!"
    else:
        print "Lowest Price: USD$ " + str(price) + "\t" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\tRecord Low: USD$ " + str(lowest_recorded)
    sys.stdout.flush()

    time.sleep(check_timeout)
    getPrices()

getPrices()
