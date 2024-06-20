import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("temp.txt")
time = data[:, 0]
temperature = data[:, 1] * 119.7

plt.figure(figsize=(10, 6))
plt.plot(time, temperature)
plt.xlabel(r'Time, $10^{-12}$ s')
plt.ylabel(r'Temperature, K')
plt.savefig("temperature.png")


