count = int(input('Введите количество билетов: '))
sum = 0
count_bil = count
while count_bil > 0:
    age = int(input('Введите возраст посетителя: '))
    if age < 18:
        sum = sum
    elif 18 <= age < 25:
        sum = sum + 990
    elif age >= 25:
        sum = sum + 1390
    count_bil = count_bil - 1
if count > 3:
    sum_itogo = sum * 0.9
else:
    sum_itogo = sum
print('Сумма к оплате =', sum_itogo)
if count >3:
    print('Ваша скидка составила =', sum * 0.1)