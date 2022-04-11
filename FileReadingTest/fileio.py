readPath = "C:\\Users\\p_tri\\Desktop\\Python\\FileReadingTest\\Latin-Lipsum.txt"
# read a file
# 'r' opens file in read-only option
with open(readPath, 'r') as rfile:
    text = rfile.read()

text = text.split(" ")

writePath = "C:\\Users\\p_tri\\Desktop\\Python\\FileReadingTest\\Write-Output-Test.txt"
# write to a file
# 'w' open file in write-only option
# write-only option will overwrite the file (if the file exists)
# if the file doesn't exist, a new file is created at "writePath"
with open(writePath, 'w') as wfile:
    for word in text:
        if(len(word) == 5 and word[-1] != ','):
            wfile.write(word + "\n")

# append to a file
# 'a' opens file in append option
# the file pointer is at the end of the file (if the file exists)
# if the file doesn't exist, a new file is created at "writePath"
with open(writePath, 'a') as afile:
    for x in range(100):
        afile.write(str(x + 1) + "\n")

# print(text)