# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:14:28 2018

@author: siddhant
"""
import numpy as np
from sklearn import svm
import os
import csv

import docx2txt
from rake_nltk import Rake

#=================================TRAINING


os.chdir(r'C:\Users\siddhant\Desktop\dbit_data\db1')

model = svm.SVC(kernel='linear', C=1, gamma=0.01)

ip = []
with open('data_in.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ip.append(row)

op = []
with open('data_out.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        op.append(row)


#test_vec = [input[10]]

answer=model.fit(ip,op)

#================================================EXTRACT FROM RESUME



my_text = docx2txt.process(r'C:\Users\siddhant\Desktop\dbit_data\db1\sh.docx')
#print(my_text)
r = Rake()
r.extract_keywords_from_text(my_text)
keywords = r.get_ranked_phrases()
#print(keywords)

#================================================CREATE BINARY TEST_VECTOR

# this is fixed 50 words
kwords = ['php','html','css','reactjs','web','angularjs','jquery','bootstrap','wordpress','ajax','apache','ruby','sql','json','java','python','deep learning','r','tensorflow','nlp','ml','machine learning','neural networks','spark','natural language processing','algorithm','analytic','image processing','big data','opencv','statistics','data','xml','ui','ux','git','android','sdk','eclipse','c++','rest','api','c-sharp','linux','native','ios','computer','science','testing','software']

arr=np.zeros(len(kwords))

#rwords = ['tech computer science machine learning gpa', 'image processing toolbox development team', '17 image processing engineer', 'played around material design', 'machine learning job', 'graphic design team', '16 graphic designer', '10 experience 2015', 'rahul vishwakarma mumbai', 'mumbai based startup', 'tech stuffs', 'team leader', 'mumbai b', 'several projects', 'new version', 'new toolboxes', 'extracurricular activities', 'com objective', 'year', 'writing', 'worked', 'vjti', 'usa', 'skills', 'sketching', 'rrvishwakarma12', 'python', 'pursue', 'passion', 'music', 'matlab', 'mathworks', 'maharashtra', 'looking', 'leading', 'java', 'india', 'head', 'google', 'gmail', 'employee', 'education', 'dream', 'developed', 'banglore', 'awards', 'awarded', 'apart', 'acknowledgements', '918692984677', '8', '2016', '2']
# this comes from rahul

rwords = keywords

for i in range(0,len(kwords)):
    if kwords[i]=='r':
        for j in range(0,len(rwords)):
            if kwords[i] == rwords[j]:
                arr[i]=1
    else:
        for j in range(0,len(rwords)):
            if kwords[i] in rwords[j]:
                #print('your skill is=  ',kwords[i])
                arr[i]=1

'''
for i in range(0,len(kwords)):
    print(kwords[i] , '==' , arr[i])
    print('\n')
'''

#================================================PREDICT ON RESUME VECTOR
answer = model.predict([arr])
#print(answer)

#print("job role to be assigned - ")
#print(model.predict(test_vec))