# %load q02_top_subreddits_wordcloud/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

path = 'data/subreddit-interactions-for-25000-users.zip'

def q02_top_subreddits_wordcloud(path):
    data, users, subred = q01_Unique_users_subreddit(path)
    cloud = WordCloud(background_color='white',width=1600,height=800,relative_scaling=0.5,normalize_plurals=True)
    wordcloud = cloud.generate_from_frequencies(data['subreddit'].value_counts())
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()




