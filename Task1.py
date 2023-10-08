x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
count = 0
for i in range(x,y+1):
    if i%3 == 0:
        count+=1
    elif i%2 == 0:
        count+=1
print("In the interval from {} to {}. Numbers that are divisible by 2 and by 3 is {}".format(x,y,count))