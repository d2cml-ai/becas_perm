import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

master = pd.read_csv("analysis/input/master.csv")

sns.histplot(data = master, x = "PUNTAJE FINAL", hue = "SELECCIONADO")
