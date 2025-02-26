# Cтворити скрипт для автоматизації входу у Facebook, або Linkedin й видобування фотографії профілю. 
# Передбачити можливості recaptcha та розписати шляхів її уникнення ( окремо в текстовому повідомленні). 
# Перенаправляти логи у out.log . Надіслати у вигляді репозиторію на гітхаб. 
# Обов’язкова умова: використання Docker контейнера для забезпечення простоти запуску та тестування. 
# Все, що не прописано у ТЗ- на Ваш розсуд

import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
USER_ID = os.getenv("FACEBOOK_USER_ID")

if os.name == 'nt':  
    log_file = 'out.log'
elif os.name == 'posix':  
    log_file = '/app/out.log'

if not os.path.exists(log_file):
    with open(log_file, 'w', encoding='utf-8'):
        pass

logging.basicConfig(filename=log_file, level=logging.INFO, encoding='utf-8')

logging.info("Скрипт запущено!")

def login_facebook():

    logging.info("Початок процесу логування...")
    url = f"https://graph.facebook.com/v13.0/{USER_ID}/picture?type=large&access_token={ACCESS_TOKEN}"

    response = requests.get(url)

    if response.status_code == 200:
        profile_picture_url = response.url
        print(f"Profile picture URL: {profile_picture_url}")
        logging.info(f"Profile picture URL: {profile_picture_url}")
    else:
        print(f"Error: {response.status_code}")
        logging.error(f"Error: {response.status_code}")

if __name__ == "__main__":
    login_facebook()


#  V.2

# import os
# import time
# import logging
# import tempfile
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from dotenv import load_dotenv

# load_dotenv()
# USERNAME = os.getenv("FACEBOOK_USERNAME")
# PASSWORD = os.getenv("FACEBOOK_PASSWORD")

# if os.name == 'nt':
#     log_file = 'AFL/out.log'
# elif os.name == 'posix':
#     log_file = '/app/out.log'

# if not os.path.exists(log_file):
#     with open(log_file, 'w'):
#         pass

# logging.basicConfig(filename=log_file, level=logging.INFO)

# logging.info("Скрипт запущено!")

# def login_facebook(username, password):

#     logging.info("Початок процесу логування...")
#     url = "https://www.facebook.com/"

#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--remote-debugging-port=9222")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-software-rasterizer")
#     chrome_options.add_argument("--incognito")

#     if os.name == 'nt' :  # Для Windows
#         chromedriver_path = 'AFL/chromedriver.exe'
#     elif os.name == 'posix':  
#         chromedriver_path = '/app/chromedriver'
#         chrome_options.add_argument("--headless") 

#     chrome_service = ChromeService(chromedriver_path)  # Для Linux використовується без .exe
#     driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#     driver.get(url)
#     time.sleep(3)
#     try:
#         email_el = driver.find_element(By.ID, 'email')
#         pass_el = driver.find_element(By.ID, 'pass')

#         email_el.send_keys(username)
#         pass_el.send_keys(password)
#         pass_el.send_keys(Keys.RETURN)

#         time.sleep(15)

#         profile_el = driver.find_element(By.XPATH, "//div[@class='x1yztbdb']//a")
#         profile_url = profile_el.get_attribute("href")
#         driver.get(profile_url)

#         time.sleep(3)
        
#         open_menu = driver.find_element(By.XPATH, "//div[@class='x15sbx0n x1xy773u x390vds xb2vh1x x14xzxk9 x18u1y24 xs6kywh x5wy4b0']")
#         open_menu.click()

#         time.sleep(3)
        
#         profile_img_el = driver.find_element(By.XPATH, "//a[@role='menuitem']")
#         profile_img_url = profile_img_el.get_attribute("href")
#         driver.get(profile_img_url)

#         time.sleep(3)

#         img_el = driver.find_element(By.XPATH, "//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6']//img")
#         img_url = img_el.get_attribute("src")
#         logging.info(f"Profile picture URL: {img_url}")

#     except Exception as e:
#         logging.error(f"Error: {str(e)}")
#     finally:
#         driver.quit()


# if __name__ == "__main__":
#     login_facebook(USERNAME, PASSWORD)