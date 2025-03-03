from itertools import permutations
a = [chr(i) for i in range(ord('A'),ord('J')+1)]
print(*permutations(a), sep = '\n')