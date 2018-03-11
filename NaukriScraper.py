
# coding: utf-8

# In[39]:


########################## Naukri

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://www.naukri.com/data-scientist-jobs-in-mumbai"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())


# In[44]:


############# title
title = []
for div in soup.find_all(name="li", attrs={"itemprop":"title"}):
    title.append(div.get_text())
    
############# Company Name
name = []
for div in soup.find_all(name="span", attrs={"itemprop":"hiringOrganization"}):
    name.append(div.get_text())
    
############# Work Experience
exp = []
for div in soup.find_all(name="span", attrs={"itemprop":"experienceRequirements"}):
    exp.append(div.get_text())
    
############ Location
location = []
for div in soup.find_all(name="span", attrs={"itemprop":"jobLocation"}):
    location.append(div.get_text())

############ skills
skills = []
for div in soup.find_all(name="span", attrs={"itemprop":"skills"}):
    skills.append(div.get_text())
    
############ salary
salary = []
for div in soup.find_all(name="span", attrs={"itemprop":"baseSalary"}):
    salary.append(div.get_text())
    
############ Date Posted
dateposted = []
for div in soup.find_all(name="span", attrs={"class":"date"}):
    dateposted.append(div.get_text())
    
############ ApplyLinks
applylinks = []
for link in soup.find_all(name="a", attrs={"target":"_blank", "class":"content"}):
    applylinks.append(str(link.attrs['href'])) 
#print(applylinks)


# In[37]:


for i in range(1,20):
    print(title[i]+","+name[i]+","+ exp[i] +","+location[i]+","+skills[i]+","+salary[i]+","+dateposted[i])
    print("\n")


# In[38]:


from pandas import DataFrame
df = DataFrame({'Job title': title, 'Company Name': name, 'Work Experience': exp, 'Job Location': location, 'skills': skills, 'salary': salary, 'dateposted': dateposted})
df


# In[43]:


applylinks = []
for link in soup.find_all(name="a", attrs={"target":"_blank", "class":"content"}):
    applylinks.append(str(link.attrs['href'])) 
print(applylinks)

