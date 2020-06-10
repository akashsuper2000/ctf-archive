a = [int(i) for i in input().split()]
c = ''
for i in range(len(a)):
    s = input()
    c+=s[a[i]-1]
print(c)
