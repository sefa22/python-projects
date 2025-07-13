from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # entr basmak için 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

options = Options()
options.add_argument("--log-level=3")  # Sadece fatal hataları göster
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Kalan uyarıları da bastır



# Buraya chromedriver.exe'nin doğru path'ini ver
driver_path = "./chromedriver.exe"
service = Service(executable_path=driver_path)
service.creationflags = 0x08000000
browser = webdriver.Chrome(service=service)
browser.get("https://www.google.com/maps/search/super+market+near+washington/@38.9135256,-77.0667162,13z?entry=ttu&g_ep=EgoyMDI1MDcwOC4wIKXMDSoASAFQAw%3D%3D")
# print(browser.page_source) sayfanın kaynak kodunu alırsın   """
#print(browser.title)
browser.fullscreen_window()
# time.sleep(2)
# browser.set_window_size(700, 700)
# time.sleep(2)
# browser.save_screenshot("screenshot.png")
# browser.close() sayfaları tek tek kapatıyor
#browser.quit() hepsini kapatıyor
isim=[]
adress=[]
tel=[]
site=[]
#browser.back() geri gelmek için 
"""for sef in range (3,13,2):
    xpath = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{i}]/div/a'
    browser.find_element(By.XPATH,xpath).click"""
merve=1
# Market listesinin olduğu bölgeyi bul



for i in range(5,75,2):
    if (i - 5) // 2 % 3 == 0 and i != 5:
        scrollable = browser.find_element(By.XPATH, '//div[@role="feed"]')
        for _ in range(2):
            browser.execute_script("arguments[0].scrollTop += 500;", scrollable)
            time.sleep(0.5)
    try:
        browser.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{i}]/div/a').click()
        time.sleep(0.5)
        sef = browser.find_elements(By.CSS_SELECTOR, '.Io6YTe.fontBodyMedium.kR99db.fdkmkc')
        a = "adres yok"
        t = "tel yok"
        s = "not found"
        name = "no name"

        for eleman in sef:
                metin = eleman.text
                sefa = browser.find_element(By.CSS_SELECTOR, '.DUwDvf.lfPIob')
                name = sefa.text

                if metin.startswith("+1"):
                    t = metin
                elif "." in metin and " " not in metin:
                    s = metin
                elif "Washington" in metin or "DC" in metin:
                    a = metin

        isim.append(name)
        adress.append(a)
        tel.append(t)
        site.append(s)

        print(f"{merve} -> ✅ completed")
        merve=merve+1
        time.sleep(1)

    except Exception as e:
            print(f"{i} -> ❌ Hata: {e}")
            isim.append("hata")
            adress.append("hata")
            tel.append("hata")
            site.append("hata")


import csv

with open('markets.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Başlık satırı
    writer.writerow(['Name', 'Adress', 'Tel', 'Site'])
    
    # Verileri yaz
    for i, a, t, s in zip(isim, adress, tel, site):
        writer.writerow([i, a, t, s])








