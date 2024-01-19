from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# Buka URL
url = "http://192.168.101.186:14007"
driver.get(url)

driver.maximize_window()

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

# masuk ke halaman Report By Scenario
Report_management = driver.find_element(By.CSS_SELECTOR,"/html/body/div[1]/div[2]/aside/ul/li[4]").click()
time.sleep(2)
Report_scenario = driver.find_element(By.XPATH,".sidebar-item:nth-child(1) .flex").click()
time.sleep(5)

# ================================================================================================
# Sort by Location

location_sort = driver.find_element(By.XPATH,"//div[@class='select-search-selected']").click()
time.sleep(2)
location_sort = driver.find_element(By.XPATH,"//li[normalize-space()='Beach']").click()
time.sleep(2)
