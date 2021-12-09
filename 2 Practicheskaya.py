# 1 nomer
import numpy as np

# a=np.linspace(10,20,21)
# print(a)
#
# 2 nomer
# b = np.linspace(-2 * np.pi, 2 * np.pi, 5)
# print(b)
# c=np.sin(b).astype(int)
# d=np.cos(b)
# print(c, '\n')
# print(d, '\n')
# print(np.all(d), '\n')
# 3 nomer
# A = np.array([[1, 2],
#               [3, 4]])
# B = np.array([[5, 6],
#               [7, 8]])
# sum = A + B
# print(sum)
# C = A.dot(B)
# print(C)
# y = np.array([1, 2, 3, 4, 5])
# a = np.array([3, 2, 1, 0, -1])
# RSS = np.square(y - a)
# print(RSS)
# print('RSS = ', RSS.sum())
# 4 nomer
# A = np.matrix('4 1 34 1 3')
# B = np.matrix('12 112 1')
# ANew = A.transpose()
# Bnew = ANew.dot(B)
# print(B)
#
# Anew = B.transpose()
# newm = Anew.dot(A)
# print(newm)
# 5nomer
from numpy import linalg

#
#
# X = np.array([[-3, 4, 1],
#               [4, 3, 1]])
# y = np.array([[10],
#               [12]])
# I = np.array([[1, 0, 0],
#               [0, 1, 0],
#               [0, 0, 1]])
# h = 0.1
# xT=X.transpose()
# x1 = xT.dot(X)
# print(x1)
# a = x1 + h * I
# print(a)
# result = np.linalg.matrix_power(a, -1)
# print(result)
# x2 = result.dot(xT)
# print(x2)
# result = x2.dot(y)
# print(result)
# nomer 6
# from scipy.integrate import quad, dblquad
#
#
# def f(x):
#     return 2 * x ** 2 + 7 * x
#
#
# v, err = quad(f, 1, 7)
# print(v, err)
#
#
# def d(x, y):
#     return x * y
#
#
# v, err = dblquad(d, 1, 2, lambda x: 1, lambda y: 2)
# print(v, err)
#
# nomer 7

# l = [str(i)+str(i-1) for i in range(10)]
# print(l)
#
# f = open('text.txt', 'w')
# for index in l:
#   f.write(index + '\n')
# f.close()
# f = open('text.txt', 'r')
# f.read()
# f.close()

# nomer 8
# A = np.array([[1, 2], [3, 4], [5, 6]])
# B = np.array([[7, 8], [9, 10]])
#
# tA = A.transpose()
# C = np.einsum("ik,kj->ij", A, B)
# D = np.einsum("ik,kj->ij", C, B)
# E = np.einsum("ik,kj->ij", D, tA)
# print(E.transpose())
