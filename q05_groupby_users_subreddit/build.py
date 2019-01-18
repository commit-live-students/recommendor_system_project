# %load q05_groupby_users_subreddit/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q04_weightage.build import q04_weightage

def q05_groupby_users_subreddit(path):
    
    df = q04_weightage(path)
    df1 = df.groupby(['username','subreddit'])['weights'].sum().reset_index()
    
    return df1

path = 'data/subreddit-interactions-for-25000-users.zip'
q05_groupby_users_subreddit(path)


