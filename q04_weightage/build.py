import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q04_weightage(path):
    data ,lenX, lenY = q01_Unique_users_subreddit(path)
    "write your solution here"
