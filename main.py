from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

albumLink = []  # List to store name of the product
albumName = []  # List to store price of the product
artists = []  # List to store rating of the product

driver.get("https://cazkolik.com/turk-caz-albumleri?page=1")

soup = BeautifulSoup(driver.page_source, "html.parser")


for h in soup.findAll('h4', attrs={'class': 'post_title'}):
    albumRouteLink = h.find('a', href=True)
    albumName.append(albumRouteLink.get_text())
    albumLink.append(albumRouteLink.get('href'))
    print(albumRouteLink.get_text())

#her linke gidince sanatcılar kısmını da arraylere ekleyip diğer sayfaya geçince '*' karakteri eklenebilir
#daha sonra substringle ayrım ypaılabilir.