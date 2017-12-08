# Finding similarity

This assignment will be comprising of finding the similarity between one user to another user or one subreddit to another subreddit. 

## Write a function `q07_recommendations()` that:
* Gives out recommendations to a particular used based on the similarities between either users or subreddits if that user     has not visited the subreddit before.
* The dataframes i.e. *subreddit similarity matrix* and *user-subreddit matrix* have been preloaded for you using the **q06_similarity(path, kind='subreddit', similarity_function = cosine_similarity)** from the previous assignment.
* Create an empty dictionary. Assign it a name.
* Create a list of the subreddits of the user in ascending order of the values. You can do it by using the **.loc[user,:]**     method on the **user-subreddit matrix** and then chaining it with the **.sort_values(ascending=False).index**. It will       generate a list of all the subreddits of that user in descending order.
* Iterate over every subreddit in the list, go to the subreddit similarity matrix and pick out its corresponding row and use   the **.loc[subreddit,:].sort_values(ascending=False)** and store it in a variable. Pick out its *index* and *values* and     store them in variables. 
* Now iterate over **zip(index, values)** and set the key as the index and value as the corresponding values. 
* Now, sort the dictionary in descending order according to the values(not the keys) and then create a list of keys. It will   be a list of subreddits.
* For the final step, recommend only those subreddits to the user if that subreddit has a null value in the **user-             similarity** matrix and display the top 5.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | str | compulsory |  | file path of the subreddit interaction dataset |
| user | str | compulsory | '--ANUSTART-' | username |
| similarity_function | function name | compulsory | cosine_similarity | type of similarity you want to compute |
| kind | string | compulsory | 'subreddit' | type of similarity you want to compute |
| number | int | compulsory | 5 | number of recommendations |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| recommendations | list | list containing the top 5 recommendations|


