d = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
s = input()
for i in range(len(s)):
    d[s[i]] += 1
for val in d.values():
    print(val, end=' ')
