# Given a list of numbers and a number, return if any 2 numbers from list add up to k
#  list = [10, 15, 3, 7], k = 17, return True

import timeit

# Naive approach, double for loop, skipping overlap

def add_up (l, k):
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            elif l[i] + l[j] == k:
                return True
    return False

l = [10, 6, 3, 7]
k = 16
print (add_up (l, k))

# Works, but O(n^2) time, not great
# Constant space?

# Try again with 1 pass
# Add each number into another list, called "seen", check to see if (k - new value) in seen list

def add_up2 (l, k):
    seen = []
    for i in range(len(l)):
        if k - l[i] in seen:
            return True
        else:
            seen.append(l[i])
    return False

l = [10, 8, 3, 7]
k = 16
print (add_up2 (l, k))

# O(n) time now
# O(n) space now

print (timeit.repeat(lambda: add_up(l,k)))
print (timeit.repeat(lambda: add_up2(l,k)))