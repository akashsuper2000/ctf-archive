open("output2.txt", "wb").write(open("output.txt", "rb").read()[::-1])
