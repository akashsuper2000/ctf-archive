# p = [redacted]
# q = [redacted]
e = 65537
# flag = "[redacted]"

def encrypt(n, e, plaintext):
  encrypted = []
  for char in plaintext:
    cipher = (ord(char) ** int(e)) % int(n)
    encrypted.append(cipher)
  return(encrypted)

n = 54749648884874001108038301329774150258791219273879249601123423751292261798269586163458351220727718910448330440812899799
ct = encrypt(n, e, flag)
print(ct)
