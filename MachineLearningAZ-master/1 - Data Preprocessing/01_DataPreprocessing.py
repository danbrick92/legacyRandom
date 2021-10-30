# Data Preprocessing

# Importing the libraries
import numpy as np # Numpy is used to do mathematical operations in Python
import matplotlib.pyplot as plt # Matlplotlib is used to plot graphs and charts
import pandas as pd # Pandas is used to manage data sets

# Get directory, subdirectory, filename
with open('/Users/MLAZ.txt') as file:
    directory = file.read()
    
subject_name = "1 - Data Preprocessing"
file_name = "Data.csv"

# Importing the dataset
dataset = pd.read_csv(directory.replace('\n','') + "/" + subject_name + "/" + file_name)
X = dataset.iloc[:,:-1].values # This gets all of the features. 
    # In the case above, we want to grab all rows, and all but the last column (since it contains the y value)
y = dataset.iloc[:,3].values # This gets all of the outputs
    # We want all rows, but only the last column since it is the y value

# Take care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
    #missing_values typically seen in dataset as "nan", this allows imputer to recognize those values
    #strategy, for missing values, can use mean ,median, or mode of column data
    #axis: use 0 to take mean of columns, 1 for rows (in this case, it makes sense with rows)
imputer = imputer.fit(X[:,1:3])
    # Fit imputer only to columns that need fixing up
X[:,1:3] = imputer.transform(X[:,1:3])
    # Apply transformation
    
# Encode categorical data 
# (cannot process labels like Spain, France, must be turned into numbers 0,1,2,etc...)
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder() # Declare our label encoder
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # tranform all lines of column 0 (Country)
# Problem: If France 1, Germany is 2, that means France > Germany? No, garbage. Need to handle this.
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features= [0]) #One hot encoder takes care of this, 
X = onehotencoder.fit_transform(X).toarray() # This creates three columns which receive a 1 or 0, correlating to France, Germany, or Spain 

# Training and Test Model
# Need to create two models.
# One is a training model, where we build the algorithm
# The other is a test model, where we test the performance of the machine learning model
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) #test size means we test on 20% of the data, random state = 0 to match his code

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler() # Does feature scaling
X_train = sc_X.fit_transform(X_train) #Scaling is fitted to the X_train dataset
X_test = sc_X.transform(X_test) #Apply scaling from previous statement to X-test
# No need for feature scaling on y, categorical binary variable