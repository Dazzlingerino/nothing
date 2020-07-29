name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
dic = dict()

for line in handle:
    if line.startswith("From "):
        lst = line.split()
        lst = lst[5].split(":")
        dic[lst[0]] = dic.get(lst[0], 0) +1
        n = sorted([(v,k) for v,k in dic.items()])
for i in n:
    print(i[0],i[1])
#better code
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
dic = dict()

for line in handle:
    if line.startswith("From "):
        lst = line.split()
        lst = lst[5].split(":")
        dic[lst[0]] = dic.get(lst[0], 0) +1
n = sorted([(v,k) for v,k in dic.items()])
for a,b in n:
    print(a,b)
