import pandas as pd
import matplotlib.pyplot as plt

# Læs CSV
df = pd.read_csv("Normal_kørsel0005.csv", header=None, names=["x", "y", "z"])

# Se de første rækker
print(df.head())

# Statistik
print(df.describe())

plt.figure(figsize=(10,5))
plt.plot(df["x"], label="X")
plt.plot(df["y"], label="Y")
plt.plot(df["z"], label="Z")
plt.xlabel("Måling")
plt.ylabel("Accelerometer (g eller LSB)")
plt.title("Accelerometerdata")
plt.legend()
plt.show()