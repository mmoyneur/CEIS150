import time
seconds = int(input("Please enter the number of second: "))
for i in range(seconds, 0,-1):
    print("seconds remaining: ", i)
    time.sleep(1)