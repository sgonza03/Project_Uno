#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Bring excel file into python
df = pd.read_csv(r'C:\Users\gonza\Documents\Projects\project1.csv', low_memory = False,)
print(df)


# In[3]:


#shrink data to get desired columns
c = df.loc[:,["pl_name","disc_year","discoverymethod","disc_facility","pl_masse","pl_dens"]]
c.head(11)


# In[4]:


#checking if column has all NaN values... if it does so what to do about them (line 11)
c.loc[:,"pl_masse"]


# In[5]:


#Create df for mass and density calculation
plt.scatter('pl_masse', 'pl_dens', color = 'red' ,data = c)
plt.xlabel('Number of Earth masses of Planet found')
plt.ylabel('density of planet found in g/cm**3')
plt.show()


# In[6]:


#stats on density and mass
ds = pd.DataFrame(c)
mean_mass = ds.loc[:,"pl_masse"].mean()
print(f'the mean planet mass is {mean_mass}')
mean_density = ds.loc[:,"pl_dens"].mean()
print(f'the mean planet density is {mean_density}')
mass_std= ds.loc[:,"pl_masse"].std()
print(f'the standard deviation for planet mass is {mass_std}')
den_std = ds.loc[:,"pl_dens"].std()
print(f'the standard deviation for planet density is {den_std}')
max_mass = ds.loc[:,"pl_masse"].max()
print(f"the max planet mass is {max_mass}")
max_dens = ds.loc[:,"pl_dens"].max()
print(f'The max planet density is {max_dens}')
min_mass = ds.loc[:,"pl_masse"].min()
print(f'The min planet mass is {min_mass}')
min_dens = ds.loc[:,"pl_dens"].min()
print(f'The min planet density is {min_dens}')


# In[7]:


#plot of individual axis... first rename first index to make x axis (create a range)... i accidently added too many x_axis columns
#first didnt put range so only got length
index = c.index
number_of_rows = range(len(c))
c.insert(0, "x_axis_2", number_of_rows, True)
c.head()


# In[8]:


#individual graphs against the new axis (density)
plt.scatter('x_axis_2', 'pl_dens', color = 'green' , data = c)
plt.ylabel('Density')
plt.xlabel('Sample Number')
plt.title('Density Graph')


# In[9]:


#individual graph of mass
plt.scatter('x_axis_2', 'pl_masse', data = c)
plt.ylabel('Number of Earth Masses')
plt.xlabel('Sample Number')
plt.title('Mass Graph')


# In[10]:


#time to fix the c data frame by removing the extra copies of the colums :(
# code used was c.drop(columns = ['x_axis'])
c.head()


# In[11]:


#first count the NaN values/ create df to check missing values of data (originally made this after In 4)
#just did count to see how many samples i had. Realized mean doesnt care about NaN values so left them 
ds = pd.DataFrame(c)
print(ds.loc[:,"pl_masse"].notna().sum())
print(ds.loc[:,"pl_dens"].notna().sum())
print(ds.loc[:,"pl_name"].notna().sum())
print(ds.loc[:,"disc_year"].notna().sum())
print(ds.loc[:,"discoverymethod"].notna().sum())
print(ds.loc[:,"disc_facility"].notna().sum())


# In[12]:


#count up discoveries per year
yr = df.loc[:,'disc_year']
years = pd.DataFrame(yr)
years.head(25)
groups = years.apply(pd.Series.value_counts, axis=0)
print(groups)


# In[13]:


#Graph discoveries per year(order w/out years in order)
groups.plot(kind = 'bar')
plt.ylabel('Number of Discoveries')
plt.xlabel('Year')
plt.title('Discoveries per Year')


# In[14]:


#count up discovery method
m = df.loc[:,'discoverymethod']
met = pd.DataFrame(m)
met.head(25)
metgroups = met.apply(pd.Series.value_counts, axis=0)
print(metgroups)


# In[15]:


#graph of discovery method
metgroups.plot(kind = 'bar')
plt.ylabel('Number of Discoveries')
plt.xlabel('Discovery Method')
plt.title('Most popular Discovery method')


# In[16]:


#count up facility (frequency)
y = df.loc[:,'disc_facility']
fac = pd.DataFrame(y)
fac.head(25)
facgroups = fac.apply(pd.Series.value_counts, axis=0, normalize = True)
print(facgroups)


# In[17]:


#graph of discovery facility
facgroups.plot(kind = 'bar')
plt.ylabel('Relative Frequency')
plt.xlabel('Facility')
plt.title('Discoveries per Facility')


# In[18]:


#Number of unique discovery methods per facility
c.groupby('disc_facility')['discoverymethod'].nunique().plot(kind='bar')
plt.show()


# In[19]:


#Number of unique facilicty per method
c.groupby('discoverymethod')['disc_facility'].nunique().plot(kind='bar')
plt.show()


# In[20]:


#Number of unique year discovered per facility
c.groupby('disc_facility')['disc_year'].nunique().plot(kind='bar')
#plt.show()
plt.subplots_adjust(top = 5 , bottom= 4.6)


# In[21]:


#Interested in seeing what the mass and density graphs will look without NaN values.
#making copy of data to make sure i dont change one ive already used
zzz = pd.DataFrame(c)
zzz.replace(np.nan,0)


# In[25]:


#NaN values replaced, so going to graph mass and density (individually) and see if graphs changed.
plt.scatter('x_axis_2', 'pl_dens', color = 'yellow' , data = zzz)
plt.ylabel('Density')
plt.xlabel('Sample Number')
plt.title('Density Graph with NaN replaced')
#showing  original graph 


# In[24]:


#original plot/graph without the zeros. 
plt.scatter('x_axis_2', 'pl_dens', color = 'green' , data = c)
plt.ylabel('Density')
plt.xlabel('Sample Number')
plt.title('Density Graph')


# In[ ]:




