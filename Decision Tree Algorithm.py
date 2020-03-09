#!/usr/bin/env python
# coding: utf-8

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# X is the set of independent variables from the data
# y is the dependent variable which needs to be predicted

train_X,val_X,train_y,val_y=train_test_split(X,y,random_seed=1)
model=DecisionTreeRegressor(random_state=1)
# model=DecisionTreeRegressor(max_leaf_nodes=100,random_state=1)
model.fit(train_X,train_y)
val_predictions=model.predict(val_X)
print(mean_squared_error(val_y,val_predictions))


# Optimizing decision trees from underfitting/over fitting
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
candidate_max_leaf_nodes=[5, 25, 50, 100, 250, 500]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = min(scores, key=scores.get)
print(scores)
print(best_tree_size)



# Now build the model on complete data
model=DecisionTreeRegressor(max_leaf_nodes=100,random_state=1)
model.fit(X,y)

