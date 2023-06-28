#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')

theme.head()


# In[4]:


theme.head(50)


# In[46]:


merged = df.merge(theme, left_on = 'parent_theme', right_on='name')
merged.head()


# In[6]:


df.head()


# In[7]:


theme.head()


# In[27]:


merged = df.merge (theme, left_on = 'parent_theme', right_on = 'name')
merged.drop(columns= 'name_y', inplace =True)
merged.head()


# In[34]:


len(merged['set_num'].isnull())


# In[35]:


licensed = merged[merged['is_licensed']]
licensed = licensed.dropna(subset=['set_num'])
licensed.head()

star_wars = licensed[licensed['parent_theme']=='Star Wars']

the_force = int(star_wars.shape[0]/licensed.shape[0]*100)

print(the_force)


# In[36]:


licensed.head()


# In[45]:


licensed_sorted = licensed.sort_values('year')
license_sorted['count']= 1

summed_df = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()

max_df = summed_df.sort_values('count', ascending=False).drop_duplicates(['year'])
max_df.sort_values('year', inplace=True)
max_df


# In[ ]:




