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
Certain infectious and parasitic diseases
Intestinal infectious diseases
Tuberculosis
Tetanus
Diphtheria
Whooping cough
Meningococcal infection
Septicaemia
Acute poliomyelitis
Measles
Viral hepatitis
Human immunodeficiency virus [HIV] disease
Malaria
Neoplasms
Malignant neoplasms
Malignant neoplasm of lip, oral cavity and pharynx
Malignant neoplasm of oesophagus
Malignant neoplasm of stomach
Malignant neoplasm of colon
Malignant neoplasm of liver and intrahepatic bile ducts
Malignant neoplasm of pancreas
Malignant neoplasm of trachea
Malignant neoplasm of prostate
Malignant neoplasm of lymphoid, haematopoietic and related tissue
Disorders of the blood and blood-forming organs and certain disorders involving the immune mec 
Anaemias
Endocrine
Diabetes mellitus
Malnutrition
Mental and behavioural disorders
Diseases of the nervous system
Diseases of the circulatory system
Acute rheumatic fever and chronic rheumatic heart diseases
Hypertensive diseases
Ischaemic heart diseases
Cerebrovascular diseases
Diseases of arteries, arterioles and capillaries
Diseases of the respiratory  system
Influenza
Pneumonia
Chronic lower respiratory diseases
Diseases of the digestive system
Gastric and duodenal ulcer
Diseases of the liver
Diseases of the musculoskeletal system and connective tissue
Diseases of the genitourinary system
Disorders of kidney and ureter
Hyperplasia of prostate
Certain conditions originating in the perinatal period
Congenital malformations, deformations and chromosomal abnormalities
Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified
External causes
Accidents
Transport accidents
Falls
Accidental drowning and submersion
Exposure to smoke, fire and flames
Accidental poisoning by and exposure to noxious substances
Intentional self-harm
Assault
 """

# Generar rangos de edad
# 0 0-9,1 10-19,2 20-29, 3 30-39,4 40-49,5 50-59,6 60-69, 7 70-79, 8 80-89, 9 90-mas

