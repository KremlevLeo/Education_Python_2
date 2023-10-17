res_s = salary = int(input('Enter a salary: '))
twen_c = 0
ten_c = 0
three_c = 0
one_c = 0
while salary > 0:
    if salary > 25:
        salary -= 25
        twen_c += 1
    elif salary >= 10:
        salary -= 10
        ten_c += 1
    elif salary >= 3:
        salary -= 3
        three_c += 1
    elif salary >= 1:
        salary -= 1
        one_c += 1
print(f'{res_s} -> {twen_c}, {ten_c}, {three_c}, {one_c}')
