from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# Buka URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)

driver.maximize_window()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))
)

# Isi formulir login

username_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")

username_input.send_keys("Admin")
password_input.send_keys("admin123")

# Klik tombol login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# mencari menu Dasbor
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
)
time.sleep(10)
search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")

# masukan kata kunci pencarian
search_input.send_keys("Dasbor")

# Tunggu beberapa detik untuk melihat hasilnya

time.sleep(5)