# 1
# years = [2000, 200, 300, 16]
# for year in years:
#     if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         print('YES')
#     else:
#         print('NO')
#
# 2
# chisla = [14, 4256, 31566, 6, 7526, 52666, 1]
# for chislo in chisla:
#     k=0
#     a = chislo
#     for i in str(a):
#         k+=1
#         a = a // 10
#     print(k)
# print("---------------------------")
#
#
# for chislo in chisla:
#     print(len(str(chislo)))

# 3
# chisla = [1, 2, 3, 4, 5, 6]
#
# for chislo in chisla:
#     k = 1
#     S = 0
#     for i in range(1, chislo+1):
#         k *= i
#         S += k
#     print(S)
#
#
# 4 задача
# stroki = ['123321', '12321', '123', '123123']
# for i in stroki:
#     if i == i[::-1]:
#         print('YES')
#     else:
#         print('NO')
#
# for stroka in stroki:
#     n = len(stroka)
#     f = True
#     for i in range(0, n//2):
#         if not stroka[i] == stroka[n-i-1]:
#             f = False
#     if f:
#         print('YES')
#     else:
#         print('N0')
#
# for stroka in stroki:
#     n = len(stroka)
#     if n % 2 == 0:
#         if stroka[0:(n//2)] == stroka[n:(n//2)-1:-1]:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         if stroka[0:(n // 2)+1] == stroka[n:(n // 2)-1:-1]:
#             print('YES')
#         else:
#             print('NO')
#
#
# 5
# s = "дан текст в виде строки напишите функцию которая возвращает словарь где ключами являются уникальные слова из этого текста а значениями число раз которое данное слово встретилось в тексте считать что слова разделяются пробелами предложите как минимум два различных решения."
# d = dict()
# for i in s.split():
#     if d.get(i, False):
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#
# 6 задание
# a = ['a', 2, 'a', 4, 3]
# n = len(a)
# b = 'a'
# k = 0
# cortezh = ()
# ks = 0
# ke = 0
# for i in range(0, n):
#     if a[i] == b:
#         ks = i
#         break
# for i in range(n):
#     if a[i] == b:
#         ke = i
#         k += 1
# if k == 1:
#     cortezh = (ke, 'None')
#     print(cortezh)
# else:
#     cortezh = (ks, ke)
#     print(cortezh)

# # упражнение 7
#
# # сортировка с помощью встроенной функции
#
# # def printSort(L):
# #     new = []
# #     L = sorted(L, reverse = True)
# #     i = 0
# #     while i < len(L):
# #         if L[i] > 0:
# #             new.append(L[i] ** 2)
# #             i += 1
# #         else:
# #             i += 1
# #     return new
# # a = [2, 4, -15, 2, -3, 3, 10 ]
# # print(printSort(a))
#
# # сортировка пузырьковая
#
# # def printSort2(L):
# #     new = []
# #     n = len(L)
# #     for i in range(n):
# #         if L[i] > 0:
# #             new.append(L[i] ** 2)
# #     i = 0
# #     n = len(new)
# #     for i in range(n-1):
# #         for j in range(n-1-i):
# #             if new[j] < new[j+1]:
# #                 new[j], new[j+1] = new[j+1], new[j]
# #     return new
# #
# # a = [2, 4, -15, 2, -3, 3, 10 ]
# # print(printSort2(a))
#
# # сортировка выборочная
# # def printSort3(L):
# #     new = []
# #     n = len(L)
# #     for i in range(n):
# #         if L[i] > 0:
# #             new.append(L[i] ** 2)
# #     i = 0
# #     n = len(new)
# #     print(new)
# #     for i in range(n-1):
# #         m = i
# #         j = i + 1
# #         while j < len(new):
# #             if new[j] < new[m]:
# #                 m = j
# #             j = j + 1
# #         new[i], new[m] = new[m], new[i]
# #     new = new[::-1]
# #     return new

# 9
# def sled_stroka(stroka):
#     stroka = [1] + stroka
#     n = len(stroka)-1
#     for i in range(1, n):
#         stroka[i] += stroka[i+1]
#     return stroka
#
#
# stroka = []
# n = int(input())
# for i in range(n):
#     stroka = sled_stroka(stroka)
#     print(*stroka)
#
# упражнение 10

# from os import path
# import os
# k = 0
# pat = os.path.abspath('text.txt')
# pat2 = os.path.abspath('text2.qwe')
# print(pat)
# print(pat2)
# full_path = path.basename(r'C:\Users\msi\PycharmProjects\prakticheskaya3\text.txt ')
# name = path.splitext(full_path)[1]
# print(name)
# for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
#   base_file, ext = os.path.splitext(filename)
#   if ext == ".123":
#     k += 1
#     os.rename(filename, base_file + ".txt")
# print(k)
# print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

# 11
# a = {'a', 'b', 'c', 'd', '1', '2', '3'}
# b = {'b', 'd', '2'}
#
# print(a-b)

# 13
# chisla = [5, 1, 8, 14, -1]
# for chislo in chisla:
#     a = [1, 1]
#     if chislo == -1:
#         i = 2
#         while True:
#             a.append(a[i - 1] + a[i - 2])
#             print(a[i])
#             i+=1
#     else:
#         for i in range(2, chislo):
#             a.append(a[i-1]+a[i-2])
#         print(*a)

# 15

# stroki = ['dsf32431', 'fref134f', 'f43fe43', 'ASFDf34g3']
# for stroka in stroki:
#     new = ''
#     mi = 10
#     for i in stroka:
#         if 64<ord(i)<91:
#             new+=str(ord(i))
#             if ord(i)%10<mi:
#                 mi = ord(i)%10
#             elif ord(i)%100<mi:
#                 mi = ord(i)%100
#         else:
#             new+= i
#     if mi == 10:
#         print(new)
#     else:
#         print(new.split(str(mi)))

# import re
# nomera = re.findall(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', ('89137759434 номер1 8-999-123-45-67  8(988)3362148 номер2 номер4 +78005553535  8(932)-123-83-42 8495123-45-67 8(944)544-23-87 8 995 767 87 90  8 936 1234567 8 (916) 865-21-64'))
# print(nomera)

# 17
# a = (0,
#      (11,
#       (21, None, None),
#       (22, None, None)
#       ),
#      (12,
#       (23, None, None),
#       (24, None, None)
#       )
#      )
# visited = set()
#
#
# def dfs1(graph, s):
#     global visited
#     if graph not in visited:
#         s += graph[0]
#         print(graph[0], s)
#         visited.add(graph)
#         if graph[1] is not None or graph[2] is not None:
#             for i in range(1, 3):
#                 dfs1( graph[i], s)
#
#
# print("Following is the Depth-First Search")
# dfs1(a, 0)
#
# visited = set()
#
# def dfs2(graph, s):
#     global visited
#     if graph not in visited:
#         s += graph[0]
#         print(graph[0], s)
#         visited.add(graph)
#         if graph[1] is not None or graph[2] is not None:
#             for i in range(1,3):
#                 dfs2(graph[i], s)
#
#
# dfs2(a, 0)
