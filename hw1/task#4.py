Fuel_consumption = float(input("витрачання палива автомобілем за 100 км"))
price_for_1_liter = float(input("сьогоднішня ціна 1 л палива"))
distance = float(input("скільки кілометрів треба здолати"))

Fuel_consumption = Fuel_consumption * distance / 100  # узнаем цену за 1 км
answer = Fuel_consumption * price_for_1_liter  # цена за всю поездку
print(f'{answer:.2f} грн')
