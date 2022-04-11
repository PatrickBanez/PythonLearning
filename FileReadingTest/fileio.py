filePath = "C:\\Users\\p_tri\\Desktop\\Python\\FileReadingTest\\Latin-Lipsum.txt"

with open(filePath, 'r') as file:
    text = file.read()

text = text.split(" ")
for word in text:
    if(len(word) == 5 and word[-1] != ","):
        print(word)

# print(text)