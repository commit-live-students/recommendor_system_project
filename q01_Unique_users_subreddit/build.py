import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_Unique_users_subreddit(path):
    "write your solution here"
    data1 =pd.read_csv(path, compression= "zip")
    data = data1.sample(frac=0.2, random_state=9)
    return data, len(data['username'].unique()), len(data['subreddit'].unique())

