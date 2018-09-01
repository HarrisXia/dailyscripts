#encoding:UTF-8
import urllib.request
import codecs
import re
from bs4 import BeautifulSoup           # HTML
from bs4 import BeautifulStoneSoup      # XML
import bs4                              # ALL
f=codecs.open('/home/harris/dblr/nips2015.txt','w','utf-8')
def GetAuthorandTitle(doc):                                                         
    soup = BeautifulSoup(doc)
    #for author in soup.findAll('span',{'itemprop':'author'}):
        #f.write(str(author.contents[0].contents[0].contents[0]))
        #f.write(", ")
    #f.write("# ")
    for title in soup.findAll('span',{'class':'title'}):
        f.write(str(title.contents[0]))
    f.write("\n")
for x in range(2015,2016):
    url='http://dblp.uni-trier.de/db/conf/nips/nips'+ '%d' %x+'.html'
    print(x)
    data= urllib.request.urlopen(url).read()
    data = data.decode('UTF-8','ignore')
    so = BeautifulSoup(data)
    for div in so.findAll('div',{'class':'data'}):
            # print(div.contents)
        # print(''.join(str(div.contents)))
        GetAuthorandTitle(''.join(str(div.contents)))
f.close()