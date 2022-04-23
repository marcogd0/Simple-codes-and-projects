#!/usr/bin/env python
# coding: utf-8

# In[2]:


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    print(dig)
    print(num)
    print(rev)
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


# In[5]:


num = int(input("Enter a number:"))

temp = num
rev = 0

dig = num//10
print(dig)


# In[4]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def isPalindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]
 
 
# Driver code
s = "was it a car or a cat i saw"
ans = isPalindrome(s)
print(ans)
#print(isPalindrome(s))

s[::-1]
s[::-2]


#if ans:
#    print("Yes")
#else:
#    print("No")


# In[22]:


s[::-2]

