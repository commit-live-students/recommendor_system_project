# %load q02_top_subreddits_wordcloud/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q02_top_subreddits_wordcloud(path):
    
    # importing data
    df, u_user, u_subreddit = q01_Unique_users_subreddit(path)
    # Generating a DataFrame that comprise count of each username  by subreddit
    df_count_subreddit = df.groupby('subreddit')['username'].count().reset_index().sort_values('username',ascending = False)
    # setting subreddit name as index of dataframe
    df_count_subreddit.index = df_count_subreddit['subreddit']
    df_count_subreddit.drop('subreddit', inplace = True,axis = 1)
    #creating dictionary of dataframe where key is subreddit name and value is frequency of particular subreddit
    d = df_count_subreddit.to_dict()['username']
    # creating object of wordCloud
    wordcloud = WordCloud()
    # generating wordcloud with frequencies store in dictionary
    wordcloud.generate_from_frequencies(frequencies=d)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


path = 'data/subreddit-interactions-for-25000-users.zip'
q02_top_subreddits_wordcloud(path)
ls


