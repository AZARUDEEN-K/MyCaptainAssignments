#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[3]:


PI = math.pi


# In[14]:


Radius = float(input("Input the radius of the circle :"))

area = Radius*Radius*PI


# In[15]:


print("Input the radius of the circle : %2f" %Radius, sep=" ")
print("The area of the circle with radius 1.1 is: %2f" %area)

