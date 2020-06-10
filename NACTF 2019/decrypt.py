import csv
s = input()
f = open('substitution.csv', 'rt')
reader = csv.reader(f, delimiter=',')
print('here')
a=[]
for i in reader:
    a.append(i)
print(a)
for i in range(len(s)):
    s = s[:i]+a[0][a[1].index(s[i])]+s[i+1:]
print(s)
