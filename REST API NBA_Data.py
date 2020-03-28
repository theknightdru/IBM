#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install nba_api


# In[4]:


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    


# In[5]:


import pandas as pd


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


dict_={'a':[11,21,31],'b':[12,22,32]}


# In[8]:


df=pd.DataFrame(dict_)


# In[9]:


type(df)


# In[10]:


df


# In[11]:


from nba_api.stats.static import teams
import matplotlib.pyplot


# In[12]:


nba_teams=teams.get_teams()


# In[13]:


nba_teams


# In[14]:


nba_teams[0:3]


# In[15]:


dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)


# In[16]:


df_teams


# In[17]:


df_warriors=df_teams[df_teams['nickname']=='Warriors']


# In[18]:


df_warriors


# In[19]:


id_warriors=df_warriors[['id']].values[0][0]


# In[20]:


id_warriors


# In[21]:


from nba_api.stats.endpoints import leaguegamefinder


# In[22]:


gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)


# In[23]:


gamefinder


# In[24]:


gamefinder.get_json()


# In[25]:


games=gamefinder.get_data_frames()[0]
games.head()


# In[26]:


get_ipython().system(' wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl')


# In[27]:


file_name = "Golden_State.pkl"
games=pd.read_pickle(file_name)


# In[28]:


games.head()


# In[29]:


games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']


# In[30]:


games_home.mean()['PLUS_MINUS']


# In[31]:


games_away.mean()['PLUS_MINUS']


# In[32]:


fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()


# In[ ]:




