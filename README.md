# Recommender system project
Welcome to Recommender system project.

In this project, you will demonstrate what you have learned in this course by conducting an experiment dealing with 'Reddit dataset'.

We have seen in the lectures how to make a user-item matrix and use it to generate recommendations using either the user-user or item-item similarity matrix.
In this exercise we will stepwise write to functions to build a recommender system.

## What we have learnt so far ..
- Popularity based recommender system
- Types of Collaborative Filtering
- Similarity functions
- Usage of the 'Surprise' package.
- Content based recommender system.

## Dataset
Now, we will try to build a recommendation system using both the user-user and item-item similarity matrices using 'cosine similarity' as the similarity measure on the 'Reddit dataset'.

### Features
* username : Username of the subreddit visitor
* subreddit : Name of the subreddit visited by the user
* utc : Timestamp of visit of the subreddit by the user

### What you will learn by solving this

- Basic revision of pandas groupby functions and wordcloud generation.
- How to calculate cosine similarity of a matrix.
- Generate user-user and item-item matrix.
- Throw out recommendations for a user.
