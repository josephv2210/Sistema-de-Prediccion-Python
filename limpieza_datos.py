#importamos las librerias necesarias
import pandas as pd

data = pd.read_csv("DataSet_Prediccion.csv")

# Borrado de registros inecesarias
# print(data.isnull().sum()) Comprobar datos nulos

# Borrado de las columnas inecesarias
# year
# area
# record type
# reliability
# source year
# value footnotes
data.drop(["Year", "Area","Record Type","Reliability","Source Year","Value Footnotes"], axis=1, inplace=True)

# borramos todos los registros nulos y las filas de la columna total
# All other diseases, All other external causes, All causes, Unknown
def EliminarFila(fila, columna, data):
    mantener = data.loc[:, columna] != fila
    return data.loc[mantener]


data = EliminarFila("Total", "Age", data)
data = EliminarFila("Unknown", "Age", data)
data = EliminarFila("All other diseases", "Cause of death (WHO)", data)
data = EliminarFila("All other external causes", "Cause of death (WHO)", data)
data = EliminarFila("All causes", "Cause of death (WHO)", data)
data = EliminarFila("Unknown", "Sex", data)

# Cambiar las cabeceras por su traduccion al español

cabecera = ["Pais", "Sexo", "Edad", "Causa de Muerte", "Cantidad"]
data.columns = cabecera

# convercion de datos de string a int

# le pasamos a la funcion una lista de strings los cuales uno a uno los va remplazando
def ConversionCategorizacion(Nombre, Columna, data):
    for i in range (len(Nombre)):
        data[Columna] = data[Columna].replace({Nombre[i]:i})
    return data

# Pais Argentina 0, Chile 1, Brazil 2, Mexico 3, Panama 4
data = ConversionCategorizacion(["Argentina", "Chile", "Brazil", "Mexico", "Panama"], "Pais", data)

# Sexo male 0, female 1
data = ConversionCategorizacion(["Male", "Female"], "Sexo", data)

# Causa de muerte
""" 
0 Certain infectious and parasitic diseases
1 Intestinal infectious diseases
2 Tuberculosis
3 Tetanus
4 Diphtheria
5 Whooping cough
6 Meningococcal infection
7 Septicaemia
8 Acute poliomyelitis
9 Measles
10 Viral hepatitis
11 Human immunodeficiency virus [HIV] disease
12 Malaria
13 Neoplasms
14 Malignant neoplasms
15 Malignant neoplasm of lip, oral cavity and pharynx
16 Malignant neoplasm of oesophagus
17 Malignant neoplasm of stomach
18 Malignant neoplasm of colon
19 Malignant neoplasm of liver and intrahepatic bile ducts
20 Malignant neoplasm of pancreas
21 Malignant neoplasm of trachea
22 Malignant neoplasm of prostate
23 Malignant neoplasm of lymphoid, haematopoietic and related tissue
24 Disorders of the blood and blood-forming organs and certain disorders involving the immune mec 
25 Anaemias
26 Endocrine
27 Diabetes mellitus
28 Malnutrition
29 Mental and behavioural disorders
30 Diseases of the nervous system
31 Diseases of the circulatory system
32 Acute rheumatic fever and chronic rheumatic heart diseases
33 Hypertensive diseases
34 Ischaemic heart diseases
35 Cerebrovascular diseases
36 Diseases of arteries, arterioles and capillaries
37 Diseases of the respiratory  system
38 Influenza
39 Pneumonia
40 Chronic lower respiratory diseases
41 Diseases of the digestive system
42 Gastric and duodenal ulcer
43 Diseases of the liver
44 Diseases of the musculoskeletal system and connective tissue
45 Diseases of the genitourinary system
46 Disorders of kidney and ureter
47 Hyperplasia of prostate
48 Certain conditions originating in the perinatal period
49 Congenital malformations, deformations and chromosomal abnormalities
50 Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified
51 External causes
52 Accidents
53 Transport accidents
54 Falls
55 Accidental drowning and submersion
56 Exposure to smoke, fire and flames
57 Accidental poisoning by and exposure to noxious substances
58 Intentional self-harm
59 Assault
 """

# Generar rangos de edad
# 0 0-9,1 10-19,2 20-29, 3 30-39,4 40-49,5 50-59,6 60-69, 7 70-79, 8 80-89, 9 90-mas

