# Assign weightage

This assignment will be comprising of assigning a particular weightage to each observation.

## Write a function `weightage()` that:
* Makes use of the function used in the very first assignment *q01_Unique_users_subreddit* to make use of the dataframe           generated in that function.
* Assigns the weights by making a new column **weights** where each data point by first subtracting each data point by the         minimum value of minimum value of the **utc** column and add 1 to it(This is done to prevent null value occurence).
* Normalize the weights calculated by dividing each data point by the maximum value and stores it into new column named as    **weights**.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | str | compulsory |  | file path of subreddit interaction dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| data | pandas dataframe | dataframe with an addtional column of weights |
