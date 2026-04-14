import math

# 1.1
# a)
# H(X) = -sum[i=1 -> n]1/8*log_2(1/8)
n = 8
def entropy(n):
    res = 0
    for _ in range(0,n+1):
        res += 1/n*math.log2(1/n)
    return -res
print("\nNORMAL ENTROPY")
print(entropy(n))
# => 3.375

# b)
# The numbers left are 5,6,7 and 8, which means we have a probability of
# 1/4.
n = 4
print(entropy(n))
# => 2.75

# c)
# 1,2,3,4,5 and 6
n = 6
print(entropy(n))
# => 3.0158

# d)
# In order to guarantee to find the right number, we always need to pose
# n/2 questions if n%2==0
# ceil(n/2)+1 questions if n%2!=0

# This means that the lower the entropy, the closer we are to our correct
# result.
# When the probability is 1 aka 100%, entropy is equal to 0.



# 1.2
# a)
print("\nSTRANGE ENTROPY")
def strange_entropy(n):
    res = 0
    def op(p):
        return p*math.log2(p)
    for i in range(0,n+1):
        match i:
            case 1: res += op(1/2)
            case 2: res += op(1/4)
            case 3|4|5|6|7|8: res += op(1/8)
    return -res
print(strange_entropy(8))
print(strange_entropy(4))
print(strange_entropy(6))
# It is lower than the normal entropy, 



# 1.3






# 2.1
# It's the binomial with repetition, so (n k) == "k parmis n" which is equal to:
# fact(n) / fact(k)*fact(n-k)).


# 2.2 and 2.3 and 2.4
print("\nSIMPLE MASTERMIND")
def simple_mastermind(secret, guess):
    black = 0
    white = 0

    l = guess[0]
    r = guess[1]

    if guess == secret: black += 2
    elif l in secret:
        if(l == secret[0]): black += 1
        else: white += 1
    elif r in secret:
        if(r == secret[1]): black += 1
        else: white += 1
    else:
        pass
    return black, white


# If we receive the values 
# b = 2 and w = 0 => entropy = 0                    (found it)
# b = 1 and w = 0 => entropy = 1/n*log_2(1/n)       (reduced to one to find out of n)
# b = 0 and w = 1 => entropy = 1/n*log_2(1/n)
# b = 0 and w = 0 => entropy = -2*(1/n*log_2(1/n))
def simple_mastermind_entropy(b,w,n):
    if(b == 2):
        return 0
    elif(b == 1) or (b==0 and w==1):
        return -1/n*math.log2(1/n)
    else:
        res = 0
        for i in range(0,n+1):
            res += 1/n*math.log2(1/n)
        return -res
    
def compute_entropy(secrets, guess):
    print(f"\nGuess {guess}")
    res = []
    sum_entropy = 0
    for i in secrets:
        black, white = simple_mastermind(i, guess)
        ent = simple_mastermind_entropy(black, white, len(secrets[0]))
        sum_entropy += ent
        res.append([i, black, white, ent])
        print(i, black, white, "H(X) = ", ent)
    return res, sum_entropy

secrets = ["AA", "AB", "AC", "BA", "BB", "BC", "CA", "CB", "CC"]
print(compute_entropy(secrets, "AA")[1])
print(compute_entropy(secrets, "AB")[1])


# 2.5
# If we simply add all the entropy scores of all the possible secrets, we get that the
# "AB" guess is better.


# 2.6
# So we go with the guess AB.
print("\n///////////////// \n")
print(simple_mastermind("AC", "AB"))
new_secrets = []
for i in secrets:
    if("A" in i or "B" in i):
        new_secrets.append(i)
print(new_secrets)

# Decided to skip the rest because going to implement it anyways later.

# 2.7 "... BB instead of AC ..."


# Part 3
# Milestone 1: Represent the game
import itertools
COLORS = [1, 2, 3, 4, 5, 6]
CODE_LENGTH = 4
def all_codes():
    """Return the list of all possible codes."""
    return list(itertools.product(COLORS, repeat=CODE_LENGTH))
codes = all_codes()
def get_response(secret, guess):
    """
    Compute the Mastermind response.
    Returns (black_pegs, white_pegs).
    """
    if guess == secret: return len(guess), 0
    black = 0
    white = 0
    already_black = []
    for index, value in enumerate(guess):
        if(value == secret[index]):
            black += 1
            already_black.append(index)
    already_white = []
    for index, value in enumerate(guess):
        if index in already_black:
            continue
        if value in secret:
            white += 1

    return black, white

s = [(1,2,3,4), (1,2,3,4), (1,2,3,4), (1,1,1,1), (1,2,1,2), (1,1,2,3,4)]
g = [(1,2,3,4), (4,3,2,1), (1,3,2,4), (1,2,3,4), (2,1,2,1), (2,1,4,1,1)]
for i in range(len(s)):
    print(s[i], g[i], get_response(s[i], g[i]))