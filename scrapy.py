from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import pdfkit

url = "https://www.hackerearth.com/practice/python/getting-started/input-and-output/tutorial/"
newpath = r'/home/soumya/hackearth/python/'
# r'^/practice/python/[a-z-]+\/[a-z0-9-]+/$'
regularExpression = re.compile(r'^/practice/python/getting-started/[a-z0-9-]+/$')
urlList = []


def getUrlList():
    content = urlopen(url).read()
    soup = BeautifulSoup(content)
    for link in soup.find_all('a'):
        if regularExpression.search(str(link.get('href'))) and (not link.get('href') in urlList):
            urlList.append(link.get('href'))
    #print(urlList)


def getTutorial():
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        counter = 1
        for urls in urlList:
            pdfkit.from_url("https://www.hackerearth.com" + urls, str(newpath) + 'Topic' + str(counter) + '.pdf')
            counter += 1


getUrlList()
getTutorial()
