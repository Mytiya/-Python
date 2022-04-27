class Customer:
    def __init__(self, first_name, last_name, city, balance):
        self.name = first_name
        self.surname = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

    

customer_1 = Customer("Иван", "Петров", "Москва", "50")
print(customer_1)