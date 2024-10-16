import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
Библиотека  pandas — это библиотека, которая предназначена для анализа уже структурированных данных, 
                     размещённых в таблицах
С помощью pandas можно: 1. Работать с DataFrame
                        2. Создавать сводные таблицы из нескольких
                        3. Осуществлять предобработку данных
                        4. Группировать данные по определённым признакам
                        5. Выводить определённые значения по фильтрам или уникальности
                        6. Использовать агрегирующие функции
                        и т.д.
"""

# Примеры:
# 1. Создание датафрейма из данных, введённых вручную
data = {'Name': ['Aleksandr', 'Vladimir', 'Marina', 'Olga', 'Natalya'],
        'Year_birth': [1982, 1984, 1982, 1983, 1983],
        'Grade': [4.51, 4.43, 4.44, 4.82, 4.56],
        'Gender': ['men', 'men', 'woman', 'woman', 'woman']}

data_student = pd.DataFrame(data)
print(data_student)
# 2. Сортировка по значению
print(data_student.sort_values('Grade', ascending=False))
# 3. Группировка данных и применение агрегирующих функций
print(data_student.groupby(['Gender']).agg({'Grade': 'mean', 'Name': 'count'}))
print(data_student.groupby(['Year_birth']).agg({'Grade': 'mean', 'Name': 'count'}))

""" 
Библиотека  numpy — это библиотека для работы с массивами 
С помощью numpy можно: 1. Cоздавать массивы — структуры данных, позволяющие хранить несколько значений 
                        в одной переменной.
                        2. Использование математических констант (numpy.pi, numpy.e), 
                        модуль генерации случайных чисел (numpy.random)
                        3. Выполнять математические, логические операции над массивами
                        4. Работать в области линейной алгебры
                        5. Статистические задачи
"""

# Примеры:
# 1. Создание массива
a1 = np.arange(0, 6).reshape(2, 3)
b1 = np.arange(10, 61, 10).reshape(2, 3)
# 2. Математические операции над массивами
print(f'Рузультат деления суммы матриц a1 и d1 на матруцу b1: \n{(a1 + b1) / b1}')
a2 = np.array([1, 2, 3])
b2 = np.array([1, 3, 2])
print(f'Рузультат сравнения матриц a2 и b2: \n{a2 > b2}')
b3 = np.arange(0, 6).reshape(3, 2)
print(f'Результат скалярного произведения двух матриц a1 и b3: \n{np.dot(a1, b3)}')
# 3 Статистика в numpy
student_grades = []
for i in range(20):
    grades = np.random.randint(2, 6)
    student_grades.append(grades)
print(f'средний балл студента: {np.mean(student_grades)}')
print(f'медиана оценок: {np.median(student_grades)}')
print(f'средне квадратичное отклонение оценок: {round(np.std(student_grades), 2)}')

""" 
Библиотека  matplotlib — это библиотека, которая предназначена для для визуализации данных. 
С помощью matplotlib можно создавать любые виды графиков: линейные, круговые диаграммы, 
построчные гистограммы и другие — в зависимости от задач
"""

# Примеры:
# 1. Линейный график
student_grades = [3, 4, 4, 5, 3, 4, 5, 4, 4]
date = ["01.08", "02.08", "05.08", "06.08", "07.08", "08.08", "09.08", "10.08", "12.08"]

plt.plot(date, student_grades, '-*', color='red')
plt.title('График успеваемости')
plt.ylabel('Оценка')
plt.yticks(range(2, 6, 1))
plt.xlabel('Дата')
plt.show()

# 2. boxplot
data_tickets = pd.DataFrame(np.random.randint(50, size=(1000, 1)), columns=['ticket_number'])

plt.boxplot(x='ticket_number', data=data_tickets)
plt.title('Распределение билетов')
plt.ylabel('')
plt.xlabel('Номер билета')
plt.show()

# 3. Диаграмма рассеяния 3D
np.random.seed(10)
rng = np.random.default_rng()
xs = rng.uniform(10, 50, 200)
ys = rng.uniform(0, 10, 200)
zs = rng.uniform(-20, 20, 200)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.show()
