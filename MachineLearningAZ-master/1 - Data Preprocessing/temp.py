# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # The : means get all lines, :-1 get all columns except the last
y = dataset.iloc[:, 3].values # 3 is the index of the last column, the one we left out on last line

# Taking care of the missing data (there is one age and one salary missing)
from sklearn.preprocessing import Imputer #used to preprocess data
imputer = Imputer(missing_values= 'NaN', #Impute = Infer compute, NaN is default and you can see missing data shows up as NaN
                  strategy = 'mean', #how it will calculate the missing values
                  axis = 0)  #
imputer = imputer.fit(X[:, 1:3]) # fit fits the dataset to the imputer, we use 1:3 because thos are in interested columns and lower index is included, outer is not
X[:, 1:3] = imputer.transform(X[:, 1:3]) #actually changes the dataset

# Encode categorical data (cannot process labels like Spain, France, must be turned into numbers 0,1,2,etc...)
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder() # Declare our label encoder
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # tranform all lines of column 0 (Country)
# Problem: If France 1, Germany is 2, that means France > Germany? No, garbage. Need to handle this.
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features= [0]) #One hot encoder takes care of this, 
X = onehotencoder.fit_transform(X).toarray() # This creates three columns which receive a 1 or 0, correlating to France, Germany, or Spain 

# Need to encode the purchased category, LabelEncoder will do just fine
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Need to create two models.
# One is a training model, where we build the algorithm
# The other is a test model, where we test the performance of the machine learning model
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) #test size means we test on 20% of the data, random state = 0 to match his code

# Will need to do some feature scaling, because ML uses Euclidean Distance which involves distance
# between square roots, one variable like salary will totally dominate the Age variable
# Feature scaling will put these numbers on the same scale
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler() # Does feature scaling
X_train = sc_X.fit_transform(X_train) #Scaling is fitted to the X_train dataset
X_test = sc_X.transform(X_test) #Apply scaling from previous statement to X-test
# No need for feature scaling on y, categorical binary variable