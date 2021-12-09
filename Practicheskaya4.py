# nomer 1
# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным). Инкапсуляция делает некоторые из компоненты доступными только внутри класса. Могут возникнуть ситуации, когда пользователь может ввести некорректное значение, для этого и существует инкапсуляция, чтобы ограничить возможности при работе с классами. в python всё равно можно получить скрытые данные и изменить их, скорее это является условностьюи программист сам долже заботиться о её сохранности.
# Статический метод не может изменять ни состояние объекта, ни состояние класса. Статические методы ограничены в том, к каким данным они могут получить доступ. Параметр self это ссылка на конкретный экземпляр класса. Параметр self является ссылкой на первый объект (экземпляр), его можно изменить, однако есть устоявшееся правило, и если его нарушить у других людей могут возникнуть трудности при чтении кода
# class Dog:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#
#     def set_age(self, age):
#         if age in range(1, 20):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def private(self):
#         print("Кличка =", self.__name, "Возраст =", self.__age)
#
#     def __private(self):
#         self.__fam = 14
#         return self.__fam
#         print("Приватный метод")
# a = Dog("Bobik")
# a.set_age(23)
# a.set_age(3)
# a.private()
# class A:
#   @staticmethod
#   def meth(value):
#     print(value)
# a = A()
# a.meth(1)
# A.meth('hello')

# nomer 2
# import math
#
#
# class complex:
#
#     def __init__(self, a, b, type_alg):
#         if not type_alg:
#             ap1 = float(a[:a.find('<')])
#             ap2 = math.radians(float(a[a.find('<') + 1:a.find('°')]))
#             bp1 = float(b[:b.find('<')])
#             bp2 = math.radians(float(b[b.find('<') + 1:b.find('°')]))
#             self.a1 = round(ap1 * math.cos(ap2), 3)
#             self.a2 = round(ap1 * math.sin(ap2), 3)
#             self.b1 = round(bp1 * math.cos(bp2), 3)
#             self.b2 = round(bp1 * math.sin(bp2), 3)
#         else:
#             self.a1 = a[0]
#             self.a2 = ''
#             second = False
#             for i in range(1, len(a) - 1):
#                 if a[i] == '+' or a[i] == '-':
#                     second = True
#                 if not second:
#                     self.a1 += a[i]
#                 else:
#                     self.a2 += a[i]
#             self.b1 = b[0]
#             self.b2 = ''
#             second = False
#             for i in range(1, len(b) - 1):
#                 if b[i] == '+' or b[i] == '-':
#                     second = True
#                 if not second:
#                     self.b1 += b[i]
#                 else:
#                     self.b2 += b[i]
#
#     def slozh(self):
#         a3 = round(int(self.a1) + int(self.b1))
#         b3 = round(int(self.a2) + int(self.b2))
#         if b3 < 0:
#             print('Сложение:', a3, b3, "j", sep='')
#         elif b3 > 0:
#             print('Сложение:', a3, "+", b3, "j", sep='')
#         else:
#             print('Сложение:', a3)
#
#     def vich(self):
#         a3 = round(int(self.a1) - int(self.b1))
#         b3 = round(int(self.a2) - int(self.b2))
#         if b3 < 0:
#             print('Вычитание:', a3, b3, "j", sep='')
#         elif b3 > 0:
#             print('Вычитание:', a3, "+", b3, "j", sep='')
#         else:
#             print('Вычитание:', a3)
#
#     def umnozh(self):
#         a3 = round(int(self.a1) * int(self.b1) - int(self.a2) * int(self.b2))
#         b3 = round(int(self.a1) * int(self.b2) + int(self.a2) * int(self.b1))
#         if b3 < 0:
#             print('Умножение:', a3, b3, "j", sep='')
#         elif b3 > 0:
#             print('Умножение:', a3, "+", b3, "j", sep='')
#         else:
#             print('Умножение:', a3)
#
#     def delen(self):
#         a3 = round(
#             (int(self.a1) * int(self.b1) + int(self.a2) * int(self.b2)) / (int(self.b1) ** 2 + int(self.b2) ** 2), 2)
#         b3 = round(
#             (int(self.b1) * int(self.a2) - int(self.a1) * int(self.b2)) / (int(self.b1) ** 2 + int(self.b2) ** 2), 2)
#         if b3 < 0:
#             print('Деление:', a3, b3, "j", sep='')
#         elif b3 > 0:
#             print('Деление:', a3, "+", b3, "j", sep='')
#         else:
#             print('Деление:', a3)
#
#
# # Полярный вид: 1<23°
# # Сложение
# a = complex('5<36.87°', '2<52°', False)
# a.slozh()
# a = complex('4+5j', '12-7j', True)
# a.slozh()
# a = complex('-3-2j', '15+6j', True)
# a.slozh()
# a = complex('7+8j', '11-8j', True)
# a.slozh()
# a = complex('-9-1j', '5+1j', True)
# a.slozh()
# # Вычитание
# a = complex('5<36.87°', '2<52°', False)
# a.vich()
# a = complex('5+9j', '3+24j', True)
# a.vich()
# a = complex('-4+16j', '11-8j', True)
# a.vich()
# a = complex('43+7j', '43-2j', True)
# a.vich()
# # Умножение
# a = complex('5<36.87°', '2<52°', False)
# a.umnozh()
# a = complex('2+3j', '-1+1j', True)
# a.umnozh()
# a = complex('7+3j', '5-8j', True)
# a.umnozh()
# a = complex('-10-4j', '8+1j', True)
# a.umnozh()
# # Деление
# a = complex('5<36.87°', '2<52°', False)
# a.delen()
# a = complex('-2+1j', '1-1j', True)
# a.delen()
# a = complex('2+5j', '3-2j', True)
# a.delen()
# a = complex('23+1j', '2+1j', True)
# a.delen()

