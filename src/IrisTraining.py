import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('iris.csv', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

X=df.drop(["class"], axis=1)
y=df["class"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

rf = RandomForestClassifier()

rf.fit(X_train,y_train)


import pickle
pickle_out = open("randomforest.pkl","wb")
pickle.dump(rf, pickle_out)
pickle_out.close()