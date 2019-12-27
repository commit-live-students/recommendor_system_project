# %load q03_plot_topK_subreddit_of_a_user/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q03_plot_topK_subreddit_of_a_user(path, user='kabanossi', k= 14):
    
    df, u_user, u_subreddit = q01_Unique_users_subreddit(path)
    df1= df.groupby('subreddit')['username'].count().reset_index().sort_values('username',ascending=False)
    df1['percentage'] = df1['username'].apply(lambda value: (float(value)/total_user)*100)
    return df1[:k]

path = 'data/subreddit-interactions-for-25000-users.zip'
q03_plot_topK_subreddit_of_a_user(path, user='kabanossi', k= 14)


