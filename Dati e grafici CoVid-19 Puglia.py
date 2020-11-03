#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates


# In[43]:


df = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (1).csv")
df.head()


# In[44]:


df.columns


# In[48]:


plt.plot( 'Date', 'Cases / Tests (weekly)', data=df, )
plt.show()


# In[52]:


dati = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (2).csv")
dati.head()


# In[53]:


dati.columns


# In[54]:


plt.plot( 'Date', 'Daily Tested People (weekly average)', data=dati, )
plt.show()


# In[ ]:




