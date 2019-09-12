"""Winston URL"""
winston = "https://avs-eu.aka.amazon.com/EU/task/"

"""Path to excel sheet from where winston cases & vendor code will be extracted."""
case_Data = "C:\\Users\\shariemo\\PycharmProjects\\Ataulla\Winston Resolver\\Case_data.xlsx"

"""Path to folder where all the vendor's data will be kept in excel sheet; the files from here will be uploaded on the Winston case."""
file_path = "C:\\Users\\shariemo\\PycharmProjects\\Ataulla\\Winston Resolver\\Vendor Sheets\\"

"""This is the xpath to where selenium will upload the files too.

NOTE: For selenium to upload the file, xpath of the upload dialog box should contain :keyword 'input'.  
"""
upload_xpath = "//div[@class='col-m-6 col-xxs-12']//div//div//div[@class='awsui-row']//div[@class='col-m-12 col-xxs-12']//awsui-form-field//div[@class='awsui-form-field awsui-form-field-stretch']//div[@class='awsui-grid awsui-form-field-controls']//div[@class='awsui-row']//div[@class='awsui-form-field-control col-xxxs-12 col-xs-9']//span//div//input"