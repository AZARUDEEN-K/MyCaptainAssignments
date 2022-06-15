#!/usr/bin/env python
# coding: utf-8

# In[20]:


Count = int(input("Enter Number of elements in the List: "))
List = []
print("Enter the elements: ",sep="/n")
for i in range(0,Count):
    num = input()
    List.append(num)


# In[21]:


print("Input: List")
for i in range(0,Count):
    print(List[i],sep=',')


# In[22]:


print("Output:")
for i in range(0,Count):
    if float(List[i]) > 0.0:
        print(List[i])

