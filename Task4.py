number = str(input('Enter a number: '))
result = 'YES'
for i in range(len(number)-1):
    if number[i] > number[1 + 1]:
        result = 'NO'
print(result)
