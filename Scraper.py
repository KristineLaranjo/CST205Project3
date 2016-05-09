from bs4 import BeautifulSoup
import requests

subject = "cats"

for num in range(1,20):
    r  = requests.get("http://www.istockphoto.com/photos/%s?pageNumber':1,'" % (subject))
    data = r.text
    soup = BeautifulSoup(data, "lxml")


    for link in soup.find_all("img"):
        print(link.get('src'))