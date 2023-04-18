import requests

url = 'https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/stream?q=select%20url%20from%20flags_108'
results = []

for i in range(100):
    response = requests.get(url)
    results.append(response.text[1])

print(results)
print(set(results))
print(''.join(results))
