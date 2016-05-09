from bs4 import BeautifulSoup
import requests


def getimage(subject):
    r  = requests.get("http://emojipedia.org/%s" % (subject))
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all("img"):
        return link.get('src')
