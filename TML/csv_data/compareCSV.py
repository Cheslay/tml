import pandas as pd
import matplotlib.pyplot as plt

# Indlæs dine to CSV-filer
# Erstat 'fil1.csv' og 'fil2.csv' med dine faktiske filnavne
df1 = pd.read_csv('Normal_kørsel0000.csv')
df2 = pd.read_csv('Udryknings_kørsel0000.csv')

# Opret to subplot ved siden af hinanden med fælles Y-akse
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Plot accX, accY, accZ for fil 1
axes[0].plot(df1['timestamp'], df1['accX'], label='accX')
axes[0].plot(df1['timestamp'], df1['accY'], label='accY')
axes[0].plot(df1['timestamp'], df1['accZ'], label='accZ')
axes[0].set_title('Fil 1')
axes[0].set_xlabel('Timestamp')
axes[0].set_ylabel('Acceleration')
axes[0].legend()

# Plot accX, accY, accZ for fil 2
axes[1].plot(df2['timestamp'], df2['accX'], label='accX')
axes[1].plot(df2['timestamp'], df2['accY'], label='accY')
axes[1].plot(df2['timestamp'], df2['accZ'], label='accZ')
axes[1].set_title('Fil 2')
axes[1].set_xlabel('Timestamp')
axes[1].legend()

plt.tight_layout()
plt.show()
