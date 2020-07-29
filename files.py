# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    num = float(line[-6:])
    counter += 1
    print(num)
    print(counter)
print('Average spam confidence:',num/counter)
