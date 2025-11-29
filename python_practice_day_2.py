# English: Create a list and separate odd and even numbers using a for loop.
# Hindi: Ek list banayein aur for loop ka upyog karke odd aur even numbers ko alag karein.
lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]
odd_num =[]
even_num =[]

for i in lst:
    if i %2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(odd_num)
print(even_num)

# English: Separate odd and even numbers using list comprehension.
# Hindi: List comprehension ka upyog karke odd aur even numbers ko alag karein.
odd_number =[i for i in lst if i %2==0]
even_number =[i for i in lst if i %2!=0]
print(odd_number)
print(even_number)

# English: Calculate the sum of even numbers and the count of odd numbers.
# Hindi: Even numbers ka sum aur odd numbers ki ginti calculate karein.
even_count = sum(i for i in lst if i %2==0)
odd_count = len([i for i in lst if i %2!=0])
print(even_count)
print(odd_count)

print()
lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]

# English: Count numbers divisible by both 3 and 5.
# Hindi: 3 aur 5 dono se divisible numbers ki ginti karein.
count_both = len([i for i in lst if i%3==0 and i %5==0])
print(count_both)
print('this is a that number')

# English: Count numbers divisible by 3 or 5 using a for loop.
# Hindi: For loop ka upyog karke 3 ya 5 se divisible numbers ki ginti karein.
count_3 = 0
count_5 =0
for i in lst:
    if  i%3==0:
        count_3 +=1
    elif i %5==0:
        count_5 +=1
print(count_3)
print(count_5)

lst =[11,1,2,3,4,5,111,6,7,8,9,10,99]

# English: Square each number and filter for even results.
# Hindi: Har number ka square karein aur even results ko filter karein.
print('this is a even count ')
enen_number = [i for i in lst if (i**2)%2==0 ]
print(enen_number)
print()

# English: This block has incorrect logic for counting squared evens/odds.
# Hindi: Is block ka logic galat hai.
squar_odd =0
squar_even = 0
for i in lst:
    if i**2 ==i%2==0:
        squar_even+=1
    else:
        squar_odd+=1
print(squar_even)
print(squar_odd)

ls1 =[4, 11, 8, 15, 3, 19]

# English: Filter numbers greater than or equal to 5 and less than 5 using a for loop.
# Hindi: For loop ka upyog karke 5 se bade ya barabar aur 5 se chhote numbers ko filter karein.
grater_then_5 =[]
grater_then_10 =[]
for i in ls1:
    if i >=5:
        grater_then_5.append(i)
    else:
        grater_then_10.append(i)
print(grater_then_10)        
print(grater_then_5)        

# English: Filter numbers into a dictionary based on whether they are above or below a certain value using list comprehension.
# Hindi: List comprehension ka upyog karke numbers ko ek dictionary mein filter karein, is aadhar par ki ve ek vishisht maan se upar hain ya neeche.
result = {
    'below_10':[i for i in lst if i>5],
    'bellow_5':[i for i in lst if i<=5]
}
print(result)

result = {
    "Below 10": [i for i in ls1 if i < 10],
    "10 or above": [i for i in ls1 if i >= 10]
}
print(result)

# English: Filter numbers that are divisible by 2 but not by 4.
# Hindi: 2 se divisible lekin 4 se nahi, aise numbers ko filter karein.
num = [2, 4, 6, 8, 10, 12]
new_num =[]
for i in num:
    if i%2==0 and i %4 !=0:
        new_num.append(i)

print(new_num)

# English: Perform a bitwise XOR operation.
# Hindi: Bitwise XOR operation perform karein.
a = 1
b =10
print(a^b)

# English: Find numbers in a list that are greater than the average of the list.
# Hindi: List mein average se bade numbers ko dhoondhein.
num = [2, 4, 6, 8, 10, 12]
avg = sum(num)/ len(num)
grater_then_avg = []
for i in num:
    if i > avg:
        grater_then_avg.append(i)
print(grater_then_avg)

grater_then_avg_1 = [i for i in num if i > avg]
print(grater_then_avg_1)

even_num =[13, 24, 57]
odd_num = [12, 3, 5, 8]
# Output: [31, 24, 75]Output: [12, 3, 5, 8]

lst = [13, 24, 57, 8, 3]
# new_lst = [int(str(num)[::-1]) if num % 2 != 0 else num for num in lst]
# print(new_lst)
# 

# English: Reverse the digits of even numbers in a list.
# Hindi: List mein even numbers ke digits ko reverse karein.
list1 = [12,23,34,45,566,67,78,89,234]
new_list =[int(str(i)[::-1]) if i%2==0 else i for i in list1]
print(new_list)

# English: Create a dictionary with numbers as keys and their squares as values using dictionary comprehension.
# Hindi: Dictionary comprehension ka upyog karke ek dictionary banayein jisme numbers keys hain aur unke squares values hain.
list2 = [2, 3, 4]
new_dict = {i: i **2 for i in list2}
print(new_dict)

# English: Create a dictionary with numbers as keys and their squares as values using a for loop.
# Hindi: For loop ka upyog karke ek dictionary banayein jisme numbers keys hain aur unke squares values hain.
new_list1= {}
for i in list2:
    new_list1[i] = i**2
print(new_list1)

# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]  # 1, 1+2=3, 3+3=6, 6+4=10

# English: Calculate the cumulative sum of a list.
# Hindi: Ek list ka cumulative sum calculate karein.
sachin = [1,2,3,4]
new_sachi =[]
cum_sum =0
for i in sachin:
    cum_sum +=i
    new_sachi.append(cum_sum)
print(new_sachi)


# Input: [2, 4, 5, 6, 8, 10]
# Output: [2, 4, 6, 8, 10]  # all divisible by 2

# English: Filter numbers in a list that are divisible by the first element of the list.
# Hindi: List mein pehle element se divisible numbers ko filter karein.
masti =[2,4,5,6,8,10]
m =masti[0]
new_masti =[]
for i in masti:
    if i % m ==0:
        new_masti.append(i)
print(new_masti)

new_sachin =[i for i in masti if i%m ==0]
print(new_sachin)
