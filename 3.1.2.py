s, t = (input() for i in range(2))

count = 0

for j in range(len(s)):
    if s.find(t, j, j + len(t)) >= 0:
        count += 1
