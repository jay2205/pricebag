import requests
from bs4 import BeautifulSoup
url = "http://www.amazon.com/Apple-iPhone-5s-A1453-Space/dp/B00F3J0LPM"
ebay_url = "http://www.ebay.com/itm/Apple-iPhone-5s-Factory-Unlocked-Smartphone-Gold-Grey-Silver-16GB-32GB-64GB-/141541457648?pt=LH_DefaultDomain_0&var=&hash=item20f4873ef0"
try:
    r = requests.get(url)
    ebay_r = requests.get(ebay_url)
    #amazon details
    soup = BeautifulSoup(r.content)
    title = soup.find_all('span', {'id':'productTitle'})
    print title[0].text
    href = soup.find('span', {'id':'acrPopover'})['title']
    print href
    cost = soup.find_all('span',{'class':'a-color-price'})
    print cost[1].text
    print cost[0].text
    print url
    #ebay details
    soup_ebay = BeautifulSoup(ebay_r.content)
    ebay_title = soup_ebay.find_all('h1',{'id':'itemTitle'})
    print ebay_title[0].text
    ebay_cost = soup_ebay.find_all('span',{'id':'prcIsum'})
    print ebay_cost[0].text
    print ebay_url
except requests.exceptions.ConnectionError as e:
    print "These aren't the domains we're looking for."
