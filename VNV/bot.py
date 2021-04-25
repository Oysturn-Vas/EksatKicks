from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import time
import os
from datetime import datetime
import subprocess
import random

# ! Gets the current working directry
current_path=str(os.getcwd())
print(current_path)

PATH = current_path + "\\chromedriver.exe"


# #! List to store the tabs and driver data
accounts=[]
driver=[]
links=[]

# #! Input 
number_of_links= 1
#int(input("\nEnter the number of links:\n"))
number_of_accounts=1
#int(input("\n\nEnter the Number of Accounts:\n"))
links.append(str("https://www.vegnonveg.com/products/air-jordan-11-retro-low-whitelegend-blue-white-black"))

size = input("Enter the Size:\n")


# hour=input("\n\nHour:")
# minutes=input("\nMinutes:")
# second=input("\nSeconds:")
# milliseconds=input("\nMilliseconds:")
# entry_time = int(f"{hour}{minutes}{second}{milliseconds}")

# ! Links input
# for i in range(0,number_of_links):
#     links.append(input(f"\n\nEnter Link {i+1}:\n"))

# ! Loop to open multiple chrome instances V2
for i in range(0,number_of_accounts):
    accounts.append(str(9014+i))
    subprocess.Popen(f'chrome.exe --remote-debugging-port={accounts[i]} --user-data-dir="{current_path}\\Chrome_Files\\Chrome_Test_Profile_{i+1}"', shell=True)
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress",f"127.0.0.1:{accounts[i]}")
    driver.append(webdriver.Chrome(PATH,chrome_options=chrome_options))
    driver[i].get(links[0])

# #! Initializing the time from the PC
# now = datetime.now()
# submit_time = int((int(now.strftime("%H%M%S%f"))/1000))
time.sleep(5)
for i in range(0,number_of_accounts):
    driver[i].find_element_by_class_name("select").click()
    time.sleep(3)
    html_list = driver[i].find_element_by_xpath(f"//li[contains(text(),'{size} UK')]")
    html_list.click()
    print("Done")
    
# driver.findElement(By.id("ctl00_mainContent_ddl_originStation1_CTXT")).click();
# driver.findElement(By.xpath("//a[@value='MAA']")).click();
# driver.findElement(By.xpath("(//a[@value='DEL'])[2]")).click();
 