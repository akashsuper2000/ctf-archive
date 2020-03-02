import os
import re
f1 = open('answer.txt','w')
files = os.listdir('./bottles')
c = ''
for i in files:
    f2 = open('./bottles/'+i,'rb')
    s = str(f2.read())
    c+=s
    f2.close()
print(c.index('ritsec'))
