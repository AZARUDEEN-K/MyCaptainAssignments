#!/usr/bin/env python
# coding: utf-8

# Input : Please enter a string Mississippi
# 
# Output : i = 04 s = 04 p =02 m =01 

# In[1]:


import collections


# In[5]:


name = input("Please Enter a string: ")


# In[7]:


repetion = collections.Counter(name)

rep = {}


for key, value in repetion.items():
    if value >= 1:
        rep[key] = value
print("Output: "+str(rep))


# In[ ]:




