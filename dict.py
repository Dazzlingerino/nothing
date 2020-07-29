# bad code
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
l = list()
d = dict()
i = 0
for line in handle:
    if line.startswith("From "):
        l = line.split()
        d = l[1]
        i += 1
print(l[1],i - 22)
# nice code
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
l = list()
d = dict()
i = None
x = None
for line in handle:
    if line.startswith("From "):
        l = line.split()
        d[l[1]] = d.get(l[1],0) + 1
        for a,b in d.items():
            if i is None or b > x:
                i = a
                x = b
print(i,x)
