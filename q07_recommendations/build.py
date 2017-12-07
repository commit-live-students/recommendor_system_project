import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from greyatomlib.recommendor_system_project.q06_similarity.build import q06_similarity

def q07_recommendations(path, user='--ANUSTART-', similarity_function=cosine_similarity, kind='subreddit', number=5):
    new_df, matrix = q06_similarity(path, kind='subreddit', similarity_function=cosine_similarity)
    "write your solution here"
