
# coding: utf-8

# In[22]:


########################## MonsterIndia.com

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://www.indeed.co.in/Android-Developer-jobs-in-Mumbai,-Maharashtra"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())


# In[15]:


################## Job title
title = []
for div in soup.find_all(name="h2", attrs={"class":"jobtitle"}):
    title.append(div.get_text())
    
################## Company Name
name = []
for div in soup.find_all(name="span", attrs={"class":"company"}):
    name.append(div.get_text())
    
################## Location
location = []
for div in soup.find_all(name="span", attrs={"class":"location"}):
    location.append(div.get_text())
    
################## Summary
summary = []
for div in soup.find_all(name="span", attrs={"class":"summary"}):
    summary.append(div.get_text())
    
################## DatePosted
dateposted = []
for div in soup.find_all(name="span", attrs={"class":"date"}):
    dateposted.append(div.get_text())
    
applylinks = []
for link in soup.find_all(name="a", attrs={"target":"_blank", "rel":"noopener nofollow"}):
    applylinks.append("https://www.indeed.co.in/"+str(link.attrs['href'])) 
#print(applylinks)


# In[21]:


for i in range(1,10):
    print(title[i]+","+name[i]+","+location[i]+","+dateposted[i]+","+summary[i])
    print("\n")


# In[29]:


applylinks = []
for link in soup.find_all(name="a", attrs={"target":"_blank", "rel":"noopener nofollow"}):
    applylinks.append("https://www.indeed.co.in/"+str(link.attrs['href'])) 
print(applylinks)

