lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]
lagest_num =lst[0]
for i in lst:
    if i> lagest_num:
        lagest_num = i
print(lagest_num)

odd_num = [i for i in lst if i%2==0]
even_num = [i for i in lst if i %2!=0]

print(odd_num)
print(even_num)

for i in lst:
    if i %2 ==0:
        odd_num.append(i)
    else:
        even_num.append(i)
print(f' odd number = {odd_num}')
print(f' even number = {even_num}')

lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]
total =0
for i in lst:
    total+= i
print(total)

lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]
lagest_num = lst[0]
second_largest = lst[2]
for i in lst:
    if i > lagest_num:
        second_largest = lagest_num
        lagest_num = i
    elif i > second_largest:
        second_largest = i
print(second_largest)

