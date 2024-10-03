int_var = 10         # int (ціле число)
float_var = 3.14     # float (дробове число)
str_var = "Hello"    # str (рядок)
bool_var = True      # bool (логічна змінна)

print("int_var =", int_var)
print("float_var =", float_var)
print("str_var =", str_var)
print("bool_var =", bool_var)

print("Тип int_var:", type(int_var))
print("Тип float_var:", type(float_var))
print("Тип str_var:", type(str_var))
print("Тип bool_var:", type(bool_var))

a = 10
b = 5
c = 7

addition = a + b   # додавання
subtraction = a - b  # віднімання
multiplication = a * b  # множення
division = a / b  # ділення
power = a ** b  # піднесення до степеня

rounded_value = round(division, 2)  # округлення
absolute_value = abs(subtraction)  # модуль різн
modulus = a % b  # оператор модулю

average = (a + b + c) / 3

print("Додавання:", addition)
print("Віднімання:", subtraction)
print("Множення:", multiplication)
print("Ділення:", division)
print("Піднесення до степеня:", power)
print("Округлене ділення до 2 знаків:" , round)
print("Модуль різниці:", absolute_value)
print("Оператор модулю (a % b):", modulus)
print("Середнє арифметичне трьох чисел:", average)

name = "Валерій"
age = 43

greeting = "Привіт, моє ім'я " + name + "."

name_upper = name.upper()  # Великий регістр
name_lower = name.lower()  # Малий регістр

info = f"Мене звати {name}, і мені {age} років."

print(greeting)
print("Ім'я у верхньому регістрі:", name_upper)
print("Ім'я у нижньому регістрі:", name_lower)
print(info)

number = int(input("Введіть число"))
if number % 2 == 0:print(f"Число {number} є парним.")
else:print(f"Число {number} є непарним.")
lower_bound: int = 10
upper_bound = 50
if lower_bound <= number <= upper_bound:print(f"Число {number} входить у діапазон від {lower_bound} до {upper_bound}.")
else: print(f"Число {number} не входить у діапазон від {lower_bound} до {upper_bound}.")
def add_two_numbers(a, b):
    return a + b
result = add_two_numbers(5, 10)
print("Сума чисел:", result)
def reverse_string(s):
    return s[::-1]
reversed_str = reverse_string("Привіт")
print("Рядок у зворотному порядку:", reversed_str)

numbers = [1, 2, 3, 4, 5]

print("Елементи списку:")
for number in numbers:print(number)

numbers.append(6)
print("\nСписок після додавання нового елемента:", numbers)

numbers.pop()
print("Список після видалення останнього елемента:", numbers)

student = {
    "ім'я": "Валерій",
    "вік": 43,
    "факультет": "Комп'ютерниі науки"
}

print("Ім'я студента:", student["ім'я"])

student["рік навчання"] = 2.10

print("\nОновлений словник з інформацією про студента:")
for key, value in student.items():print(f"{key}: {value}")

def divide_numbers():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        result = num1 / num2
        print(f"Результат ділення: {result}")

    except ZeroDivisionError:print("Помилка: ділення на нуль неможливе!")

    except ValueError:print("Помилка: введіть коректне число!")

divide_numbers()


print('Finish');





