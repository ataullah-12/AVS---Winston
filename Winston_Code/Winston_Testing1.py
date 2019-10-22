"""
This Sheet is created only for the purpose of testing code.
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Winston_Code import Excel_utils_Winston as Excel_utils
from Winston_Code import Winston_Urls as url

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# import selenium.webdriver.support.expected_conditions as ec
# import selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)
no_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 3)
made_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 4)
user_id = Excel_utils.readData(url.case_Data, 'Data', 2, 7)


driver.get(f"{url.winston}{case}")
driver.implicitly_wait(5)

# driver.find_element_by_xpath(f"{url.upload_xpath}").send_keys(f"{url.file_path}{vendor}.xlsx")
# time.sleep(3)

"""
In the below code we are entering into an iframe to write into correspondence.

iframe_corres=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']") - Assiging a variable to xpath of an iframe.
driver.switch_to.frame(iframe_corres) - switching from html to iframe
driver.find_element_by_tag_name("body").send_keys("musa bhai") - Tying information
driver.switch_to.default_content() - switching back to html to proceed with further actions. 

"""

## Corresponding on the Winston Case

iframe_corres = driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']")
driver.switch_to.frame(iframe_corres)
driver.find_element_by_tag_name("body").send_keys("This case is being tested for auto - resolution python script")
driver.switch_to.default_content()

## Winston Status

status = driver.find_element_by_id('awsui-select-1-textbox')
status.click()

## Select pending status

pending = driver.find_element_by_xpath('//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')
pending.click()
time.sleep(2)

## Select 'Ok' button after 'Pending for quality check is made

quality_check = driver.find_element_by_xpath("//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
quality_check.click()
time.sleep(2)

## Press update button

update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
update_t1.click()
time.sleep(2)

## Clicking the Status Button

status.click()
resolve = driver.find_element_by_xpath('//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')
resolve.click()

## Adding user ID in the Winston Case

iframe_corres = driver.find_element_by_xpath("//awsui-modal[@class='winston-container']//b[contains(text(),'Resolution description')]//parent::span//parent::label//parent::div//parent::awsui-form-field//iframe[@class='cke_wysiwyg_frame cke_reset']")
driver.switch_to.frame(iframe_corres)
driver.find_element_by_tag_name("body").find_element_by_tag_name("p").send_keys("@mmohdat")
driver.switch_to.default_content()
time.sleep(1)

## Mentioning Number of ASINs

asin_number = driver.find_element_by_id("awsui-input-8")
asin_number.clear()
asin_number.send_keys(no_asins)

## Mentioning Number of Worked ASINs

worked_asin = driver.find_element_by_id("awsui-input-9")
worked_asin.clear()
worked_asin.send_keys(made_asins)

# Pressing 'OK' button for submit button

ok_button = driver.find_element_by_xpath("//div[@class='awsui-modal-dialog awsui-modal-expandtofit awsui-modal-size-max']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
ok_button.click()

## Removig incorrect login ID and adding resolvers login ID

## Removes the existing login ID
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[8]/div/div[3]/div[1]/div/div/div/div/button/awsui-icon/span").click()
time.sleep(1)

## Add associate login ID
add_login_id = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/awsui-app-layout[1]/div[1]/main[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[3]/div[1]/div[1]/div[1]/awsui-input[1]/div[1]/input[1]")
time.sleep(1)
add_login_id.send_keys(user_id)
time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

## Selects the pop up image of login ID
img_login = driver.find_element_by_xpath("//div[@class='awsui-select-option-description']")
img_login.click()
## Press update button

update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
update_t1.click()
time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

## Closing the Winston Case

close_button = driver.find_element_by_xpath("//span[contains(text(),'Close')]")
close_button.click()
update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
update_t1.click()
time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

## Changing the assignee reason

assign_reason = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")
assign_reason.click()
reason_others = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[8]/div/div/div[1]")
reason_others.click()
time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

## Selecting Closure Code for the winston

# closure_selection = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")
closure_selection = driver.find_element_by_id("awsui-select-10-textbox")
closure_selection.click()
success = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[2]/div/div/div[1]/span[1]")
success.click()
time.sleep(1)

# Select 'Ok' button after 'Pending for quality check is made
quality_check = driver.find_element_by_xpath("//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
quality_check.click()
time.sleep(2)

## Select 'Ok' button after 'Pending for quality check is made

quality_check = driver.find_element_by_xpath("//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
quality_check.click()
time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

//span[text()='Proactive task']

//*[@id="awsui-select-10-textbox"]//span[text()="Select the description of work"]