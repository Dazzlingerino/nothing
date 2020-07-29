largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #print(num)

    try:
        value = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None and smallest is None:
        largest = smallest = value
        continue
    if value > largest:
            largest = value
    elif value < smallest:
            smallest = value




print("Maximum is ", largest)
print("Minimum is ", smallest)
