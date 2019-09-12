import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Winston_Code import Excel_utils_Winston as Excel_utils
from Winston_Code import Winston_Urls as url

driver = webdriver.Chrome(ChromeDriverManager().install())

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)

driver.get(f"{url.winston}{case}")
time.sleep(5)
# driver.find_element_by_xpath(f"{url.upload_xpath}").send_keys(f"{url.file_path}{vendor}.xlsx")
# time.sleep(3)

"""
In the below code we are entering into an iframe to write into correspondence.

iframe_corres=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']") - Assiging a variable to xpath of an iframe.
driver.switch_to.frame(iframe_corres) - switching from html to iframe
driver.find_element_by_tag_name("body").send_keys("musa bhai") - Tying information
driver.switch_to.default_content() - switching back to html to proceed with further actions. 

"""

iframe_corres=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']")
driver.switch_to.frame(iframe_corres)
driver.find_element_by_tag_name("body").send_keys("musa bhai")
driver.switch_to.default_content()