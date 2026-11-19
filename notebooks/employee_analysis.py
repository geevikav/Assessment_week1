#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pylot as plt
print("Employee Analysis Project")

# In[2]:


%pip install pandas matplotlib

# In[3]:


import pandas as pd 
import matplotlib.pyplot as plt
print("Employee Analysis project")


# In[4]:


import os 
print(os.listdir("../dir"))


# In[5]:


import os 
print(os.get.cwd())

# In[6]:


import os
print(os.getcwd())


# In[7]:


import os
print(os.listdir("data"))

# In[8]:


import  pandas as pd
df = pd.read_csv("data/Employee.csv")
df.head()


# In[9]:


print("Total Employees:",len(df))
print("\nColumn Names:",df.columns.tolist())
print("\nMissing Values:",df.isnull().sum())

# In[10]:


print(df["department"].value_counts())


# In[11]:


print(df.groupby("department")["salary".mean())


# In[12]:


print(df.groupby("department")["salary"].mean())

# In[13]:


print("Highest Salary:", df["salary"].max())
print("Lowest Salary:", df["salary"].min())
print("Overall Average Salary:", df["salary"].mean())

# In[14]:


%timeit df["salary"].mean()

# In[15]:


df.groupby("department")["salary"].mean().plot(
    kind="bar",
    title="Average Salary by Department",
    xlabel="Department",
    ylabel="Average Salary"
)

plt.show()

# In[ ]:




# In[ ]:




# # Employee Data Analysis
# 
# ## 1. Dataset overview
# ## 2. Department-wise Employee Count
# ## 3. Average Salary Analysis
# ## 4. Salary Statistics
# ## 5. Visualization and Findings 
# 

# In[ ]:



