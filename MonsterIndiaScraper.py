
# coding: utf-8

# In[91]:


########################## MonsterIndia.com

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "http://www.monsterindia.com/data-scientist-jobs-in-mumbai.html"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
#print(soup.prettify())


# In[69]:


########## Job title
title = []
for div in soup.find_all(name="span", attrs={"class":"title_in", "style":"margin-right:2px;"}):
    title.append(div.get_text())
    #print(div.get_text())
    
########## Company Name
name = []
for div in soup.find_all(name="div", attrs={"class":"jtxt orange"}):
    name.append(div.get_text())
    #print(div.get_text())
    
########## Job Location
location = []
for div in soup.find_all(name="div", attrs={"class":"jtxt jico ico1"}):
    location.append(div.get_text())
    #print(div.get_text())
    
########## Experience
exp = []
for div in soup.find_all(name="div", attrs={"class":"jtxt jico ico2"}):
    exp.append(div.get_text())
    #print(div.get_text())
    
########## Skills:
I = []
skills = []
for div in soup.find_all(name="div", attrs={"class":"jtxt"}):
    I.append(div.get_text())
    #print(div.get_text())
import re
for i in range(0,len(I)):
    match = re.search("Keyskills",I[i])
    if match:
        skills.append(I[i])       
#print(skills)

########## ApplyLinks
applylinks = []
for link in soup.find_all(name="a", attrs={"class":"btn pull-right apply", "role":"button", "target":"_blank"}):
    applylinks.append(str(link.attrs['href']))


# In[99]:


applylinks = []
for link in soup.find_all(name="a", attrs={"class":"btn pull-right apply", "role":"button", "target":"_blank"}):
    applylinks.append(str(link.attrs['href']))


# In[70]:


for i in range(1,39):
    print(title[i]+","+name[i]+","+location[i]+","+exp[i]+","+skills[i]),
    print("\n")


# In[90]:


for i in range(1,10):
    s = str(skills[i])
    s.replace('Keyskills:',' ')
    s.replace('"', '')
    print(s)

