# просим ввести строку и вносим ее в регистр
r = input("Введите вашу любимую цитату")
r = r.lower()

# убираем символы пунктуации
r = r.replace(".", "")
r = r.replace(",", "")
r = r.replace("-", "")
r = r.replace(":", "")
r = r.replace(";", "")
r = r.replace("?", "")
r = r.replace("!", "")

# убрали пробелы справа
r = r.rstrip()

# узнаем какое слово нужно заменить и  переводим регистр
x = input("Какое слово вы хотите заменить?")
x = x.lower()

# узнаем  показываем индекс
index = r.find(x)
print("Индекс слова в строке:", index)

# узнаем на какое слово заменить и переводим в регистр
z = input("На какое слово вы хотите заменить?")
z = z.lower()

print(r.replace(x, z))