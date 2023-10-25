from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
import datetime
import time
from os import environ



def three_days_out():

    return (datetime.datetime.today().day + datetime.timedelta(days=3).days)


def book_ideal_time():

    ans = "1"
    return ans

url = "Http://www.thepinnaclecentre.com"

amenity_id = 16844
start = "9/22/2023%205:00:00%20PM&"
end = "9/22/2023%206:00:00%20PM"
#browser = webdriver.Chrome(executable_path='./chromedriver.exe')
#browser.get(url)
print(environ.get("CHROMEWEBDRIVER",'./chromedriver.exe'))
#options = Options
#options.add_argument('--no-sandbox')
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless=new")
service = Service(executable_path= environ.get("CHROMEWEBDRIVER",'./chromedriver.exe'))

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

driver.get(url)

user_block= driver.find_element('id','Username')
pw = driver.find_element('id','Password')

user_block.send_keys("dtilley3")
pw.send_keys("y8ed8")

submit_button = driver.find_element("xpath", "//*[@id='LoginButton']")
submit = driver.find_element('id', 'LoginButton')
submit.click()

amenity_res = driver.find_element("xpath","//*[@id='leftMenu']/div[4]/ul/li[2]/ul/li[2]/span")
amenity_res.click()

book_res =  driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_NewReservatrionButton']")
book_res.click()

#squash_pick = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_AmenitiesDataList_ctl18_SelectAmenityLink']")
squash_pick = driver.find_element("xpath", "//a[text() = 'Squash Court']")
squash_pick.click()


date_to_book = three_days_out()
print(date_to_book)
xpath_booking_date = f"//a[text()={date_to_book}]"

booking_date = driver.find_element("xpath",xpath_booking_date)
booking_date.click()

time.sleep(2)

time_to_book = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_DateSelectionPanel']/ul/li[2]/div/div[1]/div[4]")
time_to_book.click()

book_time = driver.find_element("xpath", "(//tbody/tr/td/a[text() = '8:00 PM'])[1]")
book_time.click()

time.sleep(2)
save_reso = driver.find_element("xpath" , "//*[@id='ctl00_ContentPlaceHolder1_FooterSaveButton']")
save_reso.click()
time.sleep(10)
