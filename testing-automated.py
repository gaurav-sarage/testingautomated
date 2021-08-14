import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

op = Options()
op.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")
print("Let's Start our Testing")

print("TestCase 1:---")
try:
    title_name=driver.title
    print("Title verification is successfull and our tile is: ",title_name)
except:
    print("Title verification failed")

print("\nTestCase 2:---")

try:
    driver.find_element(By.CLASS_NAME,"navbar")
    count_nav=driver.find_elements(By.XPATH,'//li[@class="dropdown menu__item"]')
    if(len(count_nav)==5):
        print("Navbar Verification Successful!\n")
    else:
        print(f"Navbar is Present but there are only {len(count_nav)} are present")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

print("\nTestCase 3:---")

try:
    driver.find_element(By.PARTIAL_LINK_TEXT,"Contact Us").click()
    time.sleep(3)
    add= driver.find_element(By.XPATH,'//div[@class="contact"]/div/div/div[2]/div[2]/p').text
    contact=driver.find_element(By.XPATH,'//div[@class="contact"]/div/div/div[3]/div[2]/p[2]').text
    if("21 HENG MUI KENG TERRACE, SINGAPORE, 119613" in add and "+65-8402-8590, info@thesparksfoundation.sg" in contact):
        print("Contact and Address Informations are correct")
    else:
        print("Contact and Address Informations are incorrect")

    print("Contact Verification Successfull")
except:
    print("Contact Verification Failed")

print("\nTstcase 4:---")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()
    print("Home Element working Fine!")
except NoSuchElementException:
    print("Home Element verification Faied! Does not exist")

print("\nTstcase 5:---")
try:
    driver.find_element(By.LINK_TEXT,'About Us').click()
    driver.find_element(By.LINK_TEXT,'News').click()
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")

print("\nTstcase 6:---")
try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    driver.find_element(By.LINK_TEXT,'Policies').click()
    print('Policies page visited Successfully!\n')
except NoSuchElementException:
    print("Policies page visit Failed! Does not exist.\n")

print("\nTstcase 7:---")
try:
    driver.find_element(By.LINK_TEXT,'Programs').click()
    driver.find_element(By.LINK_TEXT,'Workshops').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,'LEARN MORE').click()
    print('Workshop page visited Successfully!\n')
except NoSuchElementException:
    print("Workshop page visit Failed! Does not exist.\n")

print("\nTstcase 8:---")
try:
    driver.find_element(By.LINK_TEXT,'LINKS').click()
    driver.find_element(By.LINK_TEXT,'Software & App').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,'Visit LINKS @TSF').click()

    print('Links page visited Successfully!\n')
except NoSuchElementException:
    print("Links page visit Failed! Does not exist.\n")

print("\nTestcase 9:---")
try:
    driver.find_element(By.XPATH,'//div[@id="home"]/div/div[1]/h1/a/img')
    print("Logo Found!")
except:
    print("No Logo Found!")

print("\nTestcase 10:---")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(2)
    driver.find_element(By.NAME,'Name').send_keys('Aman')
    driver.find_element(By.NAME,'Email').send_keys('aman123@gmail.com')
    select =Select(driver.find_element(By.CLASS_NAME,'form-control'))
    select.select_by_visible_text('Student')
    driver.find_element(By.CLASS_NAME,'button-w3layouts').click()
    print("Form Verification Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")

driver.find_element(By.XPATH,'//div[@id="home"]/div/div[1]/h1/a/img').click()
time.sleep(2)
print("\n TestCase 11:---")
try:
    driver.find_element(By.XPATH,'//iframe[@id="youtube-video"]')
    print("\nVideo Found ")
except:
    print("No Video found")

print("\n Testcase 12:---")
try:
    driver.find_element(By.XPATH,'//div[@class="footer w3layouts"]')
    print("\nFooter Found ")
except:
    print("No Footer found")

print("\n Testcase 13:---")
try:
    driver.find_element(By.XPATH,'//div[@class="owl-controls clickable"]')
    print("\nSlider Found ")
except:
    print("No Slider found")