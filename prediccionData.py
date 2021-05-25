# Librerias comunes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame

# Librerias de los distintos algoritmos
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Importamos el dataset con los datos arreglados,

dataset = pd.read_csv("Sistema de Prediccion/Data.csv")

x_train = dataset.iloc[:, 4:5].values 
y_train = dataset.iloc[:, 5].values 
# x_test = dataset.iloc[110:210, 4:5].values 
# y_test = dataset.iloc[110:210, 5].values# 

x_train = x_train.astype(int)
y_train = y_train.astype(int)
# x_test = x_test.astype(int)
# y_test = y_test.astype(int)

# SVM

clasificador_lineal = svm.SVC(kernel='linear')
clasificador_lineal.fit(x_train, y_train)

plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, clasificador_lineal.predict(x_train), color='blue')
plt.title("Support Vector Machines")
plt.xlabel("Valor inicial")
plt.ylabel("Valor final")
plt.show()

# print(f"precision de Support Vector Machines:\n {round(clasificador_lineal.score(np.array(y_test).reshape(-1,1), np.array(y_predic_SVM).reshape(-1,1)) * 100, 2)}")
print(clasificador_lineal.predict(y_train))



