readPath = "C:\\Users\\p_tri\\Desktop\\Python\\FileReadingTest\\Latin-Lipsum.txt"
# read a file
with open(readPath, 'r') as rfile:
    text = rfile.read()

text = text.split(" ")

writePath = "C:\\Users\\p_tri\\Desktop\\Python\\FileReadingTest\\Write-Output-Test.txt"
# write to a file
with open(writePath, 'w') as wfile:
    for word in text:
        if(len(word) == 5 and word[-1] != ','):
            wfile.write(word + "\n")

# append to a file
with open(writePath, 'a') as afile:
    for x in range(100):
        afile.write(str(x + 1) + "\n")

# print(text)