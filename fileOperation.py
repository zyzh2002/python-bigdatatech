# open a file in binary mode and decode it later using decode()
# useless in your test
fileData = ""
with open("stu-scores.csv", "rb") as binaryFile:
    fileData = binaryFile.read()

fileData = fileData.decode()
print(fileData)
