from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

mainCounter = 0

albumLink = []  # List to store link of the album
albumName = []  # List to store name of the album
artists = []  # List to store artists of the album

for x in range(50):
    pageLink = "https://cazkolik.com/turk-caz-albumleri?page=" + str(x+1)
    driver.get(pageLink)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    albumCountInPage = 0
    for h in soup.findAll('h4', attrs={'class': 'post_title'}):
        albumRouteLink = h.find('a', href=True)
        albumName.append(albumRouteLink.get_text())
        albumLink.append(albumRouteLink.get('href'))
        albumCountInPage += 1
    print("ALBUM COUNT IN THIS PAGE = ", albumCountInPage)
    counter = 0
    for y in range(albumCountInPage):
        link = "https://cazkolik.com" + albumLink[y + x*24]
        driver.get(link)
        soup2 = BeautifulSoup(driver.page_source, "html.parser")

        for h in soup2.findAll('p'):
            a = h.next.next
            if counter == 1:
                artists.append(a.next)
                print(a.next)
                counter = 0
                break
            counter += 1
            mainCounter += 1
            print(mainCounter)





print(len(artists))

#her linke gidince sanatcılar kısmını da arraylere ekleyip diğer sayfaya geçince '*' karakteri eklenebilir
#daha sonra substringle ayrım ypaılabilir.