# nomer 3
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return str((self.x, self.y, self.z))
#
#     def __add__(self, b):
#         x = self.x + b.x
#         y = self.x + b.y
#         z = self.x + b.z
#         return Vector(x, y, z)
#
#     def __sub__(self, b):
#         x = self.x - b.x
#         y = self.x - b.y
#         z = self.x - b.z
#         return Vector(x, y, z)
#
#     def __mul__(self, b):
#         if type(b) is Vector:
#             s = self.x * b.x + self.y * b.y + self.z * b.z
#             return s
#         else:
#             return Vector(self.x * b, self.y * b, self.z * b)
#
#     def __abs__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def cos_angle(self, b):
#         return (self * b) / (abs(self) * abs(b))
#
#
# v1 = Vector(1, 1, 1)
# v2 = Vector(1, 3, -2)
# v = v1 + v2
# print(v)
# cf = v1 * v2
# print(cf)
# co = v1.cos_angle(v2)
# print(co)
# v3 = v1 * 10
# print(v3)

# 4


# def calls_counter(call_func_in_dec):
#     def n_add(n_in_dec):
#         n_in_dec += 1
#         return call_func_in_dec(n_in_dec)
#     return n_add
#
# @calls_counter
# def call_func(a):
#     global n
#     print('This function was called', a, ' times')
#     n = a
#
#
#
# n = 0
#
# for i in range(5):
#     call_func(n)

# Nomer 5

# class CopyClassAttrs:
#     _a_ = '123'
#
#
# def get_atr(cls_template):
#     a = dir(cls_template)
#     print(a)
#     arr_atr = []
#     for i in a:
#         if not i.startswith('_', 2):
#             arr_atr.append(i)
#
#     def give_atr(cls_to_change):
#         for i in arr_atr:
#             if getattr(cls_to_change, i, False):
#                 setattr(cls_to_change, '_new'+i, getattr(cls_template, i))
#             else:
#                 setattr(cls_to_change, i, getattr(cls_template, i))
#         return cls_to_change
#     return give_atr
#
#
# @get_atr(CopyClassAttrs)
# class Qwert:
#     _a_ = "345"
#     def a(self):
#         print(dir(Qwert))
#
# f = Qwert()
# f.a()


