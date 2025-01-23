# Задача 2. Елените на Дядо Коледа
# Дядо Коледа много обича да пътешества, но за съжаление се случило, така че точно преди да замине на
# почивка три от елените му се разболяли и трябва да ги остави. Когато заминава, той трябва да съобрази колко
# храна да остави на всеки един от елените, за да не останат гладни. Напишете програма, която пресмята дали
# оставената от Дядо Коледа храна ще е достатъчна за времето, в което него няма да го има.Всеки елен изяжда
# определено количество храна на ден.
import math
# Вход:
# От конзолата се четат пет реда:
# • Първи ред – брой дни, в които Дядо Коледа отсъства – цяло число в интервала [1…5000]
days_absent = int(input())
# • Втори ред – оставена храна в килограми – цяло число в интервала [0…100000]
food_in_kg = int(input())
# • Трети ред – храна на ден за първия елен в килограми – реално число в интервала [0.00…100.00]
r1_daily_food_kg = float(input())
# • Четвърти ред – храна на ден за втория елен в килограми– реално число в интервала [0.00…100.00]
r2_daily_food_kg = float(input())
# • Пети ред – храна на ден за третия елен в килограми – реално число в интервала [0.00…100.00]
r3_daily_food_kg = float(input())

food_needed = (r1_daily_food_kg * days_absent) + (r2_daily_food_kg * days_absent) + (r3_daily_food_kg * days_absent)
# Изход:
# На конзолата трябва да се отпечата на един ред:
# • Ако оставената храна Е достатъчна:
if food_needed < food_in_kg:
    diff = food_in_kg - food_needed
    print(f'{math. floor(diff)} kilos of food left.')
# ▪ Резултатът трябва да е закръглен към ПО-МАЛКОТО цяло число
# • Ако оставената храна НЕ Е достатъчна:
elif food_needed >= food_in_kg:
    diff = food_needed - food_in_kg
    print(f'{math. ceil(diff)} more kilos of food are needed.')
# ▪ Резултатът трябва да е закръглен към ПО-ГОЛЯМОТО цяло число