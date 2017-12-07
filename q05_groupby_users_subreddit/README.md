# Group by weights

This assignment will be comprising of 

## Write a function `groupby_users_subreddit()` that:
* Uses the function **q04_weightage()** generated in the previous assignment to create a dataframe.
* Creates a new dataframe using the **.groupby()** method which groups the sum of the weights according to username and           subreddit.
* Converts the dtype of **weight** into float32 using the **.astype()** method. 

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | str | compulsory |  | file path of the subreddit interaction dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| data | pandas dataframe | dataframe with addtional column of weights |
