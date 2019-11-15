"""
This Sheet is created only for the purpose of testing code.
"""
import Winston_Code.Excel_utils_Winston as Excel_utils
import Winston_Code.Winston_Subroutine as sub
import Winston_Code.Winston_Urls as url
from Winston_Code.Winston_Driver import driver
from Winston_Code.Winston_Driver import wait
from Winston_Code.Winston_Subroutine import EC
from Winston_Code.Winston_Subroutine import By

vendor = Excel_utils.readData(url.case_Data, 'Data', 2, 1)
case = Excel_utils.readData(url.case_Data, 'Data', 2, 2)
no_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 3)
made_asins = Excel_utils.readData(url.case_Data, 'Data', 2, 4)
user_id = Excel_utils.readData(url.case_Data, 'Data', 2, 7)
correspondence = Excel_utils.readData(url.case_Data, 'Data', 9, 7)

driver.get(f"{url.winston}{case}")
driver.implicitly_wait(15)

## Winston Status

wait.until(EC.element_to_be_clickable((By.ID, "awsui-select-1-textbox")))
status = driver.find_element_by_id('awsui-select-1-textbox')
print(status.text)

if status.text == 'Assigned':
    sub.pending_status(driver, correspondence)
    sub.resolve_status(driver, user_id, no_asins, made_asins)
elif status.text == 'WIP':
    sub.resolve_status(driver, user_id, no_asins, made_asins)
elif status.text == 'Pending':
    sub.resolve_status(driver, user_id, no_asins, made_asins)
else:
    pass

Excel_utils.writeData(url.case_Data, 'Result', 2, 1, vendor)
Excel_utils.writeData(url.case_Data, 'Result', 2, 2, case)
Excel_utils.writeData(url.case_Data, 'Result', 2, 3, "Resolved")
print(f"Vendor code {vendor} with Winston id: {case}  has been resolved")
