import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from greyatomlib.recommendor_system_project.q05_groupby_users_subreddit.build import q05_groupby_users_subreddit

def q06_similarity(path, kind='subreddit', similarity_function=cosine_similarity):
    df = q05_groupby_users_subreddit(path)
    "write your solution here" 
