from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Inisialisasi WebDriver
Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# Buka URL
url = "http://192.168.101.186:14007/login"
driver.get(url)

WebDriverWait(driver, 10)

# Isi formulir login

username_input = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/div[1]/input')
password_input = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[2]/div[2]/div/input')

username_input.send_keys("admin1")
password_input.send_keys("Password123")

# Klik tombol login
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/button")
login_button.click()

# Tunggu beberapa detik untuk melihat hasilnya
time.sleep(5)

# Tutup browser
driver.quit()
