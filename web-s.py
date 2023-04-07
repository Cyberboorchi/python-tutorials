from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from bs4 import BeautifulSoup
import pandas as pd

#driver = webdriver.Chrome("C:\\wamp64\\www\\python\\chromedriver.exe")

products = []
prices = []
ratings = []
driver.get('<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq')

content = driver.page_sources
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':_31qSD5}):
    name=a.find('div',attrs={'class':_4rR01T})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    # ratings.append(rating.text) 