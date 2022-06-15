#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os


# In[12]:


Filename = input("Input the Filename:")


# In[13]:


split_tup = os.path.splitext(Filename)


# In[14]:


split_tup


# In[15]:


ext = split_tup[1]


# In[17]:


print("The extension of the file is : %s" %ext)


# In[ ]:




