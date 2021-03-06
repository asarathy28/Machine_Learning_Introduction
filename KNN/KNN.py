import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
"""
KNN --> K nearest neighbor
"""

data = pd.read_csv("car.data")
print(data.head())

# transforms columns of data into lists
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

# zips "input" lists
X = list(zip(buying, maint, door, persons, lug_boot, safety))
Y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

# sets model to KNN
model = KNeighborsClassifier(n_neighbors=7)

# trains model
model.fit(x_train, y_train)
# tests model
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for i in range(len(x_test)):
    print("Data: ", x_test[i], " Actual: ", names[y_test[i]], " Predicted: ", names[predicted[i]])
    n = model.kneighbors([x_test[i]], 7, True)
    print(n)





