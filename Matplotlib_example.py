#!/usr/bin/env python
# coding: utf-8

# ## Simple Graph:

# In[2]:


x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 51 ,52, 38, 47, 49, 46]


# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather")
plt.plot(x,y, color="Green", linewidth=2) #, linestyle='dotted')
plt.grid()


# ## Legends and grids:

# In[16]:


days = x
max_t = [50, 51, 52, 48, 47, 49, 46]
min_t = [43, 42, 40, 44, 33, 35, 37]
avg_t = [45, 48, 48, 46, 40, 42, 41]
plt.title("Weather")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.plot(days, max_t, label="Max Temp")
plt.plot(days, min_t, label="Min Temp")
plt.plot(days, avg_t, label="Avg Temp")
plt.legend(shadow="True")
plt.grid()


# ## Vertical Bars:

# In[28]:


import numpy as np
company = ['GOOGL','AMZN','MSFT','FB']
revenue = [90, 136, 89, 27]
profit = [40, 2, 34, 12]
xpos = np.arange(len(company))
xpos


# In[35]:


plt.title("US Tech Stocks")
plt.xlabel("Companies")
plt.ylabel("Revenues")
plt.xticks(xpos, company)  # set the xticks labels (company names)
plt.bar(xpos-0.2, revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2, profit, width=0.4, label="Profit")
plt.legend()


# ## Horizontal Bars:

# In[38]:


plt.title("US Tech Stocks")
plt.ylabel("Companies")
plt.xlabel("Revenues")
plt.yticks(xpos, company)  # set the xticks labels (company names)
plt.barh(xpos-0.2, revenue, height=0.4, label="Revenue")
plt.barh(xpos+0.2, profit, height=0.4, label="Profit")
plt.legend()


# ## Histograms:

# In[57]:


blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77 ,82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.xlabel('Sugar Range')
plt.ylabel('Total No of Patients')
plt.title('Blood Sugar Analysis')
plt.hist([blood_sugar_men, blood_sugar_women], 
         bins=[80, 100, 125, 150], 
         rwidth=0.95, 
         color=['green', 'orange'],
         label=['Men', 'Women']),
        #orientation='horizontal')  # print results as buckets
plt.legend()
plt.show()


# ## Pie Chart:

# In[71]:


exp_vals = [1400, 600, 300, 410, 250]
exp_labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]


plt.pie(exp_vals, 
        labels=exp_labels, 
        radius=1.5, 
        autopct="%0.2f%%", 
        shadow="True",
       explode=[0, 0.1, 0.1, 0, 0],
       startangle=45)


# ## Saving Graph to File:

# In[69]:


plt.savefig('piechart.png', 
            bbox_inches="tight",
           pad_inches=2,
           transparent=True)  # must save to file before plt.show()!

plt.show()  # remove the matplotlib text prints

