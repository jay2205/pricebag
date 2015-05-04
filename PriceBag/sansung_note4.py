from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import cgitb; cgitb.enable()
app = Flask(__name__)
@app.route('/note4')
def note4():
    #try:
        #return render_template("index.html")
    #except Exception, e:
    #    return str(e)
#def iphone5s():
    url = "http://www.amazon.com/Samsung-Galaxy-SM-N915F-Factory-Unlocked/dp/B00P8Z25QY"
    ebay_url = "http://www.ebay.com/itm/NEW-Samsung-Galaxy-Note-4-N910H-FACTORY-UNLOCKED-5-7-QHD-32GB-16MP-WHITE-/141501784599?pt=LH_DefaultDomain_0&hash=item20f229e217"
    try:
        r = requests.get(url)
        ebay_r = requests.get(ebay_url)
        #amazon details
        soup = BeautifulSoup(r.content)
        title = soup.find_all('span', {'id':'productTitle'})
        #print title[0].text
        href = soup.find('span', {'id':'acrPopover'})['title']
        #print href
        cost = soup.find_all('span',{'class':'a-color-price'})
        #print  cost[1].text
        #print  cost[0].text
        #print  url
        #ebay details
        soup_ebay = BeautifulSoup(ebay_r.content)
        ebay_title = soup_ebay.find_all('h1',{'id':'itemTitle'})
        #print ebay_title[0].text
        ebay_cost = soup_ebay.find_all('span',{'id':'prcIsum'})
        print ebay_cost[0].text
        return render_template('s6.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."


if __name__ == "__main__":
 app.run(debug=True)
