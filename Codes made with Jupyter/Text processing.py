#!/usr/bin/env python
# coding: utf-8

# In[5]:


products = ["ABC123", "abd012", " ABS111", "Ab0222", "ahsushas"]
#produtos = "ABC123, abd012, ABS111, Ab0222"


# In[6]:


def text_processing(text):
    text = text.upper()
    text = text.strip() # remove spaces at the beginning and at the end of the string
    return text


# ## Conventional form using a for loop 

# In[3]:


for i, product in enumerate(products):
    products[i] = text_processing(product)
print(products)


# ## Using the map function

# In[7]:


print(products)
products = list(map(text_processing, products))
print(products)

