fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = line.rstrip()
    x = line.split()
    for word in x:
        if word in lst: continue
        lst.append(word)
    lst.sort()
print(lst)

# better variant
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.rstrip().split():
        if word in lst: continue
        lst.append(word)
    lst.sort()
print(lst)
