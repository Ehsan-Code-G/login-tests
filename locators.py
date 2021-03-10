from selenium.webdriver.common.by import By

class CommonLocators():

    User_Name_Box = (By.ID,"identifierId")
    Next_Button = (By.XPATH,"//*[@id='identifierNext']/div/button")
    Password_Box = (By.NAME,"password")
    Submit_Button = (By.XPATH,"//*[@id='passwordNext']/div/button")
    Wrong_Msg_Tag = (By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span")
    Page_Title = (By.XPATH,"/html/head/title")
    