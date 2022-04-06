ticket = int(input("Какое количество билетов вам надо: "))
price = int()

count_ticket = [int(input("Возраст поситителя: ")) for i in range(ticket)]

for i in count_ticket:
    if 25 <= i <= 120:
        price += 1390
    elif 18 <= i < 25:
        price += 990

print(f"Стоимость билетов - {price}")

if ticket > 3:
    discount = round(price/100*90, 2)
    print(f"Стоимость билетов с учетом скидки 10% - {discount}")