# Librerias comunes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split

# Librerias de los distintos algoritmos
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Importamos el dataset con los datos arreglados,

dataset = pd.read_csv("Data.csv")
 

is_T = []
dataS = []
X_T = []
Y_T = []


for i in range(63):
    is_T.append(dataset.loc[:, 'Causa de Muerte'] == i)
    dataS.append(dataset.loc[is_T[i]])
    neoData = dataS[i]
    X_T.append(neoData.iloc[:, 3:4].values)
    Y_T.append(neoData.iloc[:, 5].values)

# -------------------------------------------------------------------------------------------------------------------

def Pred(x, y, enfermedad):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    x_train = x_train.astype(int)
    y_train = y_train.astype(int)

    # SVM

    clasificador_lineal = svm.SVC(kernel='linear')
    clasificador_lineal.fit(x_train, y_train)

    # Graficacion
    plt.scatter(x_train, y_train, color='red')
    plt.plot(x_train, clasificador_lineal.predict(x_train), color='blue')
    plt.title(f"Support Vector Machines, Enfermedad {enfermedad}")
    plt.xlabel("Valor inicial")
    plt.ylabel("Valor final")
    plt.show()

    # Prediccion
    y_predic = clasificador_lineal.predict(x_train)
    print("Enfermedad Numero ", enfermedad, "\n", y_predic[:100])

prin=26
Pred(X_T[prin], Y_T[prin], prin)

print(X_T[prin])
print(Y_T[prin])
for i in range(63):
    Pred(X_T[i], Y_T[i], i)