# nomer 6
# import csv
#
# class Matrix:
#     def __init__(self):
#         pass
#
#     def umnozh(self, A, B):
#         if not len(A[0]) == len(B):
#             raise Exception('Количество столбцов первой матрицы и строк второй матрицы не совпадают')
#         n_strok_A = len(A)
#         n_stolb_A = len(A[0])
#         n_stolb_B = len(B[0])
#         summ = 0
#         C = [[0 for j in range(n_stolb_B)] for i in range(n_strok_A)]
#         for i in range(n_strok_A):
#             for j in range(n_stolb_B):
#                 for z in range(n_stolb_A):
#                     summ += A[i][z] * B[z][j]
#                 C[i][j] = summ
#                 summ = 0
#         for i in range(n_strok_A):
#             print(*C[i])
#         print('---------------')
#
#         return C
#
#     def transpon(self, A):
#         n_strok = len(A)
#         n_stolb = len(A[0])
#         C = [[0 for j in range(n_strok)] for i in range(n_stolb)]
#         for i in range(n_strok):
#             for j in range(n_stolb):
#                 C[j][i] = A[i][j]
#         for i in range(n_stolb):
#             print(*C[i])
#         print('---------------')
#
#         return C
#
#     def sled(self, A):
#         n_strok = len(A)
#         n_stolb = len(A[0])
#         summ = 0
#         n = min([n_stolb, n_strok])
#         for i in range(n):
#             summ +=A[i][i]
#         print('След матрицы = ', summ)
#
#         return summ
#
#     def opred(self, A):
#         n_strok = len(A)
#         n_stolb = len(A[0])
#         summ = 0
#         if n_stolb != n_strok:
#             print('Количество столбцов первой матрицы и строк второй матрицы не совпадают')
#
#             return None
#         else:
#             def dop_min(J, matrix):
#                 summ1 = 0
#                 n = len(matrix)
#                 C = [[0 for j in range(n-1)] for i in range(n-1)]
#                 # print(C)
#                 for i in range(0, n-1):
#                     a_stolb = 0
#                     for j in range(n-1):
#                         if j == J:
#                             a_stolb = 1
#                         # print(matrix[i+1][j+a_stolb])
#                         C[i][j] = matrix[i+1][j+a_stolb]
#                         # print(C)
#                 if n == 2:
#                     return C[0][0]
#                 else:
#                     for i in range(n-1):
#                         summ1 += (-1) ** (2 + i) * C[0][i] * dop_min(i, C)
#                     return summ1
#             for i in range(n_stolb):
#                 summ += (-1)**(2+i)*A[0][i]*dop_min(i, A)
#         print('Определитель =', summ)
#         return summ
#
#     def zapis(self, A):
#         with open("matrix.csv", mode="w", encoding='utf-8') as w_file:
#             file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
#             for i in A:
#                 file_writer.writerow(i)
#
#     def chtenie(self, A):
#         with open("matrix.csv", encoding='utf-8') as r_file:
#             file_reader = csv.reader(r_file, delimiter=",")
#             for row in file_reader:
#                 print(*row)
#
#
#
# a = Matrix()
# A = [[0, 1, 2],
#      [3, 4, 5],
#      [6, 7, 8]]
# B = [[8, 7, 6],
#      [5, 4, 3],
#      [2, 1, 0]]
# a.umnozh(A, B)
# a.transpon(A)
# a.sled(A)
# a.sled(B)
# a.opred(A)
# a.opred(B)
# C = [[1, 2, 3],
#      [4, 5, 6]]
# D = [[8, 7, 6],
#      [5, 4, 3],
#      [2, 1, 0]]
# a.umnozh(C, D)
# a.transpon(C)
# a.sled(C)
# a.sled(D)
# a.opred(C)
# a.opred(D)
# a.zapis(A)
# a.chtenie(A)

# nomer 7
# import typing as t
#
#
# class Coffee:
#     def __init__(self, dobavka: t.Optional[str] = None):
#         if dobavka:
#             raise Exception("Выбран 2 раза кофе")
#
#     stoim = 0
#
#
# class Latte(Coffee):
#     cost = 1
#
#
# class Capuchino(Coffee):
#     cost = 2
#
#
# class Americano(Coffee):
#     cost = 3
#
#
# class Dobavka:
#
#     def __init__(self, dobavka: t.Optional[str] = None):
#         if dobavka:
#             Coffee.stoim += dobavka.cost
#         else:
#             raise Exception("Кофе не является аргументом")
#
#
# class Sahar(Dobavka):
#     cost = 0.1
#
#     def calculate_cost(self):
#         print(Coffee.stoim + self.cost)
#         Coffee.stoim = 0
#
#
# class Slivki(Dobavka):
#     cost = 0.2
#
#     def calculate_cost(self):
#         print(Coffee.stoim + self.cost)
#         Coffee.stoim = 0
#
#
# class Kardamon(Dobavka):
#     cost = 0.3
#
#     def calculate_cost(self):
#         print(Coffee.stoim + self.cost)
#         Coffee.stoim = 0
#
#
# class Penka(Dobavka):
#     cost = 0.4
#
#     def calculate_cost(self):
#         print(Coffee.stoim + self.cost)
#         Coffee.stoim = 0
#
#
# class Sirop(Dobavka):
#     cost = 0.5
#
#     def calculate_cost(self):
#         print(Coffee.stoim + self.cost)
#         Coffee.stoim = 0
#
#
# Penka(Sirop(Capuchino)).calculate_cost()
# Kardamon(Penka(Sirop(Capuchino))).calculate_cost()
# Latte(Kardamon(Penka(Sirop()))).calculate_cost
# Latte(Kardamon(Penka(Sirop(Latte)))).calculate_cost
