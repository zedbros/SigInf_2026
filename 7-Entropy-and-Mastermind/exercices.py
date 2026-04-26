import math
from collections import defaultdict

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
    already_scanned = []
    for index, value in enumerate(guess):
        if(value == secret[index]):
            black += 1
            already_black.append(index)
            already_scanned.append(value)
    for index, value in enumerate(guess):
        if index in already_black:
            continue
        if value in secret and already_scanned.count(value) < secret.count(value):
            white += 1
            already_scanned.append(value)

    return black, white

s = [(1,2,3,4), (1,2,3,4), (1,2,3,4), (1,1,1,1), (1,2,1,2), (1,1,2,3,4)]
g = [(1,2,3,4), (4,3,2,1), (1,3,2,4), (1,2,3,4), (2,1,2,1), (2,1,4,1,1)]
for i in range(len(s)):
    print(s[i], g[i], get_response(s[i], g[i]))



# Milestone 2
def partition(candidates, guess):
    """
    Partition candidates by the response each would give to guess.
    Returns a dict mapping response -> list of candidates.
    """
    groups = defaultdict(list)
    for c in candidates:
        groups[get_response(c, guess)].append(c)
    return dict(groups)
codes = all_codes()
test_partition = partition(codes, (1, 1, 2, 2))

total = sum(len(g) for g in test_partition.values())
print(f"\n{'Response':<12} {'Count':>6}")
print("-" * 19)
for response, group in sorted(test_partition.items()):
    print(f"{str(response):<12} {len(group):>6}")
print(f"Number of distinct responses: {len(test_partition)}")
print(f"Total candidates across all groups: {total}  (expected 1296)\n")


# Milestone 3
def expected_entropy(candidates, guess):
    """
    Compute the expected entropy of the candidate set after making guess.
    """
    partitions = partition(candidates, guess)
    total = len(candidates)
    h = 0
    for group in partitions.values():
        p = len(group)/total
        if p > 0:
            h -= p*math.log2(p)
    # This is (-sum(p*log_2(p))), the entropy.
    # But we want expected *remaining* entropy, not the entropy of the response distribution.

    # Going to do this instead in the best_guess section versus here.
    return h

def best_guess(candidates, all_codes_list):
    """
    Return the guess (from all_codes_list) that minimizes expected remaining entropy.
    """
    best_guess = None
    best_h = -1
    for guess in all_codes_list:
        h = expected_entropy(candidates, guess)
        if best_h < h:
            best_guess = guess
            best_h = h
    return best_guess

def solve():
    candidates = all_codes()
    codes = all_codes()
    turn = 1

    print(f"I will try to guess your secret code ({CODE_LENGTH} pegs, colors {COLORS}).")
    print("After each guess, enter the response as: black white (e.g. '2 1')\n")

    while True:
        if len(candidates) == 1:
            print(f"Turn {turn}: The secret must be {candidates[0]}!")
            break

        guess = best_guess(candidates, codes)
        print(f"Turn {turn}: I guess {guess}")

        response_str = input("Your response (black white): ")
        black, white = map(int, response_str.split())
        if black == CODE_LENGTH:
            print(f"Solved in {turn} turn(s)!")
            break
        # Filter candidates to those consistent with the response
        candidates = [c for c in candidates if get_response(c, guess) == (black, white)]
        print(f" {len(candidates)} candidate(s) remaining.\n")
        turn += 1

solve()
