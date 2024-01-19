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

# masuk ke halaman content management

content_management = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/aside/ul/li[2]').click()

time. sleep(5)

# ================================================================================================
# Masuk Scenario
scenario_beach = driver.find_element(By.XPATH, "//a[contains(text(),'6 Scenario(s)')]").click()
time.sleep(10)

# view scenario
view_scenario_dresswounds = driver.find_element(By.XPATH, "//div[2]/div[5]/div/a").click()
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(10)
view_scenario_infus_tidakmasukvena = driver.find_element(By.XPATH, "//div[3]/div[5]/div/a").click()
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
view_scenario_perform = driver.find_element(By.XPATH,"//div[4]/div[5]/div/a").click()
time.sleep(5)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
view_scenario_pertolongan_lebih_lanjut = driver.find_element(By.XPATH,"//div[6]/div[5]/div/a").click()
time.sleep(5)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()

# ================================================================================================
# Edit Screnario
edit_scenario_dresswounds = driver.find_element(By.XPATH, "//div[2]/div[5]/div/a[2]").click()
time.sleep(5)
type_description = driver.find_element(By.CSS_SELECTOR, ".min-h-\[80px\]")
type_description.clear()
type_description.send_keys("Testing dress wounds")
time.sleep(10)

type_exam_duration = driver.find_element(By.CSS_SELECTOR, ".space-y-2:nth-child(5) > .flex")
type_exam_duration.clear()
type_exam_duration.send_keys("100")
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
# button_save=driver.find_element(By.XPATH, "//button[2]").click()
# ---------
edit_scenario_infus_tidakmasukvena = driver.find_element(By.XPATH, "//div[3]/div[5]/div/a[2]").click()
time.sleep(5)
type_description = driver.find_element(By.CSS_SELECTOR, ".min-h-\[80px\]")
type_description.clear()
type_description.send_keys("Testing infus")
time.sleep(10)

type_exam_duration = driver.find_element(By.CSS_SELECTOR,".space-y-2:nth-child(5) > .flex")
type_exam_duration.clear()
type_exam_duration.send_keys("100")
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
# button_save=driver.find_element(By.XPATH, "//button[2]").click()
# ---------
edit_scenario_infus_perform = driver.find_element(By.XPATH, "//div[4]/div[5]/div/a[2]").click()
time.sleep(5)
type_description = driver.find_element(By.CSS_SELECTOR, ".min-h-\[80px\]")
type_description.clear()
type_description.send_keys("Testing perform")
time.sleep(10)

type_exam_duration = driver.find_element(By.CSS_SELECTOR, ".space-y-2:nth-child(5) > .flex")
type_exam_duration.clear()
type_exam_duration.send_keys("100")
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
# button_save=driver.find_element(By.XPATH, "//button[2]").click()
# ---------
edit_scenario_pertolongan_lebih_lanjut = driver.find_element(By.XPATH, "//div[6]/div[5]/div/a[2]").click()
time.sleep(5)
type_description = driver.find_element(By.CSS_SELECTOR, ".min-h-\[80px\]")
type_description.clear()
type_description.send_keys("Testing patah tulang")
time.sleep(10)

type_exam_duration = driver.find_element(By.CSS_SELECTOR, ".space-y-2:nth-child(5) > .flex")
type_exam_duration.clear()
type_exam_duration.send_keys("100")
time.sleep(10)
back = driver.find_element(By.XPATH, "//span[contains(.,'Back')]").click()
time.sleep(5)
button_save=driver.find_element(By.XPATH, "//button[2]").click()
# ---------

# ================================================================================================
# Sort By Difficulty

drop_down_difficulty = driver.find_element(By.XPATH,"//div/div[2]/div/div/div[2]/div/div").click()
time.sleep(5)

difficulty_perwira = driver.find_element(By.CSS_SELECTOR,"div[class='table-header mb-4'] li:nth-child(2)").click()
time.sleep(5)
clear_search_difficulty = driver.find_element(By.XPATH,"//div[2]/div/div[2]/div/i").click()
time.sleep(5)
difficulty_bintara = driver.find_element(By.CSS_SELECTOR,".select-search-show-list-item:nth-child(3)").click()
time.sleep(5)
clear_search_difficulty = driver.find_element(By.XPATH,"//div[2]/div/div[2]/div/i").click()
time.sleep(5)

# ================================================================================================
# Sort By Search

search_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search...']")
time.sleep(2)
search_button.send_keys("dre")
time.sleep(5)

# End