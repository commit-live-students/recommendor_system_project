# %load q01_Unique_users_subreddit/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = '.data/subreddit-interactions-for-2500-user.csv'


def q01_Unique_users_subreddit(path):
    
    data =pd.read_csv(path, compression= 'zip')
    return data, len(data['username'].unique()), len(data['subreddit'].unique())



