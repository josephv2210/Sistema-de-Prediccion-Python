# Librerias comunes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split

# Librerias de los distintos algoritmos
from sklearn.model_selection import train_test_split
from sklearn import svm

# Importamos el dataset con los datos arreglados,

dataset = pd.read_csv("Data.csv")
 
# Variables vacias en donde se van a almaccenar los datos
is_T = []
dataS = []
X_T = []
Y_T = []

# Se dividen los datos por enfermedad y se guardan los datos respectivos
for i in range(63):
    is_T.append(dataset.loc[:, 'Causa de Muerte'] == i)
    dataS.append(dataset.loc[is_T[i]])
    neoData = dataS[i]
    X_T.append(neoData.iloc[:, 3:4].values)
    Y_T.append(neoData.iloc[:, 5].values)

# -----------------------------------------------Algoritmo SVM-------------------------------------------------------
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

# ----------------------- Generar la prediccion para una enfermedad correspondiente -------------------------------
# prin=26
# Pred(X_T[prin], Y_T[prin], prin)

# -------------------------- Generar la prediccion para todas las enfermedades ------------------------------------
for i in range(63):
    Pred(X_T[i], Y_T[i], i)




