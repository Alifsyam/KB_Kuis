# Mendefinisikan matriks
A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Menghitung perkalian matriks A dan C
AC = np.dot(A, C)
print("Hasil perkalian matriks A dan C:")
print(AC)

# Menghitung perkalian matriks A dan B
AB = np.dot(A, B)
print("\nHasil perkalian matriks A dan B:")
print(AB)

# Menghitung penjumlahan matriks D dan E
D_plus_E = np.add(D, E)
print("\nHasil penjumlahan matriks D dan E:")
print(D_plus_E)

# Menghitung pengurangan matriks D dan E
D_minus_E = np.subtract(D, E)
print("\nHasil pengurangan matriks D dan E:")
print(D_minus_E)