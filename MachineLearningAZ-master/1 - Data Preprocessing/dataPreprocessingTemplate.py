# Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # The : means get all lines, :-1 get all columns except the last
y = dataset.iloc[:, 3].values # 3 is the index of the last column, the one we left out on last line

# Test and Training Models
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) #test size means we test on 20% of the data, random state = 0 to match his code

# Feature scaling 
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler() # Does feature scaling
#X_train = sc_X.fit_transform(X_train) #Scaling is fitted to the X_train dataset
#X_test = sc_X.transform(X_test) #Apply scaling from previous statement to X-test
