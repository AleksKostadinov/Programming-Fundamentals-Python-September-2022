text = input()
mylist = []

for i in range(len(text)):
    if text[i].isupper():
        mylist.append(i)
print(mylist)