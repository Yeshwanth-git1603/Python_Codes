#!/usr/bin/env python
# coding: utf-8

# In[3]:


#important functions in dictionary

d={"name":"yeshwanth","age":"23","fav_sport":"formula 1"}
print(type(d))
d=dict(d)
print(d)

# creating a list of tuple elements in dictionary

values=[("name","yeshwanth"),("age","23")]
res=dict(values)
print(res)

result={x for x in res}
print(type(result))


# In[ ]:


# printing the keys and values


print(d)
print(d.values())
for x in d.values():
    print(x)
for y in d.keys():
    print(y)


# In[ ]:


# printing the sum of values in the dictionary
d={"num1":1,"num2":2,"num3":3}
sum=0
for x in d.values():
    sum=sum+x
    print(sum)
    

    


# In[ ]:


vowels=['a','e','i','o','u']
v=input("enter the value")
for f in v:
    if f in vowels:
        print('found',f)
    else:
        print('not found',)


# In[ ]:


# sum of n numbers
n=int(input("enter the numbers"))
sum=0
for x in range(n):
    sum=sum+x
    print(sum)


# In[ ]:


# dictionary comprehension

loop={x:x for x in range(1,10)}
print(loop)

names={"name":"yesh" for x in range(1,10)}
print(names)

ages={x:y for x in range(1,5)
     for y in range(x)}
print(ages)


# In[ ]:


# user defined functions

def cars(name,brand,price):
    print(name,brand,price)
    
    
cars("911gt3rs","porsche","350k")


# using function to add numbers

def add(a,b):
    c=a+b
    print(c)
    
add(1,2)

# using function to add the numbers

def numbers():
    x=int(input("enter the number"))
    sum=0
    for n in range(x):
        sum=sum+n
        print(sum)
numbers()


# In[ ]:


# writing a function to accept 2 numbers and return its sum

def nums(a,b):
    return a+b

res=nums(1,2)
print("the sum is",res)
print("the sum is",nums(100,20))
    

#checking a number whether it is even or odd using function

def cal():
    n=int(input("enter the number to check"))
    if n % 2==0:
        print("even")
    else:
        print("odd")
cal()



# In[4]:


# finding the factorial of a given number

def fact():
    n=int(input('enter a number'))
    sum=0
    for x in range(n[::-1]):
        sum=sum*x
        print(sum)
        
fact()


# In[ ]:




