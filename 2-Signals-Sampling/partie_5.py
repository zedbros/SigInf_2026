import numpy as np
import matplotlib.pyplot as plt
import math

sampling_rate = 0.00001
time = np.arange(0, 1, sampling_rate)
print(time)

frequency = 12
nu = 2.0*(math.pi)*frequency
y = []
for i in time:
    y.append(math.sin(nu*i))

plt.plot(time, y, label="12Hz sine waves")

# THE EXERCICSE
# The sampling rate should be equal to 15Hz so fs = 15*sampling_rate/frequency
fs = 15*sampling_rate/frequency
new_nu = 2.0*(math.pi)*15
new_y = []
for index, value in enumerate(time):
    new_y.append(math.sin(new_nu*value))

plt.plot(time, new_y, label="15Hz alias")

plt.show()
