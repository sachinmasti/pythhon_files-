lst =  [4, 5, 4, 6, 7, 5, 8]
# Output: [6, 7, 8]
print(list(dict.fromkeys(lst)))

new_lst = []

for i in lst:
    if lst.count(i) ==1:
        new_lst.append(i)
print(new_lst)

s = "aabbcdef"
new_s = ''.join(i for i in s if s.count(i) ==1)
print(new_s)


list1 = [10, 45, 2, 67, 33, 67]

largest = float ('-inf')
second_largest = float ('-inf')

for i in list1:
    if i > largest:
        second_largest = largest
        largest= i
    elif i > second_largest and i != largest:
        second_largest = i
    
print(f'{largest=}')
print(f'{second_largest=}')

num = 18
sum_num = 0
temp_num = num

for i in str(num):
    sum_num = sum_num+int(i)
if temp_num % sum_num == 0:
    print(f'{temp_num} is Harshad number')
else:
    print(f'{temp_num} is not Harshad number')


string = 'swiss'

# uni_str = ''.join(set(string))
# print(uni_str)

new_str = {}
for i in string:
   new_str[i] = new_str.get(i,0)+1

for j in string:
    if new_str[j] ==1:
        print(j)
        break
# print(new_str)