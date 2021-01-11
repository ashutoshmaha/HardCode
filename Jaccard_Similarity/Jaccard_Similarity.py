#!/usr/bin/env python
# coding: utf-8

# # Program to calculate Jaccard Similarity Score with no external libraries.
# # Ashutosh Mahajan

# In[ ]:


# Algorithm:
# 1.start
# 2.convert all sent into lowercase.
# 3.split all sent into separate words in lists.
# 4.create a functn that intersects them. 
# 5.create a functn that unions them.
# 6.divide and print the number of words in both intersection and union to get the jaccard similarity score.
# 7.stop


# In[2]:


#Sample sentences to be processed are:

D1 = 'I asked him to buy apples for the cake'
D2 = 'Apple announces that new iphone will be released in this month'
D3 = 'My cat apple likes eating apples'
D4 = 'She will buy him an apple phone'

#conversion of uppercases to lower cases:
def tolowercase(sentence):
    return(sentence)

Da=D1
Dp=(Da.lower())
print(Dp)

Db=D2
Di=(Db.lower())
print(Di)

Dc=D3
Dm=(Dc.lower())
print(Dm)

Dd=D4
Du=(Dd.lower())
print(Du)


# In[3]:


# Split the sentences into separate words:
Dq=(Dp.split())
print(Dq)

Dj=(Di.split())
print(Dj)

Dn=(Dm.split())
print(Dn)

Dv=(Du.split())
print(Dv)


# In[4]:


# Intersections of all sentences:
def intersection(alpha, beta): 
    common_words = [value for value in alpha if value in beta] 
    return common_words 

#iteration 1 with Dq   
alpha=Dq      
beta=Dq
result1=intersection(alpha,beta)
print(result1)


alpha=Dq
beta=Dj
result2=intersection(alpha,beta)
print(result2)

alpha=Dq
beta=Dn
result3=intersection(alpha,beta)
print(result3)

alpha=Dq
beta=Dv
result4=intersection(alpha,beta)
print(result4)

#iteration 2 with Dj

alpha=Dj
beta=Dj
result6=intersection(alpha,beta)
print(result6)

alpha=Dj
beta=Dn
result7=intersection(alpha,beta)
print(result7)

alpha=Dj
beta=Dv
result8=intersection(alpha,beta)
print(result8)

#iteration 3 with Dn

alpha=Dn
beta=Dn
result11=intersection(alpha,beta)
print(result11)

alpha=Dn
beta=Dv
result12=intersection(alpha,beta)
print(result12)

#iteration 4 with Dv

alpha=Dv
beta=Dv
result16=intersection(alpha,beta)
print(result16)


# In[5]:


# Union of all sentences:
def Union(rho, psi): 
    all_words = rho + psi 
    return all_words

#iteration 1 with Dq
rho=Dq      
psi=Dq
outcome1=Union(rho,psi)
union1 = [i for i in outcome1]
for i in result1:
  if i in outcome1:
    union1.remove(i)
print(union1)


rho=Dq
psi=Dj
outcome2=Union(rho,psi)
union2 = [i for i in outcome2]
for i in result2:
  if i in outcome2:
    union2.remove(i)
print(union2)

rho=Dq
psi=Dn
outcome3=Union(rho,psi)
union3 = [i for i in outcome3]
for i in result3:
  if i in outcome3:
    union3.remove(i)
print(union3)

rho=Dq
psi=Dv
outcome4=Union(rho,psi)
union4 = [i for i in outcome4]
for i in result4:
  if i in outcome4:
    union4.remove(i)
print(union4)

#iteration 2 with Dj

rho=Dj
psi=Dj
outcome6=Union(rho,psi)
union6 = [i for i in outcome6]
for i in result6:
  if i in outcome6:
    union6.remove(i)
print(union6)

rho=Dj
psi=Dn
outcome7=Union(rho,psi)
union7= [i for i in outcome7]
for i in result7:
  if i in outcome7:
    union7.remove(i)
print(union7)

rho=Dj
psi=Dv
outcome8=Union(rho,psi)
union8 = [i for i in outcome8]
for i in result8:
  if i in outcome8:
    union8.remove(i)
print(union8)


# #iteration 3 with Dn

rho=Dn
psi=Dn
outcome11=Union(rho,psi)
union11 = [i for i in outcome11]
for i in result11:
  if i in outcome11:
    union11.remove(i)
print(union11)

alpha=Dn
psi=Dv
outcome12=Union(rho,psi)
union12 = [i for i in outcome12]
for i in result12:
  if i in outcome12:
    union12.remove(i)
print(union12)


# #iteration 4 with Dv

rho=Dv
psi=Dv
outcome16=Union(rho,psi)
union16 = [i for i in outcome16]
for i in result16:
  if i in outcome16:
    union16.remove(i)
print(union16)


# In[6]:


# Jaccard similarity scores of all the sentences:
# These scores will be filled up in the matrix row wise towards right and column wise downwards also:

#D1 to D1,D2,D3,D4

a1=(len(result1))/(len(union1))
print(a1)
a2=(len(result2))/(len(union2))
print(a2)
a3=(len(result3))/(len(union3))
print(a3)
a4=(len(result4))/(len(union4))
print(a4,'\n\n')

#D2 to D2,D3,D4

b2=(len(result6))/(len(union6))
print(b2)
b3=(len(result7))/(len(union7))
print(b3)
b4=(len(result8))/(len(union8))
print(b4,'\n\n')


#D3 to D3,D4


c3=(len(result11))/(len(union11))
print(c3)
c4=(len(result12))/(len(union12))
print(c4,'\n\n')


#D4 to D4

d4=(len(result16))/(len(union16))
print(d4,'\n\n')

