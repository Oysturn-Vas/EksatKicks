from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess
import os

# ! Gets the current working directry
current_path=str(os.getcwd())

PATH = current_path + "\\chromedriver.exe"

# #! List to store the tabs and driver data
tabs=[]
driver=[]

# #! Input 
number_of_tabs=int(input("\n\nEnter the Number of Accounts:\n"))

# ! Loop to open multiple chrome instances V2
for i in range(0,number_of_tabs):
    tabs.append(str(9014+i))
    subprocess.Popen(f'chrome.exe --remote-debugging-port={tabs[i]} --user-data-dir="{current_path}\\Chrome_Files\\Chrome_Test_Profile_{i+1}"', shell=True)
    time.sleep(5)
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress",f"127.0.0.1:{tabs[i]}")
    driver.append(webdriver.Chrome(PATH,chrome_options=chrome_options))
    time.sleep(5)
    driver[i].get("chrome://settings/clearBrowserData")
    time.sleep(5)