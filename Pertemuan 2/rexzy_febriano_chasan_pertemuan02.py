# -*- coding: utf-8 -*-
"""Rexzy Febriano Chasan_Pertemuan02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y1gtgVXecD9drh5V4R9IhAuUiSdgHCuO

MK DAA Latihan Pertemuan ke 2
"""

a = [1,2,3]
b = [4,5,6]
hasil = a + b
print(sum(hasil))

def penjumlahan(deret1,deret2):
  total = 0
  for i in deret1:
    total += i
  for i in deret2:
    total += i
  return total

penjumlahan(a,b)

penjumlahan(a,b)

import numpy
nilai_siswa = numpy.array ([85,55,40,90])

print(nilai_siswa[3])

nama = input("Masukkan nama: ")
NIM = input("Masukkan NIM mu: ")
print(f"Hello World!\nNama saya {nama}\nNIM saya {NIM}")

if 5 > 2:
  print("Five is greater than 2")

x = 5
y = "john"
print(x)
print(y)

x = 5
x = Sally
print(x)h

def getfirst(list):
  return list[0]
getfirst([1,2,3,4,5,6])

def getlast(list):
  return list[-1]
getlast([1,2,3,4,5,6])

import numpy as np

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Get the shape (size) of the array
size = array.shape
print(size)

list = [1,3,5,7]
def kali(deret1):
  total = 1
  for i in deret1:
    total *= i
  return total

kali(list)
