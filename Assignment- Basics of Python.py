#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Calculate the sum of two integers and print the result
num1 = 3
num2 = 8
sum = num1 + num2
print('The sum is:',sum)


# In[7]:


# Calculate the average of three floating-point numbers and display the result
num1 = 1.2
num2 = 4.3
num3 = 7.2
average = (num1 + num2 + num3) / 3
print('The average is', average)


# In[10]:


# Concatenate two strings and print the combined string
str1 = "Hi"
str2 = "John"
combined_str = str1 + " " + str2
print("The combined string is", combined_str)


# In[12]:


string = "Hi John"


# In[16]:


# Extract a substring from a given string using Slicing
substring = string[4:7]
print("Substring", substring)


# In[20]:


# Count the number of occurrences of a specific character in a given string
String = "Hi John"
character = "0"
count = string.count(character)
print("Number of occurrences of", character, ":", count)


# In[23]:


# Convert a given string to lowercase
string = "Hi John"
lowercase_string = string.lower()
print("Lowercase String:", lowercase_string)


# In[26]:


#  Check if a given string ends with a specific substring
string = "Hi John"
substring = "John"
if string.endswith(substring):
    print("The string ends with", substring)
else:
    print("The string does not end with", substring)


# In[27]:


#  Replace a specific substring with another substring in a given string
string = "Hi John"
old_substring = "John"
new_substring = "Nikhil"
new_string = string.replace(old_substring, new_substring)
print("New substring", new_string)


# In[28]:


# Check if a given string contains only numeric characters
string = "0987672"
if string.isnumeric():
    print("The string contain the numeric characters")
else:
    print("The string does not contain any numeric characters")


# In[30]:


# Check if a given number is positive or negative using conditional statements
number = 5
if number > 10:
   print("The number is positive") 
elif number < 10:
    print("The number is negative")
else:
    print("The number is zero")


# In[ ]:




