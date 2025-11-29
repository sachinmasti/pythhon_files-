lst : list = [2,3,4,5,6]

for i in range(len(lst)):
  for j in range(i + 1, len(lst)):
    sum_num = 0
    additon = lst[i]+lst[j]
    sum_num+=additon
    if sum_num % 2==0:
        print(sum_num)
        print((lst[i], lst[j]))
    print()
    print('this is a sorter version')
    new_sum =lst[i]+lst[j]
    if new_sum % 2==0:
        print((lst[i],lst[j]))

s = "education is the key to success"

vowels = 'auioe'

vo_count = sum(s.count(v) for v in vowels)
print(vo_count)

vowels_count = 0

for char in s:
    if char.isalpha():
        if char.lower() in vowels:
            vowels_count +=1
print(vowels_count)

lst1  = [5, 3, 10, 2, 20, 8]
max_dif = float('-inf')
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        diff = lst1[j] - lst1[i]
        if diff > max_dif:
            max_dif = diff
        # print((lst1[i],lst1[j]))
print(max_dif)

nums = [12, 45, 7, 23, 89, 54]

largest = float('-inf')

second_largest = float('-inf')

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Largest:", largest)
print("Second Largest:", second_largest)
