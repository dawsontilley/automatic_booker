from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time


def three_days_out():

    return (datetime.datetime.today().day + datetime.timedelta(days=3).days)


def book_ideal_time():

    ans = "1"
    return ans

#url = "https://northwestbadmintonacademy.sites.zenplanner.com/login.cfm"
#url = "https://auth.buildinglink.com/Account/Login"
#url = https://thepinnaclecentre.buildinglink.com/v2/tenant/amenities/NewReservation.aspx?from=1&amenityId=16844&starts=9/22/2023%205:00:00%20PM&ends=9/22/2023%206:00:00%20PM
url = "Http://www.thepinnaclecentre.com"

amenity_id = 16844
start = "9/22/2023%205:00:00%20PM&"
end = "9/22/2023%206:00:00%20PM"
#browser = webdriver.Chrome(executable_path='./chromedriver.exe')
#browser.get(url)

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
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

squash_pick = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_AmenitiesDataList_ctl18_SelectAmenityLink']")
squash_pick.click()





""""
grid_res = driver.find_element("xpath","//*[@id='ctl00_ContentPlaceHolder1_AvailabilityGridViewButton']")
grid_res.click()

fake_input_for_squash = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_AmenitiesDropdownTree']/span/span[1]")
fake_input_for_squash.click()

squash_selection = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_AmenitiesDropdownTree_EmbeddedTree']/ul/li[16]/div/span[2]")
squash_selection.click()

next_day = driver.find_element("xpath","//*[@id='ctl00_ContentPlaceHolder1_ButtonNextDay']")
next_day.click()
next_day.click()


refresh = driver.find_element("xpath","//*[@id='ctl00_ContentPlaceHolder1_RefreshCalendarButton']")
refresh.click()
"""

date_to_book = three_days_out()
print(date_to_book)
xpath_booking_date = f"//a[text()={date_to_book}]"


#xpath_booking_date = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_StartDatePicker_Top']/tbody/tr[5]/td[2]/a")
booking_date = driver.find_element("xpath",xpath_booking_date)
booking_date.click()

#time_box = driver.find_element("xpath" , "//*[@id='ctl00_ContentPlaceHolder1_StartTimePicker_dateInput']")
#time_box.click()

#six_pm_time = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl']/tbody/tr[4]/td[2]/a")
#seven_pm_time = driver.find_element("xpath","//*[@id='ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl;]/tbody/tr[4]/td[3]/a")
#seven_pm_time.click()
#//*[@id="ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl"]/tbody/tr[3]/td[2]/a
#xpath_time = "//tbody/tr/td/a/[text()=7:00 PM]"

#start_time = driver.find_element("xpath", "//[@id'ctl00_ContentPlaceHolder1_StartTimePicker_dateInput_wrapper']")
#start_time.click()


#maybe_xpath = "//tbody/tr/td/a[text()='7:00 PM']"
#xpath = "//a[text() ='7:00 PM']"
#time_to_book = driver.find_element("xpath" , "(//a[contains(text(), '7:00 pm')])[1])")
#time_to_book = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_StartTimePicker_dateInput_wrapper']")
#time_to_book.click()

time.sleep(2)

time_to_book = driver.find_element("xpath", "//*[@id='ctl00_ContentPlaceHolder1_DateSelectionPanel']/ul/li[2]/div/div[1]/div[4]")
time_to_book.click()
#"//input[@id='ctl00_ContentPlaceHolder1_StartTimePicker_wrapper']"

#time.sleep(2)

#time_block = driver.find_element("xpath", //*[@id="ctl00_ContentPlaceHolder1_StartTimePicker_dateInput"])
#//*[@id='ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl']/tr/td

book_time = driver.find_element("xpath", "(//tbody/tr/td/a[text() = '8:00 PM'])[1]")
book_time.click()
#//*[@id="ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl"]/tbody/tr[4]/td[3]/a

time.sleep(2)
save_reso = driver.find_element("xpath" , "//*[@id='ctl00_ContentPlaceHolder1_FooterSaveButton']")
save_reso.click()
time.sleep(10)
