
# coding: utf-8

# In[150]:


import docx2txt
my_text = docx2txt.process(r'''C:\Users\lenovo\Desktop\resume\Rahul Vishwakarma.docx''')
print(my_text)


# In[151]:


from rake_nltk import Rake

r = Rake()

r.extract_keywords_from_text(my_text)

keywords = r.get_ranked_phrases()

print(keywords)


# In[98]:


########## Optional

#file = open(r'''C:\Users\lenovo\Desktop\resume\Bag of words.txt''', "r") 
#print(file.read())


# In[99]:


import sys, os, time

k = ['php','html','css','reactjs','web','angularjs','jquery','bootstrap','wordpress','ajax','apache','ruby','sql','json','java','python','deep learning','r','tensorflow','nlp','ml','machine learning','neural networks','spark','natural language processing','algorithm','analytic','image processing','big data','opencv','statistics','data','xml','ui','ux','git','android','sdk','eclipse','c++','rest','api','c-sharp','linux','native','ios','computer','science','testing','software']
ar = []

for i in range(0,50):
    for j in range(1,len(keywords)):
        if k[i] in keywords[j]:
            ar.append("1")
            time.sleep(0)
            
#print(ar)


# In[143]:


######## recieved designations:
import random
designations = ["Data Scientist", "Web developer", "Android Developer", "Embedded engineer", "Graphic Designer"]

key = random.randint(0,4) #Recieved

print(key)


# In[144]:


## Using MechanicalSoup

import mechanicalsoup

# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://duckduckgo.com/")

# Fill-in the search form
browser.select_form('#search_form_homepage')
browser["q"] = designations[key] + "job in mumbai"
browser.submit_selected()

# Display the results
c = 0
linksdb = []
for link in browser.get_current_page().select('a.result__a'):
    if c >= 1:
        #print(link.text, '->', link.attrs['href'])
        linksdb.append(link.attrs['href'])
    c = c + 1
    if c == 21:
        break;


# In[145]:


import re 
db1 = []
db2 = []
#lists = ["shine","indeed","monster","naukri","timesjob","angel","wisdomjobs"]
lists = ["indeed","monster","naukri"]
for i in range(0,len(linksdb)):
    for j in range(0,3):
        match = re.search(lists[j] , linksdb[i])
        if match:
            print(linksdb[i])
            print(lists[j])
            db1.append(linksdb[i])
            db2.append(lists[j])


# In[158]:


import sys, os, time
from pandas import DataFrame

