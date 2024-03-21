#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dinesh Sagar #######
#dineshsagar66@gmail.com#
#9000088487#
#07/24/23######## -- Dummy Commit

#Project - Build a webscraping crawler that can open the website and download all the PDF files and extract data from it.#

# Detailed Pipeline of my approach #

# Understand the problem --> design a workflow --> install required libraries and dependencies --> Selenium to open the website
# and crawl thorough it --> Find the a tags containing the download option --> Selenium clicks on download. --> pdf files are
# saved in local machine --> Importing libraries for pdf processing --> reading the pdf files and accumulating data and 
# saving the output to the file. Peform testing and then END>

##### Importing libraries######
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import easygui
from easygui import diropenbox,msgbox # My favorite graphical user interface which lets user to select files and folder.

###### Logic for GUI and selenium ################

show=msgbox("Hi Welcome to webscraper.\n\n I am ready to crawl and download the files \n\n Click on OK to proceed further!.",title='Webscraper - Testing model by DS')
takeinp=diropenbox("Select the folder to which you want to download the files:")
options = webdriver.ChromeOptions()

options.add_experimental_option('prefs',{
"download.default_directory":"{}".format(takeinp),
"download.prompt_for_download": False, # sometimes the pdf popsup in the website. but as we want to download, set it to False #
"plugins.always_open_pdf_externally": True})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

URL = 'https://www.hyundai.com/in/en/click-to-buy/request-a-brochure'
driver.get(URL)

driver.maximize_window()
driver.implicitly_wait(10) # Asking to wait 10 seconds for website to load in case of slow network #

all_the_tags = driver.find_elements(By.XPATH,'//a') # For getting all <a> tags #
count=0
for a in all_the_tags:
    if a.get_attribute('href') and '.pdf' in a.get_attribute('href') and 'Download' in a.text: # To fetch the download link 
        a.click() # crawler clicks on the download button #
        driver.implicitly_wait(10)
        count+=1
        if count >=10:
            break
            
##### Reading and processing pdf files which are downloaded by selenium #######        
            
import os
import PyPDF2 # one of the library for pdf processing, we can use tabula, camelot but used PyPDF2 for this testing. 
import pandas as pd

c='{}'.format(takeinp)
d=os.listdir(c)
try:
    for i in d:
        if i.endswith('.pdf'): # looping through the folder and checking only pdf files #
            file=c+"\\"+i
            reader=PyPDF2.PdfReader(file)
            count = len(reader.pages)
            for i in range(count):
                page = reader.pages[i]
                output = page.extract_text()
                output = str(output)
                with open("scrapeddata.txt","a") as f:
                    os.chdir(c)
                    f.write(output)
                
except UnicodeEncodeError as e: #some pdfs have encoding of utf-8 to save that kind of data.
    for i in d:
        if i.endswith('.pdf'): # looping through the folder and checking only pdf files #
            file=c+"\\"+i
            reader=PyPDF2.PdfReader(file)
            count = len(reader.pages)
            for i in range(count):
                page = reader.pages[i]
                output = page.extract_text()
                output = str(output)
                print(output)
                with open("scrapeddata.txt","a",encoding='utf-8') as f:
                    os.chdir(c)
                    f.write(output)
time.sleep(6)
driver.close()
print("Yayyyy! Successfully downloaded PDF's and extracted text from all the PDF's,\n\n The Files are placed here: {}".format(takeinp))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




