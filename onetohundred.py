# loop from 1 till 100 prints multiples 3, 5, and 3*5 with text
for i in range(1, 101):
    if i % 15 == 0:
        print("ThreeFive")
    elif i % 5 == 0:
        print("Five")
    elif i % 3 == 0:
        print("Three")
    else:
        print(i)
