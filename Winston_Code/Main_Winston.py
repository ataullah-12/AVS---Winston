import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Winston_Code import Excel_utils_Winston as Excel_utils
from Winston_Code import Winston_Urls as url

driver = webdriver.Chrome(ChromeDriverManager().install())

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)

driver.get(f"{url.winston}{case}")
time.sleep(2)
driver.find_element_by_xpath(f"{url.upload_xpath}").send_keys(f"{url.file_path}{vendor}.xlsx")
time.sleep(1)