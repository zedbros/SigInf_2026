import matplotlib.pyplot as plt
import math


# PARTIE 0
a = ['A', 'D', 'E', 'I', 'M', 'N', 'P', 'R', 'U', 'Y']
p = [7.11, 3.67, 12.1, 6.59, 2.62, 6.39, 2.49, 6.07, 4.49, 0.46]
A = {}
for i in range(len(a)):
    A[a[i]] = p[i]
s = sum(p)
plt.bar([i for i in A.keys()], [i/s for i in A.values()])
plt.show()

normalised_p = [round(i/s, 2) for i in p]

entropie = 0
for i in normalised_p:
    entropie -= i*math.log2(i)
print(entropie)


for i in range(len(a)):
    print(a[i], normalised_p[i])


# PARTIE 2

codes = ["000", "001", "010", "100", "011", "1010", "1011", "110", "1110", "1111"]

E_l_C_x = 0
for i in range(len(a)):
    E_l_C_x += len(codes[i])*normalised_p[i]
print(E_l_C_x)
