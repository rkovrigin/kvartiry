import urllib
from lxml import html
import unicodedata

url = "http://www.naidi-kvartiru.ru/search?rooms=2&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&keywords=&sort=0&photo=0&page="
cian = "http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=4&city[0]=1&type=-2&wp=1&room2=1&foot_min=10&only_foot=2"

page = html.fromstring(urllib.urlopen(url + '1').read())
cPage = html.fromstring(urllib.urlopen(cian).read())

links = page.xpath("//html/body/div[2]/div[h5/text()!='']")
cLink = page.xpath("//*[@id='dl2m_9543806_metro']/text()")

# /html/body/div[2]/div[2]/h5/text()
# /html/body/div[2]/div[3]/h3/a
# 'lxml.html.HtmlElement'
#print len(links)
line = "";
f1 = open("text1.txt", 'w')
#for i in links:
	#x = i.xpath("h3/a")
	#y = x[0]
	#line = y.text
	#line2 = line.encode('latin1', 'ignore')
	##line2 = line2.replace("\r\n", "")
	##print line2.replace("\xc3", "")
	#print line2
	#f1.write(line2)

	##print unicodedata.normalize('NFKD', line)
print cLink
