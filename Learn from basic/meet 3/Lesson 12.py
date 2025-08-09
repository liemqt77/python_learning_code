#belajar Array atau list
"""
my_list = [1, 2.5, "hello", True] #1
print(my_list)

my_list = [10, 20, 30, 40, 50] #2
print(my_list[0])  # Output: 10
print(my_list[3])  # Output: 40

# Menambahkan elemen di akhir list #3
my_list = [1, 2, 3]
my_list[1] = 5  # Mengubah nilai elemen kedua (indeks 1)
print(my_list)
my_list.append(6)
print(my_list)  # Output: [1, 5, 3, 6]

# Menghapus elemen tertentu
my_list.remove(5)
print(my_list)  # Output: [1, 3, 6]

# Menghapus elemen berdasarkan indeks
my_list.pop(1)
print(my_list)  # Output: [1, 6]

my_list = [5, 3, 8, 2]
print(len(my_list))  # Output: 4

my_list.sort()
print(my_list)  # Output: [2, 3, 5, 8]

my_list.reverse()
print(my_list)  # Output: [8, 5, 3, 2]

import array #4

# Membuat array dengan tipe data 'i' (integer)
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)

# Array dengan tipe data float
arr_float = array.array('f', [1.1, 2.2, 3.3])
print(arr_float)

arr = array.array('i', [1, 2, 3, 4, 5])

# Akses elemen dengan indeks
print(arr[0])  # Output: 1

# Modifikasi elemen dalam array
arr[2] = 10
print(arr)  # Output: array('i', [1, 2, 10, 4, 5])

# Menambahkan elemen ke akhir array
arr.append(6)
print(arr)  # Output: array('i', [1, 2, 10, 4, 5, 6])

# Menghapus elemen pertama yang ditemukan
arr.remove(10)
print(arr)  # Output: array('i', [1, 2, 4, 5, 6])

# Menghapus elemen berdasarkan indeks
arr.pop(1)
print(arr)  # Output: array('i', [1, 4, 5, 6])

arr.reverse()
print(arr)  # Output: array('i', [6, 5, 4, 2, 1])

"""

