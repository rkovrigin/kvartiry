import urllib
import codecs
from lxml import html
import unicodedata

url = "http://www.naidi-kvartiru.ru/search?rooms=2&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&keywords=&sort=0&photo=0&page="
cian = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=4&city[0]=1&type=-2&wp=1&room2=1&foot_min=10&only_foot=2"

page = html.fromstring(urllib.urlopen(url + '1').read())
cPage = html.fromstring(urllib.urlopen(cian).read())

links = page.xpath("//html/body/div[2]/div[h5/text()!='']")
cLink = page.xpath("//*[@id='dl2m_9543806_metro']/text()")

# cian xpath //*[@id="dl2m_9745552_metro"]/a[3]
#//*/id/a[3]
#//*[@id="dl2m_9649395_metro"]/a[3]
urlCian = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=0&city[0]=1&type=-2&wp=1&room2=1&foot_min=15&only_foot=2&cl=-1&p=1"
#//*[@id="tbody"]/tbody/tr/td/table/tbody/tr/td/div[1]/fieldset/table[2]/tbody/tr/

for i in range(1):
	metro = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=" + str(i+1) + "&city[0]=1&type=-2&wp=1&room2=1&foot_min=15&only_foot=2&cl=-1&p=1"
	
	page = html.fromstring(urllib.urlopen(metro).read())
	#block with appartments
	#linkStation = page.xpath("//*[@*]/a[3]")
	blocks = page.xpath("//*[contains(@id,'tr_')]")
	print "%d %d %s" % (len(blocks), i+1, "")

	for j in blocks:
		#price = j.xpath("//*[contains(@id, '_price')]")
		#print "%d %s" % (len(price), price[2].text)
		#print type(j)
		#print len(j)
		print j[4].text

	#//*[@id="dl2m_9649395_price"]/text()[1]
	#//*[@id="dl2m_9649395_price"]/text()[2]
# price block
#//*[@id="dl2m_9649395_price"] 
	# block = ""
	# linkPrice = page.xpath("//*[@=*_price]//text()[1]")
	# if (len(linkPrice) > 0 ):
	# 	print "%d %d %s" % (len(linkPrice), i+1, "")
	# 	for j in linkPrice:
	# 		block = block + j.encode('ascii','ignore')
	# print block
