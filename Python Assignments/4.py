import random as r
x = r.randint(1, 100)
flag = 0
for i in range(3):
    if(i == 2):
        print("Last chance")
    else:
        print("{}st chance".format(i+1))
    num = int(input("Guess the number between 1 to 100: "))
    if(num == x):
        print("Your Guess is correct!!")
        flag = 1
        break
    elif(num < x):
        print("Your number is smaller than the actual.Try Again")
    elif(num  > x):
        print("Your number is greater than the actual.Try Again")
if(flag == 0):
    print("Number is: ", x)