for j in range(0,len(db2)-1):
    
    if db2[j] == "naukri":
        ########################## Naukri
        import requests
        import bs4
        from bs4 import BeautifulSoup
        import pandas as pd
        import time

        URL = db1[j]
        #conducting a request of the stated URL above:
        page = requests.get(URL)
        #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
        soup = BeautifulSoup(page.text, "html.parser")
        #printing soup in a more structured tree format that makes for easier reading
        #print(soup.prettify())
        
        ############# title
        title0 = []
        for div in soup.find_all(name="li", attrs={"itemprop":"title"}):
            title0.append(div.get_text())

        ############# Company Name
        name0 = []
        for div in soup.find_all(name="span", attrs={"itemprop":"hiringOrganization"}):
            name0.append(div.get_text())

        ############# Work Experience
        exp0 = []
        for div in soup.find_all(name="span", attrs={"itemprop":"experienceRequirements"}):
            exp0.append(div.get_text())

        ############ Location
        location0 = []
        for div in soup.find_all(name="span", attrs={"itemprop":"jobLocation"}):
            location0.append(div.get_text())

        ############ skills
        skills0 = []
        for div in soup.find_all(name="span", attrs={"itemprop":"skills"}):
            skills0.append(div.get_text())

        ############ salary
        salary0 = []
        for div in soup.find_all(name="span", attrs={"itemprop":"baseSalary"}):
            salary0.append(div.get_text())

        ############ Date Posted
        dateposted0 = []
        for div in soup.find_all(name="span", attrs={"class":"date"}):
            dateposted0.append(div.get_text())
            
        ############ ApplyLinks
        applylinks0 = []
        for link in soup.find_all(name="a", attrs={"target":"_blank", "class":"content"}):
            applylinks0.append(str(link.attrs['href'])) 
        #print(applylinks)
            
        for i in range(1,20):
            print(title0[i]+","+name0[i]+","+ exp0[i] +","+location0[i]+","+skills0[i]+","+salary0[i]+","+dateposted0[i]+","+applylinks0[i])
            print("\n")
            
        time.sleep(2)
    
    
    
    if db2[j] == "indeed":
        ########################## Indeed

        import requests
        import bs4
        from bs4 import BeautifulSoup
        import pandas as pd
        import time

        URL = db1[j]
        #conducting a request of the stated URL above:
        page = requests.get(URL)
        #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
        soup = BeautifulSoup(page.text, "html.parser")
        #printing soup in a more structured tree format that makes for easier reading
        #print(soup.prettify())
        
        ################## Job title
        title1 = []
        for div in soup.find_all(name="h2", attrs={"class":"jobtitle"}):
            title1.append(div.get_text())

        ################## Company Name
        name1 = []
        for div in soup.find_all(name="span", attrs={"class":"company"}):
            name1.append(div.get_text())

        ################## Location
        location1 = []
        for div in soup.find_all(name="span", attrs={"class":"location"}):
            location1.append(div.get_text())

        ################## Summary
        summary1 = []
        for div in soup.find_all(name="span", attrs={"class":"summary"}):
            summary1.append(div.get_text())

        ################## DatePosted
        dateposted1 = []
        for div in soup.find_all(name="span", attrs={"class":"date"}):
            dateposted1.append(div.get_text())
        
        ################## Applylinks
        applylinks1 = []
        for link in soup.find_all(name="a", attrs={"target":"_blank", "rel":"noopener nofollow"}):
            applylinks1.append("https://www.indeed.co.in/"+str(link.attrs['href'])) 
        #print(applylinks)
            
        for i in range(1,10):
            print(title1[i]+","+name1[i]+","+location1[i]+","+ "----" +","+summary1[i]+","+"----"+dateposted1[i]+","+applylinks1[i])
            print("\n")
            
        time.sleep(2)
        
        
    
    if db2[j] == "monster":
        ########################## MonsterIndia.com

        import requests
        import bs4
        from bs4 import BeautifulSoup
        import pandas as pd
        import time

        URL = db1[j]
        #conducting a request of the stated URL above:
        page = requests.get(URL)
        #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
        soup = BeautifulSoup(page.text, "html.parser")
        #printing soup in a more structured tree format that makes for easier reading
        #print(soup.prettify())
        
        ########## Job title
        title2 = []
        for div in soup.find_all(name="span", attrs={"class":"title_in", "style":"margin-right:2px;"}):
            title2.append(div.get_text())
            #print(div.get_text())

        ########## Company Name
        name2 = []
        for div in soup.find_all(name="div", attrs={"class":"jtxt orange"}):
            name2.append(div.get_text())
            #print(div.get_text())

        ########## Job Location
        location2 = []
        for div in soup.find_all(name="div", attrs={"class":"jtxt jico ico1"}):
            location2.append(div.get_text())
            #print(div.get_text())

        ########## Experience
        exp2 = []
        for div in soup.find_all(name="div", attrs={"class":"jtxt jico ico2"}):
            exp2.append(div.get_text())
            #print(div.get_text())

        ########## Skills:
        I2 = []
        skills2 = []
        for div in soup.find_all(name="div", attrs={"class":"jtxt"}):
            I2.append(div.get_text())
            #print(div.get_text())
        import re
        for i in range(0,len(I)):
            match = re.search("Keyskills",I[i])
            if match:
                skills2.append(I[i])       
        #print(skills)
        
        ########## apply links
        applylinks2 = []
        for link in soup.find_all(name="a", attrs={"class":"btn pull-right apply", "role":"button", "target":"_blank"}):
            applylinks2.append(str(link.attrs['href']))
        
        for i in range(1,39):
            print(title2[i]+","+name2[i]+","+location2[i]+","+exp2[i]+","+skills2[i]+","+"-----"+","+"--------"+","+applylinks2[i]),
            print("\n")
            
        time.sleep(2)


# In[178]:


str0 = []
for i in range(0,10):
    str0.append("{"+ "\"designation\"" + ":" + "\""+ title0[i] +  "\"" +","+ "\"Company Name\"" + ":" + "\""+ name0[i] +  "\""  + "," + "\"Work Experience\"" + ":" + "\""+ exp0[i] +  "\"" + "," + "\"Work Location\"" + ":" + "\""+ location0[i] +  "\""  + "," + "\"Skills\"" + ":" + "\""+ skills0[i] +  "\""  + "," + "\"Salary\"" + ":" + "\""+ salary0[i] +  "\""  + ",""\"Date Posted\"" + ":" + "\""+ dateposted0[i] +  "\""  + ",""\"Apply Links\"" + ":" + "\""+ applylinks0[i] +  "\""+"}" )
#print(str0)
str01 = str(str0).replace("'",'')
print(str01)

