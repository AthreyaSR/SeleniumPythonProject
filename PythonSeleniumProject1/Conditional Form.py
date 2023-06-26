from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from selenium.webdriver.common.by import By


driver.get("https://practice.microdegree.work")

driver.find_element(By.LINK_TEXT, "Manual Testing").click()
firstName = driver.find_element(By.NAME,"fname")
lastName = driver.find_element(By.NAME,"lname")
Email_Address = driver.find_element(By.NAME,"email")
GenderM = driver.find_element(By.XPATH,"/html/body/div[2]/form/table/tbody/tr/td[1]/input")
GenderF = driver.find_element(By.XPATH,"/html/body/div[2]/form/table/tbody/tr/td[2]/input")
NameList = ["Ganesha","Mahesha","Nagesha","","Lakshmi","Seetha","Latha"]

def empty(a):
    print(a)

def form(FirstName, value,List1):
    firstName.send_keys(FirstName)
    if FirstName == "":
        empty("no input")
    elif FirstName == value:
        print(FirstName)
        lastName.send_keys("Bappa moriya")
        LastName = lastName.get_attribute('value')
        print(LastName)
        if LastName == "Bappa moriya":
            Email_Address.send_keys(FirstName + "@gmail.com")
            EmailAddress = Email_Address.get_attribute('value')
            print(EmailAddress)
        if FirstName in List1[0:3]:
            GenderM.click()
            print("male")
        elif FirstName in List1[4:7]:
            GenderF.click()
            print("female")

    else: print(FirstName)
for i in range(7):
    form(NameList[i],NameList[i],NameList)
    # to clear previous entries
    firstName.clear()
    lastName.clear()
    Email_Address.clear()

# to get the value in input field
    # lastName.send_keys("hi")
    # LastName = lastName.get_attribute('value')
    # print(LastName)
time.sleep(3)