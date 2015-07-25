#J. van der Linde
#Steam Marketplace Price Watcher
#Last updated 2015-07-24

import urllib
import re
import time
import sched
import sys
import datetime
import winsound

#==============================================================
#As a user, the lines below are all you need to change
steam_market_url = 'http://steamcommunity.com/market/listings/570/Faceless%20Rex'
ideal_price = 25                #Ideal price in USD
check_timeout = 10              #Delay between checks in seconds
#Don't mess with anything below this line unless you're a programmer
#==============================================================

lowest_recorded = 999999999

def getPrices():
    global lowest_recorded

    regex_extract = re.compile('/market/listings/([0-9]+)/(.+)$', re.IGNORECASE|re.DOTALL)
    extract_matches = regex_extract.findall(steam_market_url)
    appid = str(extract_matches[0][0])
    item_name = str(extract_matches[0][1])
    
    url = 'http://steamcommunity.com/market/priceoverview/?currency=1&appid=' + appid + '&market_hash_name=' + item_name
    regex_pattern = re.compile('\"lowest_price\":.*?([0-9]+\.[0-9]*)', re.IGNORECASE|re.DOTALL)
    page = urllib.urlopen(url).read()

    regex_matches = regex_pattern.findall(page)
    price = float(regex_matches[0])
    if price < lowest_recorded:
        lowest_recorded = price
        winsound.Beep(2000, 700)

    if (price <= ideal_price):
        print "Lowest Price: USD$ " + str(price) + "\t<===== Lower than your ideal price! Buy!"
        winsound.Beep(2000, 4000)
    else:
        print "Lowest Price: USD$ " + str(price) + "\t" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\tRecord Low: USD$ " + str(lowest_recorded)
    sys.stdout.flush()

    time.sleep(check_timeout)
    getPrices()

getPrices()
