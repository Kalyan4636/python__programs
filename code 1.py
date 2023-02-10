# Python code to swap the element
# of first and last row and display
# the result


def interchangeFirstLast(mat, n, m):
	rows = n

	# swapping of element between
	# first and last rows
	for i in range(n):
		t = mat[0][i]
		mat[0][i] = mat[rows-1][i]
		mat[rows-1][i] = t


# Driver Program
mat = [[8, 9, 7, 6],
	[4, 7, 6, 5],
	[3, 2, 1, 8],
	[9, 9, 7, 7]]

n = 4
m = 4
interchangeFirstLast(mat, n, m)

# printing the interchanged matrix
for i in range(n):
	for j in range(m):
		print(mat[i][j], end=" ")
	print("")
