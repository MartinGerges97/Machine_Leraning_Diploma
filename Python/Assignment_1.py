#!/usr/bin/env python
# coding: utf-8

# In[10]:


# map function takes two argumnets (the function ~capital~ , the list to iterate on ~names~)
# it will loop over the given list of any length and return True or False based on the conditon for all the values in the list
# map function took the rule of both if and for statements in one line of code. 


#code to check if the name in the list starts with a capital letter or not
def capital(names):
    return names[0]>='A' and names[0]<='Z'
    
names = ['Ahmed','ali', 'karem','martin']

capital_lett = map(capital,names)
print(list(capital_lett))

# output
# [True, False, False, False]



# In[11]:


# filter function works with the same concept of map function but with a difference that filter returns the 
# the value in the list we are iterating on. 


#code to find the names start wit a capital letter
def capital(names):
    return names[0]>='A' and names[0]<='Z'
    
names = ['Ahmed','ali', 'karem','martin']

capital_letter = filter(capital,names)
print(list(capital_letter))

# output
# ['Ahmed']



# In[ ]:




