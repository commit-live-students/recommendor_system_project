
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from greyatomlib.recommendor_system_project.q05_groupby_users_subreddit.build import q05_groupby_users_subreddit

def q06_similarity(path, kind='subreddit', similarity_function=cosine_similarity):
    "write your solution here"
    df = q05_groupby_users_subreddit(path)
    df01 = df.iloc[:100,:]
    matrix= df01.pivot_table(values='weights',columns='subreddit',index='username')
    matrix.fillna(0, inplace=True)
    if kind == 'user':
        new_df = pd.DataFrame(similarity_function(matrix.values), columns=matrix.index, index=matrix.index)
        return new_df, matrix
    elif kind =='subreddit':
        new_df = pd.DataFrame(similarity_function(matrix.T.values), columns=matrix.columns, index=matrix.columns)
        return new_df, matrix
    else:
        pass

a = q06_similarity('data/subreddit-interactions-for-25000-users.zip')
print(a)
