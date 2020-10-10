maxRange = 5
string = ""
character = "*"

for i in range(maxRange*2):
    if i < maxRange:
        string += character
    else:
        string = string[:len(string)-1]
    print(string)
