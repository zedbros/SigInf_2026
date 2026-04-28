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
# plt.show()

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





# PARTIE 3
f = open("8-Code-Prefix/lorem_ipsum.txt")
# print(f.read())

code = {}
alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))
for index, value in enumerate(alphabet):
    code[value] = index
coded_text = ""
temp = ""
for i in f:
    i = i.lower()
    if i not in alphabet:
        if temp == "":
            coded_text += i
        else:
            coded_text += code[temp]
            coded_text += i
        continue

    if temp == "":
        temp += i
    else:
        t = temp + i
        if t in code:
            temp += i            
        else:
            code[t] = code[temp] + i
            coded_text += code[t]

print('-' * 20)
# print(coded_text)

# with open("8-Code-Prefix/coded_lorem_ipsum.txt", "w", encoding="utf-8") as w:
#     for i in coded_text:
#         w.write(i)
