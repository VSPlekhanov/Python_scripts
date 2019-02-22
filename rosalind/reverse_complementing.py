d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
s = input()
for i in range(len(s) - 1, -1, -1):
    print(d[s[i]], end='')
