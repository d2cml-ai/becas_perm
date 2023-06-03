import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
from statsmodels.discrete.discrete_model import Probit

master = pd.read_csv("analysis/input/master.csv")
master["conti"] = master._merge.map({"both": 1, "left_only": 0})
# master = pd.get_dummies(master, columns = ["CONDICIÓN"], prefix = "", prefix_sep = "")
# master = master[master["REGIÓN DE ESTUDIO"] == "LIMA\nMETROPOLITANA"]
master = master[master["PUNTAJE FINAL"] == 60]
data = master[["conti", "SELECCIONADO", "IES"]]
data.loc[:, "SELECCIONADO"] = data.SELECCIONADO.apply(int)

y, X = dmatrices("conti ~ SELECCIONADO + IES", data, return_type = "dataframe")

# res_l = sm.GLM(y, X, family = sm.families.Binomial()).fit(cov_type = "cluster", cov_kwds = {"groups": data.IES})
# res_p = sm.GLM(y, X, family = sm.families.Binomial(link = sm.genmod.families.links.probit())).fit(cov_type = "cluster", cov_kwds = {"groups": data.IES})
res_o = sm.OLS(y, X).fit(cov_type = "cluster", cov_kwds = {"groups": data.IES})

# print(res_l.summary())
# print(res_p.summary())
print(res_o.summary())

