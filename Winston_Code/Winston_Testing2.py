"""
This Sheet is created only for the purpose of testing code.
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Winston_Code import Excel_utils_Winston as Excel_utils
from Winston_Code import Winston_Urls as url

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 100)

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)
no_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 3)
made_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 4)
user_id = Excel_utils.readData(url.case_Data, 'Data', 2, 7)

driver.get(f"{url.winston}{case}")
driver.implicitly_wait(15)
# driver.find_element_by_xpath(f"{url.upload_xpath}").send_keys(f"{url.file_path}{vendor}.xlsx")
# # time.sleep(3)

"""
In the below code we are entering into an iframe to write into correspondence.
iframe_corres=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']") - Assiging a variable to xpath of an iframe.
driver.switch_to.frame(iframe_corres) - switching from html to iframe
driver.find_element_by_tag_name("body").send_keys("musa bhai") - Tying information
driver.switch_to.default_content() - switching back to html to proceed with further actions. 
"""

# wait.until(EC.element_to_be_clickable((By.XPATH, "//iframe[@class='cke_wysiwyg_frame cke_reset']")))
# iframe_corres = driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']")
# driver.switch_to.frame(iframe_corres)
# driver.find_element_by_tag_name("body").send_keys("This case is being tested for auto - resolution python script")
# driver.switch_to.default_content()
#
# # Winston Status
# wait.until(EC.element_to_be_clickable((By.ID, "awsui-select-1-textbox")))
# status = driver.find_element_by_id('awsui-select-1-textbox')
# status.click()
#
# ## Select pending status
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')))
# pending = driver.find_element_by_xpath('//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')
# pending.click()
#
# ## Selecting Pending Reason
#
# wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span")))
# pending_reason_dd = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span')
# pending_reason_dd.click()
#
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='awsui-select-option-label'][text()='Pending for quality check']")))
# pending_reason = driver.find_element_by_xpath("//span[@class='awsui-select-option-label'][text()='Pending for quality check']")
# pending_reason.click()
#
# ## Select 'Ok' button after 'Pending for quality check is made
# wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")))
# quality_check = driver.find_element_by_xpath("//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
# quality_check.click()
# # time.sleep(2)
#
# ## Press update button
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')))
# update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
# update_t1.click()
# # time.sleep(2)

"""
PART 2 - Checking...
"""

## Pressing Resolve Button

wait.until(EC.element_to_be_clickable((By.ID, "awsui-select-1-textbox")))
status = driver.find_element_by_id('awsui-select-1-textbox')
status.click()


wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Resolved']")))
resolve = driver.find_element_by_xpath("//span[text()='Resolved']")
resolve.click()

## Adding user ID in the Winston Case

wait.until(EC.element_to_be_clickable((By.XPATH, "//awsui-modal[@class='winston-container']//b[contains(text(),'Resolution description')]//parent::span//parent::label//parent::div//parent::awsui-form-field//iframe[@class='cke_wysiwyg_frame cke_reset']")))
iframe_corres = driver.find_element_by_xpath("//awsui-modal[@class='winston-container']//b[contains(text(),'Resolution description')]//parent::span//parent::label//parent::div//parent::awsui-form-field//iframe[@class='cke_wysiwyg_frame cke_reset']")
driver.switch_to.frame(iframe_corres)
driver.find_element_by_tag_name("body").find_element_by_tag_name("p").clear()
driver.find_element_by_tag_name("body").find_element_by_tag_name("p").send_keys(f"@{user_id}")
driver.switch_to.default_content()
# time.sleep(1)

## Selecting "Description of Work" dropdown



wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-9-textbox"]')))
desc_work = driver.find_element_by_xpath('//*[@id="awsui-select-9-textbox"]')

if desc_work.text != "Proactive task":

    desc_work.click()
    # time.sleep(1)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Proactive task']")))
    desc_reason = driver.find_element_by_xpath("//span[text()='Proactive task']")

    desc_reason.click()
    # time.sleep(1)

else:
    pass


## Mentioning Number of ASINs

wait.until(EC.element_to_be_clickable((By.ID, "awsui-input-8")))
asin_number = driver.find_element_by_id("awsui-input-8")
asin_number.clear()
asin_number.send_keys(no_asins)

## Mentioning Number of Worked ASINs

worked_asin = driver.find_element_by_id("awsui-input-9")
worked_asin.clear()
worked_asin.send_keys(made_asins)

## Pressing 'OK' button for submit button

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='awsui-modal-dialog awsui-modal-expandtofit awsui-modal-size-max']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")))
ok_button = driver.find_element_by_xpath("//div[@class='awsui-modal-dialog awsui-modal-expandtofit awsui-modal-size-max']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
ok_button.click()
# time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')))
update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
update_t1.click()
time.sleep(3)

"""
Part 3 Checking...
"""

## Removig incorrect login ID and adding resolvers login ID

## Removes the existing login ID

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[8]/div/div[3]/div[1]/div/div/div/div/button/awsui-icon/span")))
remove_image = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[8]/div/div[3]/div[1]/div/div/div/div/button/awsui-icon/span")
remove_image.click()
time.sleep(1)

## Add associate login ID

wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/awsui-app-layout[1]/div[1]/main[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[3]/div[1]/div[1]/div[1]/awsui-input[1]/div[1]/input[1]")))
add_login_id = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/awsui-app-layout[1]/div[1]/main[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[3]/div[1]/div[1]/div[1]/awsui-input[1]/div[1]/input[1]")
time.sleep(1)
add_login_id.send_keys(user_id)
# time.sleep(2) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

## Selects the pop up image of login ID

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[1]/div/div/div/ul/li/awsui-select-option/div')))
img_login = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[1]/div/div/div/ul/li/awsui-select-option/div')
img_login.click()

## Changing the assignee reason

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")))
assign_reason = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")
assign_reason.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[8]/div/div/div[1]")))
reason_others = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[2]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[8]/div/div/div[1]")
reason_others.click()
# time.sleep(1) #TODO: Try and see if the code works without any error if the time is reduced to 1 second

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WinstonApp"]/div/div[9]/awsui-modal/div[2]/div/div/div[3]/span/span/awsui-button[2]/button')))
save_button = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[9]/awsui-modal/div[2]/div/div/div[3]/span/span/awsui-button[2]/button')
save_button.click()

# Closing the Winston Case

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Close')]")))
close_button = driver.find_element_by_xpath("//span[contains(text(),'Close')]")
close_button.click()

## Selecting Closure Code for the winston

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")))
closure_selection = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-trigger/div/div/span/span")
closure_selection.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[2]/div/div/div[1]/span[1]")))
success = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div/div/div[9]/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/awsui-form-field/div/div/div/div/span/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[2]/div/div/div[1]/span[1]")
success.click()
# time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WinstonApp"]/div/div[9]/awsui-modal/div[2]/div/div/div[3]/span/span/awsui-button[2]/button/span')))
ok_button = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[9]/awsui-modal/div[2]/div/div/div[3]/span/span/awsui-button[2]/button/span')
ok_button.click()
time.sleep(3)