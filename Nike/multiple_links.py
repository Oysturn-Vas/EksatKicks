from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os
from datetime import datetime
import subprocess
import random

# ! Gets the current working directry
current_path=str(os.getcwd())

PATH = current_path + "\\chromedriver.exe"

# #! List to store the tabs and driver data
tabs=[]
driver=[]
links=[]

# #! Input 
number_of_links=int(input("\nEnter the number of links:\n"))
number_of_tabs=int(input("\n\nEnter the Number of Accounts:\n"))

hour=input("\n\nHour:")
minutes=input("\nMinutes:")
second=input("\nSeconds:")
milliseconds=input("\nMilliseconds:")
entry_time = int(f"{hour}{minutes}{second}{milliseconds}")

# ! Links input
for i in range(0,number_of_links):
    links.append(input(f"\n\nEnter Link {i+1}:\n"))

# ! Loop to open multiple chrome instances V2
for i in range(0,number_of_tabs):
    tabs.append(str(9014+i))
    subprocess.Popen(f'chrome.exe --remote-debugging-port={tabs[i]} --user-data-dir="{current_path}\\Chrome_Files\\Chrome_Test_Profile_{i+1}"', shell=True)
    time.sleep(3)
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress",f"127.0.0.1:{tabs[i]}")
    driver.append(webdriver.Chrome(PATH,chrome_options=chrome_options))
    time.sleep(3)
    driver[i].get(links[0])
    time.sleep(26)
# ! Loop to open multiple links V2
    for j in range(1,number_of_links):
        drivers=driver[i]
        drivers.switch_to.new_window()
        time.sleep(3)
        drivers.get(links[j])
        time.sleep(26)

# #! Initializing the time from the PC
now = datetime.now()
submit_time = int((int(now.strftime("%H%M%S%f"))/1000))

# #! Submiting the entry loop
while True:
    if submit_time>=entry_time:
        for i in range(0,number_of_tabs):
            for handle in driver[i].window_handles:
                driver[i].switch_to.window(handle)
                try:
                    search_submit_button=driver[i].find_element_by_class_name("button-submit")
                except NoSuchElementException as exception:
                    driver[i].get(links[1])
                    time.sleep(5)
                finally:
                    search_submit_button.click()
        print("Done")
        break
    else:
        now = datetime.now()
        submit_time = int(int(now.strftime("%H%M%S%f"))/1000)      