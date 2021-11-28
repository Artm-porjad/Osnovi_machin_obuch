# 1
# years = [2000, 200, 300, 16]
# for year in years:
#     if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         print('YES')
#     else:
#         print('NO')
#
# 2
# chisla = [142, 425, 315, 646, 752, 52, 1]
# for chislo in chisla:
#     print(chislo // 10 % 10)
# print("---------------------------")
# for chislo in chisla:
#     if chislo>9:
#         print(str(chislo)[-2])
#     else:
#         print(0)
#
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

print(dir(int))