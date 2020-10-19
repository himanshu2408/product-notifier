from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from win10toast import ToastNotifier
import time
from playsound import playsound
toaster = ToastNotifier()

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    while True:
        driver.get("https://www.amazon.in/dp/B0864JT3GT/?coliid=I1VVYOSBPIZ78Y&colid=2LNETFR2D1RYK&psc=0&ref_=lv_ov_lig_dp_it")
        centerCol = driver.find_element(By.ID, "centerCol").text
        print(centerCol[0:267])
        try:
            variation = driver.find_element(By.ID, "variation_size_name")
            if(variation):
                print(variation.text)
                if('256' in variation.text):
                    toaster.show_toast(productTitle,
                            variation.text,
                            icon_path=None,
                            duration=100)
                    playsound('fire-truck-air-horn.mp3')
        except:
            print("PRODUCT NOT AVAILABLE")
        print("**************************************\n\n")
        time.sleep(60)