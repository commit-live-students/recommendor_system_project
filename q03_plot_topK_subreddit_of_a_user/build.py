import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit

def q03_plot_topK_subreddit_of_a_user(path, user='kabanossi', k=14):
    data, lenX, lenY = q01_Unique_users_subreddit(path) 
    "write your solution here"
    

    
