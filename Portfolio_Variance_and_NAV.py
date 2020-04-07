#!/usr/bin/env python
# coding: utf-8

# <b>Portfolio Variance</b>

# In[1]:


import pandas as pd
import pandas_datareader.data as pdr    #Import Libraries
import datetime as dt
import numpy as np


# In[2]:


ticker = ['CONCOR.NS','NESTLEIND.NS','ASIANPAINT.NS','HDFCBANK.NS','INFY.NS']   #Stocks of your portfolio
Wt_Stocks = [0.23,0.21,0.17,0.19,0.20]   #Weight per stock


# In[3]:


start_date = dt.datetime(2020,4,3) - dt.timedelta(735)        # Specify the start and end date
end_date = dt.datetime(2020,4,3)


# In[4]:


data = pdr.get_data_yahoo(ticker,start_date,end_date)      #Get data from Yahoo Finance API


# In[5]:


df_close = data['Adj Close']     #Extract adjusted close data from whole price data
df_close


# In[6]:


df_ret = df_close.pct_change(1)     #Find the daily return
df_ret = df_ret.round(4)             #Round to 4 decimal places
df_ret


# In[7]:


avg_ret = df_ret.iloc[1:df_ret.size].mean()      # Find the average return over the period
avg_ret = avg_ret.round(4)   #Round to 4 decimal places
avg_ret


# In[8]:


X = df_ret - avg_ret
X = X.iloc[1:X.size]   #Excess Return Matrix (Excluding NaN value at the top)
X


# In[9]:


X_n = X.reset_index()       #To remove date as datetime index
X_n.drop(columns = 'Date',inplace = True)
X_n


# In[10]:


X_nT = X_n.loc[0:X_n.size,ticker[0]:ticker[-1]].T       # Transpose of matrix X


# In[11]:


XTX = X_nT.dot(X_n)       #Transpose(X) * (X)


# In[12]:


n = len(X_n.axes[0])   #Find the number of data points


# In[13]:


var_cov_mtx = XTX/n                     #Find the variance covariance matrix
var_cov_mtx = var_cov_mtx.round(5)
var_cov_mtx


# In[14]:


S_Dev = df_ret.std()             #Find the standard deviation of each stock
S_D = pd.DataFrame(S_Dev)
S_D = S_D.round(5)
S_D


# In[15]:


S_DT = S_D.T   #Find the transpose of S.D
S_DT


# In[16]:


Pro_SD = S_D.dot(S_DT)      #Dins SD * SDT
Pro_SD = Pro_SD.round(5)
Pro_SD


# In[17]:


corr_mtx = var_cov_mtx.div(Pro_SD)    # var_cov_mtx * Pro_SD
corr_mtx = corr_mtx.round(5)         #Correlation matrix
corr_mtx


# In[18]:


Wt_Stocks_df = pd.DataFrame(Wt_Stocks)           #Convert the weight of each stock into a dataframe
Wt_Stocks_df = Wt_Stocks_df.set_index(S_D.index)   #Set the index same as all others
Wt_Stocks_df


# In[19]:


Wt_SD = S_Dev * Wt_Stocks        # Find the weighted standard deviation of stocks
Wt_SD_df = pd.DataFrame(Wt_SD)
Wt_SD_df = Wt_SD_df.round(5)
Wt_SD_df


# In[20]:


M1 = Wt_SD_df.T.dot(corr_mtx)     # Transpose(Wt_SD) * Corr_mtx
M1


# In[21]:


M2 = M1.dot(Wt_SD_df)    #M1 * Wt_SD
M2


# In[22]:


Port_Var = M2[0].apply('sqrt')    #Sqrt(M2) = Portfolio Variance or Portfolio S.D
Port_Var = Port_Var*100
Port_Var = Port_Var.round(3)
Port_Var


# In[23]:


Wt_port_ret = Wt_Stocks_df.T.mul(100)    # Convert stock weights into percentages
Wt_port_ret


# In[24]:


port_dret = pd.concat([Wt_port_ret,df_ret[1:]], ignore_index = True)    #Concatenate previous dataframe to weighted stocks dataframe
port_dret


# In[25]:


for i in range(1,len(port_dret.index)):
    port_dret.iloc[i] = port_dret.iloc[i-1]*(1+port_dret.iloc[i])     #Portfolio's daily returns


# In[26]:


port_dret


# In[27]:


port_dret['NAV'] = port_dret.sum(axis = 1)     #Returns in terms of NAV
port_dret


# In[28]:


port_dret = port_dret.set_index(df_ret.index)    #Set the date index
port_dret


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


NAV = port_dret['NAV']
NAV.plot()                              #Plot NAV (Net Asset Value)

