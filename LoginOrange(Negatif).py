from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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

username_input.send_keys("tester")
password_input.send_keys("tester123")

# Klik tombol login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# validasi invalid login

invalid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='alert']"))
)
invalid = driver.find_element(By.CSS_SELECTOR, "div[role='alert']")

action_chains = ActionChains(driver)
action_chains.double_click(invalid).perform()

# Tunggu beberapa detik untuk melihat hasilnya
time.sleep(5)