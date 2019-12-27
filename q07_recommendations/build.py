# %load q07_recommendations/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from greyatomlib.recommendor_system_project.q06_similarity.build import q06_similarity

def q07_recommendations(path, user='--ANUSTART-', similarity_function=cosine_similarity, kind='subreddit', number=5):
    'write your solution here'
    new_df, matrix = q06_similarity(path, kind='subreddit', similarity_function=cosine_similarity)
    final_dict = dict()
    sorted_sub = matrix.loc[user,:].sort_values(ascending=False).index
    for sub in sorted_sub:
        final_sub = new_df.loc[sub,:].sort_values(ascending=False)
        index = final_sub.index
        values = final_sub.values
        for i ,j in zip(index, values):
            final_dict[i]=j
    sorted_dict = sorted(final_dict.items(), key=lambda x: x[1],reverse=True)
    final = [x[0] for x in sorted_dict]
    recommend = [x for x in final if matrix.loc[user,x]==0.0]
    return recommend[0:number]




