import math
import random

def P(i, nbr_of_repititions):
    return (1/2*math.pow(nbr_of_repititions, 2))*(math.factorial(nbr_of_repititions)/math.factorial(i))
    

def H(nbr_of_repetitions):
    res = 0
    for i in range(nbr_of_repetitions):
        p_i = P(i, nbr_of_repititions=nbr_of_repetitions)
        res += p_i*math.log2(p_i)
    return -res

res = 0
for _ in range(100):
    res += H(10)

print(res/100)
