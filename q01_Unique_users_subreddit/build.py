# %load q01_Unique_users_subreddit/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit as original

path = 'data/subreddit-interactions-for-25000-users.zip'

def q01_Unique_users_subreddit(path):
    data = pd.read_csv(path, compression = 'zip')
    return data, np.unique(data.username).shape[0], np.unique(data.subreddit).shape[0]



