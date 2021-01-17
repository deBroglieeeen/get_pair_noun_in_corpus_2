import pandas as pd
import timeit
#import scipy as sp
#import scipy.stat
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

X = pd.read_csv('output/df_sub_sum_analize.csv')
X['value'] = X['value'].replace(['၌','တွင်','မှာ'],[0, 1, 2])
print(X)
y = X.value
X.drop(['value'], axis = 1, inplace = True)

X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,random_state=0)
X_train = X_train_full
X_valid = X_valid_full
#X_test = X_test_full[my_cols].copy()

# One-hot encode the data (to shorten the code, we use pandas)
X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
#X_test = pd.get_dummies(X_test)
X_train, X_valid = X_train.align(X_valid, join='left', axis=1)
#X_train, X_test = X_train.align(X_test, join='left', axis=1)
#my_model_1 = XGBRegressor()

#my_model_1.fit(X_train,y_train)
#predictions_1 = my_model_1.predict(X_valid)

#mae_1 = mean_absolute_error(predictions_1,y_valid) # Your code here

# Uncomment to print MAE
#print("Mean Absolute Error:" , mae_1)

my_model_2 = XGBRegressor(n_estimators=1000,learning_rate=0.05) # Your code here

# Fit the model
# Your code here
print(timeit.timeit(lambda: my_model_2.fit(X_train,y_train,
               early_stopping_rounds=5,
               eval_set=[(X_valid,y_valid)],
               verbose=False),number=1))
# Get predictions
predictions_2 =  my_model_2.predict(X_valid)# Your code here
print(predictions_2)
# Calculate MAE
mae_2 = mean_absolute_error(predictions_2,y_valid) # Your code here

# Uncomment to print MAE
print("Mean Absolute Error:" , mae_2)
