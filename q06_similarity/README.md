# Finding similarity

This assignment will be comprising of finding the similarity between one user to another user or one subreddit to another subreddit. 

## Write a function `similarity()` that:
* Calculates the cosine similarity. 
* The dataframe has been preloaded for you using the **function q05_groupby_users_subreddit()**. Pass the required path as an     argument to the function. Take only the first 100 rows; this is done for computational purposes.
* Make a pivot table of the new dataframe using the **.pivot_table()**  method and pass the parameters inside it as **values**   equal to *weights*, **columns** equal to *subreddits* and **index** equal to *username*. It will create a user-subreddit       matrix and store it with a new name. Fill all the **NA**s there with zero using the **.fillna(0, inplace=True)** method.
* You will be generating a subreddit similarity matrix here. Use the **cosine_similarity()** on the transpose of the matrix in   the previous step. 
* Now, to generate a dataframe, set the columns and index of the similarity matrix equal to the subreddit names.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | str | compulsory |  | file path of the subreddit interaction dataset |
| kind | string | compulsory | 'subreddit' | type of similarity you want to compute |
| similarity_function | function name | compulsory | cosine_similarity | type of similarity you want to compute |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| data | pandas dataframe | dataframe containing the cosine smilarity values of required type|


