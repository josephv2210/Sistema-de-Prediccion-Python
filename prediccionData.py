# Librerias comunes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split

# Librerias de los distintos algoritmos
from sklearn import svm

# Importamos el dataset con los datos arreglados,

dataset = pd.read_csv("Data.csv")

x = dataset.iloc[5500:6099, 4:5].values 
y = dataset.iloc[5500:6099, 5].values 

# is_0 = dataset.loc[:, 'Causa de Muerte'] == 0
# for i in range(is_0):
#     if 
# x = dataset.loc[:, is_0]
# y = dataset.iloc[:, 5].values 

# print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


x_train = x_train.astype(int)
y_train = y_train.astype(int)

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
y_predic = clasificador_lineal.predict(x_train)
print(y_predic[:100])



