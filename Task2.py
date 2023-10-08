x = int(input("Enter the number of numbers you want to enter: "))
max = 0
sec_max = 0
for i in range(0, x):
    tmp = int(input('{} number: '.format(i+1)))
    if tmp > max:
        sec_max = max
        max = tmp
    elif tmp > sec_max:
        sec_max = tmp
print('You have enter {} numbers maximum {} and the second maximum number is {}'.format(x, max, sec_max))
