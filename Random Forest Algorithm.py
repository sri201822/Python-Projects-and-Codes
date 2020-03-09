#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
train_X,val_X,train_y,val_y=train_test_split(X,y,random_state=1)
forest_model=RandomForestRegressor(random_state=1)
forest_model.fit(train_X,train_y)
val_predictions=forest_model.predict(val_X)
print(mean_absolute_error(val_y,val_predictions))

