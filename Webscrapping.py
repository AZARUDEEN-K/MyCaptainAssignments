import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090"

req = requests.get(url)

Soup = BeautifulSoup(req.content,"html.parser")

Model = Soup.find_all("h1",{"class":"product-title"})[0].get_text()
print(Model)
