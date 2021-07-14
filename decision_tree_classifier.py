from sklearn import tree
import numpy as np
from sklearn.datasets import load_iris

# Prints we will the name of iris species from a predicted number
def decode(num):
	for j in num:
		if j==0:
			print("setosa")
		elif j==1:
			print("versicolor")
		else:
			print("virginica")

test_ids = []
iris = load_iris()


for k in range (0, 20):
	test_ids.append(k)
for k in range (50, 70):
	test_ids.append(k)
for k in range (100, 120):
	test_ids.append(k)

# Data for training our model
train_target = np.delete(iris.target, test_ids)
train_data = np.delete(iris.data, test_ids, axis=0)

classify = tree.DecisionTreeClassifier()

clf.fit(train_data, train_target)

data1 = float(input("Enter lenght of sepal : "))
data2 = float(input("Enter width of sepal : "))
data3 = float(input("Enter length of petal : "))
data4 = float(input("Enter width of petal : "))

data = [data1, data2, data3, data4]

decode(clf.predict(data))
