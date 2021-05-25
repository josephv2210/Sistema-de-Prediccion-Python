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

x_train = dataset.iloc[:100, 4:5].values 
y_train = dataset.iloc[:100, 5].values 
x_test = dataset.iloc[110:210, 4:5].values 
y_test = dataset.iloc[110:210, 5].values# 

x_train = x_train.astype(int)
y_train = y_train.astype(int)
x_test = x_test.astype(int)
y_test = y_test.astype(int)

# Naive Bayes

#Aquí tenemos un  GaussianNB() método que realiza exactamente las mismas funciones que el código explicado anteriormente
model = GaussianNB()
model.fit(x_train, y_train)

#Haciendo predicciones
expected = y_test
y_predic_Naive = model.predict(x_test)

# Nearest Neighbor
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)
y_predic_Neighbor = neigh.predict(x_test)

# Random Forest Classification

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train, y_train)
y_predic_Forest = clf.predict(x_test)

# Regresion Lineal

pr = linear_model.LinearRegression()
pr.fit(x_train, y_train) #entrena el modelo
Y_pred = pr.predict(x_test)

# SVM

clasificador_lineal = svm.SVC(kernel='linear')
clasificador_lineal.fit(x_train, y_train)

#x_test = np.array([numero a evaluar])
y_predic_SVM = clasificador_lineal.predict(x_test)

plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, clasificador_lineal.predict(x_train), color='blue')
plt.title("Support Vector Machines")
plt.xlabel("Valor inicial")
plt.ylabel("Valor final")
plt.show()

print(f"precision de Naive Bayes:\n {round(model.score(np.array(y_test).reshape(-1,1), np.array(y_predic_Naive).reshape(-1,1)) * 100, 2)}")
print(f"precision de Nearest Neighbor:\n {round(neigh.score(np.array(y_test).reshape(-1,1), np.array(y_predic_Neighbor).reshape(-1,1)) * 100, 2)}")
print(f"precision de arbol de decision:\n {round(clf.score(np.array(y_test).reshape(-1,1), np.array(y_predic_Forest).reshape(-1,1)) * 100, 2)}")
print(f"Precision de regresion polinomial:\n {round(pr.score(x_train, y_train)*100,2)}") 
print(f"precision de Support Vector Machines:\n {round(clasificador_lineal.score(np.array(y_test).reshape(-1,1), np.array(y_predic_SVM).reshape(-1,1)) * 100, 2)}")




