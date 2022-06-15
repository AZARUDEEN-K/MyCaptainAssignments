#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input("Enter the Number of Fibonacci series required: "))

a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a,sep=',')
    print(b,sep=',')
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(c,sep=',')


# In[ ]:




