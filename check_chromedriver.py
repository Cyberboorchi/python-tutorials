from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import io


options = Options()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

#driver.get("https://www.google.com")
#driver.get("https://www.news.mn")

driver.get("https://www.apu.mn")

content = driver.page_source

#print("Content", content)


#with io.open("google_home1.html", "w", encoding="utf-8") as f:
#with io.open("news_mn_home1.html", "w", encoding="utf-8") as f:
with io.open("transbank_mn_home1.html", "w", encoding="utf-8") as f:
    file = f.write(content) 
    
#file.write(content) 
#file.close() 

