import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = "/Users/lwk/Downloads/hwk1_convergence.csv"

# Read tab-delimited CSV
df = pd.read_csv(path, sep="\t")

# Inspect
print(df.head())
print(df.columns)
# Drop observations with missing GDP data
df = df.dropna(subset=["gdppc1960", "gdppc2000"])

# Annualized growth rate
df["growth"] = (1/40) * np.log(df["gdppc2000"] / df["gdppc1960"])
bin_width = 0.01
bins = np.arange(df["growth"].min(), df["growth"].max() + bin_width, bin_width)

plt.figure()
plt.hist(df["growth"], bins=bins)
plt.xlabel("Annualized GDP per capita growth rate")
plt.ylabel("Number of countries")
plt.title("Histogram of GDPPC Growth Rates (1960–2000)")
plt.show()
