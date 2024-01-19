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

# masuk ke halaman User management

content_management = driver.find_element(By.XPATH, '//li[3]/a/span').click()

time. sleep(5)

# ================================================================================================
# Pagination

pagination = driver.find_element(By.XPATH,"//li[normalize-space()='2']").click()
time.sleep(5)
pagination = driver.find_element(By.XPATH,"//li[normalize-space()='3']").click()


# ================================================================================================
# Add User

# add_user = driver.find_element(By.CSS_SELECTOR, "button[class='inline-flex items-center justify-center font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 px-4 py-2 bg-primary-1 text-based-1 hover:bg-primary-2 hover:text-white !px-4 h-[38px] sm:text-base text-sm rounded-[5px]']").click()
# time.sleep(5)
# type_username = driver.find_element(By.XPATH,"//input[@id='username']")
# type_username.send_keys("testingQA")
# time.sleep(1)
# type_firstname = driver.find_element(By.XPATH,"//input[@id='user_detail.firstName']")
# type_firstname.send_keys("SQA")
# time.sleep(1)
# type_lastname = driver.find_element(By.XPATH,"//input[@id='user_detail.lastName']")
# type_lastname.send_keys("tester")
# time.sleep(1)
# year_registered = driver.find_element(By.XPATH,"//input[@id='user_detail.yearRegistered']").click()
# time.sleep(2)
# year_registered = driver.find_element(By.XPATH,"//div[normalize-space()='2023']").click()
# time.sleep(5)
# select_rank = driver.find_element(By.XPATH,"//div[@id='user_detail.rank']//div[@class='select-search-selected']").click()
# time.sleep(2)
# select_rank = driver.find_element(By.XPATH,"//li[normalize-space()='Pangkat Bintara TNI AL']").click()
# time.sleep(5)
# select_role = driver.find_element(By. XPATH,"//div[@id='role']//div[@class='select-search-selected']").click()
# time.sleep(2)
# select_role = driver.find_element(By.XPATH,"//li[normalize-space()='Instructor']").click()
# time.sleep(5)
# type_password = driver.find_element(By.XPATH, "//input[@id='password']")
# type_password.send_keys("password")
# time.sleep(2)
# confirm_password = driver.find_element(By.XPATH,"//input[@id='passwordConfirmation']")
# confirm_password.send_keys("password")
# time.sleep(2)
# # button_save = driver.find_element(By.XPATH,"//button[@type='submit']").click()
# # time.sleep(10)

# ================================================================================================
# Sort By Role

# drop_down_role = driver.find_element(By.XPATH,"//body/div/div/main/main/div/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
# time.sleep(2)
# drop_down_role = driver.find_element(By.XPATH,"//li[normalize-space()='Instructor']").click()
# time.sleep(5)
# clear_sort_role = driver.find_element(By.XPATH,"//div[2]/div/div[2]/div/i").click()
# time.sleep(2)
# drop_down_role = driver.find_element(By.XPATH,"//li[normalize-space()='Trainee']").click()
# time.sleep(5)
# clear_sort_role = driver.find_element(By.XPATH,"//div[2]/div/div[2]/div/i").click()
# time.sleep(2)

# ================================================================================================
# Sort By Status

# drop_down_status = driver.find_element(By.XPATH,"//p[normalize-space()='User Status']").click()
# time.sleep(5)
# drop_down_status = driver.find_element(By.XPATH,"//li[normalize-space()='Inactive']").click()
# time.sleep(5)
# clear_sort_role = driver.find_element(By.XPATH,"//i[@class='pusdikes-icon-close icon']").click()
# time.sleep(2)
# drop_down_status = driver.find_element(By.XPATH,"//li[normalize-space()='Active']").click()
# time.sleep(5)
# clear_sort_role = driver.find_element(By.XPATH,"//i[@class='pusdikes-icon-close icon']").click()
# time.sleep(2)

# ================================================================================================
# Feature Search

search_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search...']")
time.sleep(2)
search_button.send_keys("test")
time.sleep(5)

# ================================================================================================
# View user

# user_view = driver.find_element(By. XPATH, "//a[@class='styles_btn-view__A7F6c']").click()
# time.sleep(5)
# back = driver.find_element(By.XPATH, "//button[@class='inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 styles_btn-back__yk9z1']").click()
# time.sleep(5)

# search_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search...']")
# time.sleep(2)
# search_button.send_keys("test")
# time.sleep(5)

# ================================================================================================
# Edit user

user_edit = driver.find_element(By. XPATH, "//a[@class='styles_btn-edit__LCvqP']").click()
time.sleep(5)
type_username = driver.find_element(By.XPATH,"//input[@id='username']")
type_username.send_keys("1")
time.sleep(1)
type_firstname = driver.find_element(By.XPATH,"//input[@id='user_detail.firstName']")
type_firstname.send_keys("_edit")
time.sleep(1)
type_lastname = driver.find_element(By.XPATH,"//input[@id='user_detail.lastName']")
type_lastname.send_keys("_edit")
time.sleep(1)
year_registered = driver.find_element(By.XPATH,"//input[@id='user_detail.yearRegistered']").click()
time.sleep(1)
year_registered = driver.find_element(By.XPATH,"//div[normalize-space()='2024']").click()
time.sleep(2)
select_rank = driver.find_element(By.XPATH,"//div[@id='user_detail.rank']//div[@class='select-search-selected']").click()
time.sleep(2)
select_rank = driver.find_element(By.XPATH,"//li[normalize-space()='Pangkat Tamtama TNI AL']").click()
time.sleep(2)
select_role = driver.find_element(By. XPATH,"//div[@id='role']//div[@class='select-search-selected']").click()
time.sleep(2)
select_role = driver.find_element(By.XPATH,"//li[normalize-space()='Trainee']").click()
time.sleep(2)
type_password = driver.find_element(By.XPATH, "//input[@id='password']")
type_password.send_keys("password123")
time.sleep(2)
confirm_password = driver.find_element(By.XPATH,"//input[@id='passwordConfirmation']")
confirm_password.send_keys("password123")
time.sleep(2)
user_status = driver.find_element(By.XPATH,"//span[@class='px-4 py-2 text-white bg-based-3 rounded-full peer-checked:bg-transparent peer-checked:text-white']").click()
time.sleep(10)
# button_save = driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(10)

back = driver.find_element(By.XPATH, "//button[@class='inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 styles_btn-back__yk9z1']").click()
time.sleep(5)

search_button = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search...']")
time.sleep(2)
search_button.send_keys("test")
time.sleep(5)

# ================================================================================================
# Delete user

delete_user = driver.find_element(By.XPATH,"//button[contains(.,'Delete')]").click()
time.sleep(2)
button_delete = driver.find_element(By.CSS_SELECTOR,".styles_dialog-delete_btn-delete__LJ_i_").click()
time.sleep(10)

# End