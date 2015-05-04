from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import cgitb; cgitb.enable()
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/phones')
def phone():
    return render_template('phone.html')
@app.route('/iphone5s')
def iphone5s():
    url = "http://www.amazon.com/Apple-iPhone-5s-A1453-Space/dp/B00F3J0LPM"
    ebay_url = "http://www.ebay.com/itm/Apple-iPhone-5s-Factory-Unlocked-Smartphone-Gold-Grey-Silver-16GB-32GB-64GB-/141541457648?pt=LH_DefaultDomain_0&var=&hash=item20f4873ef0"
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
        #print ebay_cost[0].text
        return render_template('iphone5.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."

@app.route('/iphone6')
def iphone6():
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
        #print ebay_cost[0].text
        return render_template('iphone6.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."

@app.route('/iphone6plus')
def iphone6plus():
    url = "http://www.amazon.com/Apple-iPhone-Plus-Gold-Unlocked/dp/B00NQGONB2"
    ebay_url = "http://www.ebay.com/itm/Apple-iPhone-6-Plus-16GB-Factory-GSM-and-CDMA-Unlocked-Smartphone-Model-A1524-/271813956519?pt=LH_DefaultDomain_0&var=&hash=item3f495fd3a7"
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
        #print ebay_cost[0].text
        return render_template('iphone6+.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."

@app.route('/samsungs5')
def samsungs5():
    url = "http://www.amazon.com/Samsung-SM-G900H-Factory-Unlocked-International/dp/B00J4TK4B8"
    ebay_url = "http://www.ebay.com/itm/Samsung-Galaxy-S5-SM-G900V-16GB-Unlocked-Black-White-Gold-Blue-/151651459667?pt=LH_DefaultDomain_0&var=&hash=item234f21a253"
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
        #print ebay_cost[0].text
        return render_template('s5.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."

@app.route('/note4')
def note4():
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
        #print ebay_cost[0].text
        return render_template('s6.html',az_t = title[0].text,az_rate = href, az_cst1=cost[1].text,az_cst2=cost[2].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."

@app.route('/samsung_s6_edge')
def s6():
    url = "http://www.amazon.com/Samsung-Galaxy-S6-Sapphire-Sprint/dp/B00V7FWBZY"
    ebay_url = "http://www.ebay.com/itm/Samsung-Galaxy-S6-Edge-SM-G925-FACTORY-UNLOCKED-5-1-QHD-Black-White-/371285593904?pt=LH_DefaultDomain_0&var=&hash=item5672588f30"
    try:
        r = requests.get(url)
        ebay_r = requests.get(ebay_url)
        #amazon details
        soup = BeautifulSoup(r.content)
        title = soup.find_all('span', {'id':'btAsinTitle'})
        #print title[0].text
        href = soup.find('span', {'class':'swSprite s_star_4_0 '})['title']
        #print href
        cost = soup.find_all('span',{'id':'current-price'})
        #print  cost[1].text
        #print  cost[0].text
        #print  url
        #ebay details
        soup_ebay = BeautifulSoup(ebay_r.content)
        ebay_title = soup_ebay.find_all('h1',{'id':'itemTitle'})
        #print ebay_title[0].text
        ebay_cost = soup_ebay.find_all('span',{'id':'prcIsum'})
        #print ebay_cost[0].text
        return render_template('se6.html',az_t = title[0].text,az_rate = href, az_cst1=cost[0].text,az_url=url,e_t= ebay_title[0].text,e_cst = ebay_cost[0].text,e_url=ebay_url)
        #print "Content-Type: text/html"
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."


if __name__ == "__main__":
 app.run(debug=True)
