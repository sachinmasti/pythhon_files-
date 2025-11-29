lst = [1,2,3,4,5,6]
new_lst =[]
for i in lst:
    if i % 2 ==0:
        new_lst.append(i**2)
    elif i % 2!=0:
        new_lst.append(i**3)
print(new_lst)

new_lst1 =[i**2 if i%2==0 else i**3 for i in lst]
print(new_lst1)

nums = [10, 21, 32, 43, 54, 65]
odd =[i for i in nums if i%2!=0]
print(odd)

even =['even' if i%2==0 else 'odd' for i in nums]
print(even)

words = ["apple", "banana", "cat", "dog", "elephant"]

new_words =[i.upper()if len(i) > 3 else i for i in words]
print(new_words)

nums = [1, 2, 3, 4, 5, 6]
square =[i**2 for i in nums ]
print(square)

new_nums =[i *2 if i %2==0 else i *3 for i in nums]
print(new_nums)

nums = [5, 10, 15, 20, 25, 30]
even_num =[f'even - {i}' for i in nums if i%2==0]
print(even_num)

new_n =[f"even - {i*2}" if i %2==0 else f"odd - {i*3}" for i in nums]
print(new_n)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for j in i:
        print(j**2,end = " ")


new_matrix =[j**2 for i in matrix for j in i]
print(new_matrix)


flatten = []
for i in matrix:
    for j in i:
        flatten.append(j)
print(flatten)
flatten_1 = [j for i in matrix for j in i]
print(flatten_1)

print()

even_matrix = []
for i in matrix:
    for j in i:
        if j % 2 == 0:
            even_matrix.append(j)
print(even_matrix)

print()

matrix_even = [j for i in matrix  for j in i if j%2==0]
print(matrix_even)

print()

squar_matrix =[[j*2 for j in  i] for i in matrix]
print(squar_matrix)
