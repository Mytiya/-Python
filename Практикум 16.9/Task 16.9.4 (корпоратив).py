class Customer:
    def __init__(self, first_name, last_name, city, balance):
        self.name = first_name
        self.surname = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

    def corporate(self):
        return f'"{self.name} {self.surname}. {self.city}"'

customer_1 = Customer("Иван", "Петров", "Москва", 50)
customer_2 = Customer("Петр", "Иванов", "Ижевск", 100)
customer_3 = Customer("Евгений", "Сидоров", "Самара", 64)
customer_4 = Customer("Мария", "Петрова", "Саратов", 94)
customer_5 = Customer("Анна", "Смирнова", "Пенза", 120)

customers = [customer_1, customer_2, customer_3, customer_4, customer_5]

for customer in customers:
    print(customer.corporate())
