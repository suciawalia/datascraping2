from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels")

now = datetime.now()
booklist = []
i = 1
while i<=100:
    for book in driver.find_elements_by_tag_name("tr"):
        print(book.text.split("\n"))
        for img in book.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            booklist.append(
                {"No": book.text.split("\n")[0],
                "Title": book.text.split("\n")[1],
                "Author": book.text.split("\n")[2],
                "Rating": book.text.split("\n")[3],
                "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S\n"),
                "Image": img.get_attribute("src")
                    }
                )

hasil_scraping = open("hasilscraping.json", "w")
json.dump(booklist, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()