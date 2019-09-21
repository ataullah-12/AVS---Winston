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
driver.implicitly_wait(15)

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)

driver.get(f"{url.winston}{case}")
driver.find_element_by_xpath(f"{url.upload_xpath}").send_keys(f"{url.file_path}{vendor}.xlsx")
# time.sleep(3)

"""
In the below code we are entering into an iframe to write into correspondence.

iframe_corres=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']") - Assiging a variable to xpath of an iframe.
driver.switch_to.frame(iframe_corres) - switching from html to iframe
driver.find_element_by_tag_name("body").send_keys("musa bhai") - Tying information
driver.switch_to.default_content() - switching back to html to proceed with further actions. 

"""

iframe_corres = driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']")
driver.switch_to.frame(iframe_corres)
driver.find_element_by_tag_name("body").send_keys("This case is being tested for auto - resolution python script")
driver.switch_to.default_content()

# Winston Status
status = driver.find_element_by_id('awsui-select-1-textbox')
status.click()

# Select pending status
pending = driver.find_element_by_xpath('//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')
pending.click()
time.sleep(2)

# Select 'Ok' button after 'Pending for quality check is made
quality_check = driver.find_element_by_xpath("//div[@class='awsui-modal-container awsui-modal-expandtofit']//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']")
quality_check.click()
time.sleep(2)

# Press update button
update_t1 = driver.find_element_by_xpath('//*[@id="WinstonApp"]/div/div[8]/div/div[3]/div[2]/awsui-button/button/span')
update_t1.click()
time.sleep(2)

status.click()
resolve = driver.find_element_by_xpath('//*[@id="awsui-select-1-dropdown-option-2"]/div/div/div[1]/span[1]')
resolve.click()

driver.switch_to.frame(iframe_corres)
# driver.find_element_by_tag_name("body").click()
driver.find_element_by_tag_name("body").send_keys("login @mmohdat")
driver.switch_to.default_content()
time.sleep(1)