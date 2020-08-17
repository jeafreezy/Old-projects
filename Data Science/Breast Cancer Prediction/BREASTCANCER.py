# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 05:07:06 2018

@author: jeafreezy
"""

#THIS PROJECT CLASSIFIES A BREAST CANCER CONDITION TO BE EITHER BENIGN OR MALIGNANT
#THE CODES WERE WRITTEN IN JUPYTER NOTEBOOK.

#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
%matplotlib inline
#READING IN THE DATA
breastcancer=pd.read_csv('breast-cancer-wisconsin-data.csv'
#EXPLORATORY DATA ANALYSIS
breastcancer.head()
breastcancer.info()
breastcancer.describe()
a=breastcancer.corr()
a
#DATA VISIALIZATION
plt.figure(figsize = (20,10))
sns.heatmap(a)
fig=plt.figure()
sns.barplot(x='diagnosis',y='concave points_worst',data=breastcancer)
plt.title('concave_point_worst VS diagnosis')
sns.lmplot(x='perimeter_worst',y='concave points_worst',data=breastcancer,col='diagnosis')
sns.pairplot(data=breastcancer,hue='diagnosis')
#FEATURE ENGINNERING
breastcancer.drop('id',axis=1,inplace=True)
breastcancer['diagnosis']=breastcancer['diagnosis'].astype('category')
breastcancer['diagnosis']=breastcancer['diagnosis'].cat.codes
breastcancer.head()
#SPLITTING DATASET INTO DEPENDENT AND INDEPENDENT VARIABLES
from sklearn.model_selection import train_test_split
X=breastcancer[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']]
y=breastcancer[['diagnosis']]
#TRAINING THE MODEL
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
#CALLING THE LOGISTIC REGRESSON CLASS
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
#MAKING PREDICTIONS
predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print (classification_report(y_test,predictions))
from sklearn.metrics import confusion_matrix
#ACCURACY ASSESSMENT
confusion_matrix(y_test, predictions)
from sklearn.metrics import accuracy_score
(accuracy_score(y_test, predictions)) * 100