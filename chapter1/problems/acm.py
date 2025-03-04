import sys
correct = set()
probs = {}
lines = sys.stdin.read().splitlines()
lines = lines[:len(lines)-1]
for line in lines:
    time, name, status = line.split()
    if status == 'right':
        probs[name] = probs.get(name,0) + int(time)
        correct.add(name)
    if status == 'wrong':
        probs[name] = probs.get(name,0) + 20
t = 0
for p in probs:
    if p in correct:
        t += probs[p]
print(len(correct),t)