import requests
from bs4 import BeautifulSoup
url = "http://www.amazon.com/Samsung-Galaxy-S6-Sapphire-Sprint/dp/B00V7FWBZY"
ebay_url = "http://www.ebay.com/itm/Samsung-Galaxy-S6-Edge-SM-G925-FACTORY-UNLOCKED-5-1-QHD-Black-White-/371285593904?pt=LH_DefaultDomain_0&var=&hash=item5672588f30"
try:
    r = requests.get(url)
    ebay_r = requests.get(ebay_url)
    #amazon details
    soup = BeautifulSoup(r.content)
    title = soup.find_all('span', {'id':'btAsinTitle'})
    print title[0].text
    #print title
    href = soup.find('span', {'class':'swSprite s_star_4_0 '})['title']
    print href
    cost = soup.find_all('span',{'id':'current-price'})
    #print cost[1].text
    print cost[0].text
    #print cost[2].text
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
