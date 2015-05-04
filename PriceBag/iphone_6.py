from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import cgitb; cgitb.enable()
app = Flask(__name__)
@app.route('/iphone6')
def iphone6():
    #try:
        #return render_template("index.html")
    #except Exception, e:
    #    return str(e)
#def iphone5s():
    url = "http://www.amazon.com/Apple-iPhone-Space-Gray-Unlocked/dp/B00NQGP42Y"
    ebay_url = "http://www.ebay.com/itm/Apple-iPhone-6-Gold-Space-Grey-Silver-AT-T-Sprint-Verizon-T-Mobile-A1549/371286745620?_trksid=p2047675.c100005.m1851&_trkparms=aid%3D222007%26algo%3DSIC.MBE%26ao%3D1%26asc%3D30542%26meid%3D70f3a70689bc427f8037cc7101f2c5fa%26pid%3D100005%26rk%3D3%26rkt%3D6%26mehot%3Dpp%26sd%3D151651459593&rt=nc"
    try:
        r = requests.get(url)
        ebay_r = requests.get(ebay_url)
        #amazon details
        soup = BeautifulSoup(r.content)
        title = soup.find_all('span', {'id':'productTitle'})
        #print title[0].text
        href = soup.find('span', {'id':'acrPopover'})['title']
        print href
        cost = soup.find_all('span',{'class':'a-color-price'})
        print  cost[1].text
        print  cost[0].text
        print  url
        #ebay details
        soup_ebay = BeautifulSoup(ebay_r.content)
        ebay_title = soup_ebay.find_all('h1',{'id':'itemTitle'})
        #print ebay_title[0].text
        ebay_cost = soup_ebay.find_all('span',{'id':'prcIsum'})
        print ebay_cost[0].text
        return render_template('iphone6.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."


if __name__ == "__main__":
 app.run(debug=True)
