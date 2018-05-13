# %load q01_Unique_users_subreddit/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/subreddit-interactions-for-25000-users.zip'
def q01_Unique_users_subreddit(path):
    data = pd.read_csv(path,compression='zip')
    variable1 = len(data.username.unique())
    variable2 = len(data.subreddit.unique())
    return data,variable1,variable2



