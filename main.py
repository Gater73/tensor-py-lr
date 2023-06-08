import tensorflow, keras
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

#Reads dataset
data = pd.read_csv("student-mat.csv", sep=";")

#Isolates only the columns we want to work with
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

#Selects what column the AI should predict
predict = "G1"

#Drops the column we want to predict
x = np.array(data.drop([predict], 1))
#Selects only the column we want to predict
y = np.array(data[predict])

#Separates data into train data and test data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

#Selects the model for Linear Regression
linear = linear_model.LinearRegression()

#Trains the model
linear.fit(x_train, y_train)
#Calculates accuracy based on the training and the test data
acc = linear.score(x_test, y_test)

#Colects user input so we can predict just one row
gee2 = int(input("Enter the students G2: "))
gee3 = int(input("Enter the students G3: "))
studyTime = int(input("Enter the students studytime: "))
failures = int(input("Enter the students failures: "))
absences = int(input("Enter the students absences: "))

print("Information used to predict stops here")

actual_grade = int(input("Enter the students actual G1 number: "))

#Creates a array with the data the user providade minus G1
data_to_test = [[gee2, gee3,  studyTime,  failures,  absences]]
#Predicts G1
predict_one = linear.predict(data_to_test)

#Print results to the screen
print(f"With a accuracy of {acc * 100:.2f}% the AI predicted a value of {predict_one} for G1 using [G2={data_to_test[0][0]}, G3={data_to_test[0][1]}, studytime={data_to_test[0][2]}, failures={data_to_test[0][3]}, absences={data_to_test[0][4]}] and the actual G1 number was {actual_grade}.")
