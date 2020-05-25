import random
while True:
    print("\nvalue: {}".format(random.randint(1, 6)))
    ans = input("do you want to continue?(y/n)\t")
    if ans == 'y':
        continue
    else:
        break