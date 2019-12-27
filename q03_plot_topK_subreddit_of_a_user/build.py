# %load q03_plot_topK_subreddit_of_a_user/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q03_plot_topK_subreddit_of_a_user(path, user='kabanossi', k=14):
    data, users, subred = q01_Unique_users_subreddit(path)
    new_df = pd.DataFrame(data.groupby('username')['subreddit'].value_counts()[user][:k])
    new_df.plot.bar()
    plt.show();


