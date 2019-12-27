# %load q01_Unique_users_subreddit/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_Unique_users_subreddit(path):
    
    df = pd.read_csv(path, compression='zip')
    variable1 = len(df['username'].unique())
    variable2 = len(df['subreddit'].unique())
    
    return df,variable1, variable2


path = 'data/subreddit-interactions-for-25000-users.zip'
q01_Unique_users_subreddit(path)



