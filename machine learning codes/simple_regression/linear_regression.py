#simple linear regression

#importing the required library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#importing the dataset
dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,1].values
y=dataset.iloc[:,0].values
x=x.reshape(-1,1)
y=y.reshape(-1,1)


#splitting of data into training set and test

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)


#fitting simple linear regression to the training set


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(xtrain,ytrain)
ypred=regressor.predict(xtest)

#visualising the training set

plt.scatter(xtrain,ytrain,color='blue')
plt.plot(xtrain,regressor.predict(xtrain),color='red')
plt.title('Salary VS Experience (Training Set)')
plt.ylabel('Years of Experience')
plt.xlabel('Salary')
plt.show()


#visualising the test set

plt.scatter(xtest,ytest,color='blue')
plt.plot(xtrain,regressor.predict(xtrain),color='red')
plt.title('Salary VS Experience (Test Set)')
plt.ylabel('Years of Experience')
plt.xlabel('Salary')
plt.show()



