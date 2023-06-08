import tensorflow, keras
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G1"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)

gee2 = int(input("Enter the students G2: "))
gee3 = int(input("Enter the students G3: "))
studyTime = int(input("Enter the students studytime: "))
failures = int(input("Enter the students failures: "))
absences = int(input("Enter the students absences: "))

print("Information used to predict stops here")

actual_grade = int(input("Enter the students actual G1 number: "))

data_to_test = [[gee2, gee3,  studyTime,  failures,  absences]]
predict_one = linear.predict(data_to_test)


print(f"With a accuracy of {acc * 100:.2f}% the AI predicted a value of {predict_one} for G1 using [G2={data_to_test[0][0]}, G3={data_to_test[0][1]}, studytime={data_to_test[0][2]}, failures={data_to_test[0][3]}, absences={data_to_test[0][4]}] and the actual G1 number was {actual_grade}.")