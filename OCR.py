import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.model_selection import train_test_split
from sklearn import datasets

dg = datasets.load_digits()
x = dg.data
y = dg.target


x_tarain, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)


model = linear_model.LogisticRegression()
model.fit(x_tarain, y_train)

out = model.predict(x_test)
out

y_test

er =  out - y_test
er
t = 0
f = 0
for i in er:
    if i == 0:
        t += 1
    else:
        f += 1

print(t, f)
pr_er = (t * 100) / 180
print('percentage erro:', pr_er)
