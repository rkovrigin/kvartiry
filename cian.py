import urllib
import codecs
from lxml import html
import unicodedata

cian = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=4&city[0]=1&type=-2&wp=1&room2=1&foot_min=10&only_foot=2"

cPage = html.fromstring(urllib.urlopen(cian).read())

urlCian = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=0&city[0]=1&type=-2&wp=1&room2=1&foot_min=15&only_foot=2&cl=-1&p=1"

for i in range(10):
	metro = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=" + str(i+1) + "&city[0]=1&type=-2&wp=1&room2=1&foot_min=15&only_foot=2&cl=-1&p=1"

	page = html.fromstring(urllib.urlopen(metro).read())
	#block with appartments
	blocks = page.xpath("//*[contains(@id,'tr_')]")
	#print "%d %d %s" % (len(blocks), i+1, "")

	for j in blocks:
		#money j[4].text
		#metro j[1][6].text
		price = (j[4].text)
		price2 = int((price.split(','))[0])
		try:
			metro = j[1][6]
		except:
			metro = "none"

		if (price2 <= 40 and price2 > 0 and metro != "none"):
			print "%d %s" % (price2, metro.text)