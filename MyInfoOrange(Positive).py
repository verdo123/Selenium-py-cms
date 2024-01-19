from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
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

# Verifikasi menu My Info
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(6)"))
)
My_info = driver.find_element(By.CSS_SELECTOR, "li:nth-child(6)").click()

# Edit Personal Details
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']"))
)
time.sleep(5)

Full_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
action_chains = ActionChains(driver)
action_chains.double_click(Full_name).perform()
Full_name.send_keys("Verdo")

time.sleep(5)

Middle_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Middle Name']")
action_chains = ActionChains(driver)
action_chains.double_click(Middle_name).perform()
Middle_name.send_keys("Daviarta")

time.sleep(5)

Employee_id = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
action_chains.double_click(Employee_id).perform()
Employee_id.send_keys("FIT161")

time.sleep(5)

Nick_name = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
action_chains.double_click(Nick_name).perform()
Nick_name.send_keys("SQA")

time.sleep(5)
save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Tunggu beberapa detik untuk melihat hasilnya
time.sleep(5)

