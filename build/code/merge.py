import pandas as pd
import statsmodels as sm
from patsy import dmatrices

mat_20 = pd.read_stata("https://www.dropbox.com/s/cuylv1y9ler8wv2/Matriculados%2026dic%202018-2021.dta?dl=1").query("año == 2020")

an_2020 = pd.read_excel("https://www.dropbox.com/scl/fi/9fvhd0t3001p15o48d28o/ANEXO2020.xlsx?dl=1&rlkey=h8z8awln9ryycwi72o655bx55")
an_2020["N° DE DNI"] = an_2020["N° DE DNI"].apply(str).str.replace("\\n", "")
an_2020 = an_2020.rename(columns = {"N° DE DNI": "numero_documento"})

master = an_2020.merge(mat_20, how = "left", on = "numero_documento", indicator = True)
master.drop(columns = ["UNNAMED:0", "Unnamed: 11", "Unnamed: 10"], inplace = True)
master["IES"] = master["IES"].str.replace("\n", "")
master["IES"] = master["IES"].str.replace("NABEC", "")

master.to_csv("build/output/master.csv", index = False)