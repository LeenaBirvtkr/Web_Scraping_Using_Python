#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
import time
from bs4 import BeautifulSoup
import requests


# In[7]:


try:
    page=requests.get("https://economictimes.indiatimes.com/news/economy/articlelist/1286551815.cms")
    
except:
    error_type, error_obj, error_info=sys.exc_info()
    print('Error for link',error_info.tb_lineno)


# In[8]:


page


# In[9]:


soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class':'eachStory'})


# In[10]:


soup


# In[11]:


links


# In[12]:


for i in links:
    print(i.text)
    print('\n')


# In[15]:


for index, i in enumerate(links, 1):
    print(f"News {index}:")
    print(i.text)
    print('\n')


# In[ ]:




