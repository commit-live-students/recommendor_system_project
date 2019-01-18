# %load q04_weightage/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q04_weightage(path):
    
    df, u_user, u_subreddit = q01_Unique_users_subreddit(path)
    # minimum value in utc
    mininum = min(df['utc'])
    #maximum value in utc for normalization
    maximum = max(df['utc'])
    
    # creating weight column
    df['weight'] = ((df['utc'] - mininum)+1)/maximum
    
    return df
    

path = 'data/subreddit-interactions-for-25000-users.zip'
q04_weightage(path)


