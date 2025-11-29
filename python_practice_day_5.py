# English: Calculate the product and sum of digits of a number.
# Hindi: Ek number ke digits ka product aur sum nikalo.
number = 405
product_num = 1
sum_digit = 0
while number > 0:
    digit = number % 10
    product_num = product_num * digit
    sum_digit = sum_digit + digit
    number //= 10
print(product_num)
print(sum_digit)


# English: Reverse each word in a string.
# Hindi: String ke har shabd ko reverse karo.
string = 'hello world'
reverse = ''
result = ''

for char in string:
    if char != ' ':
        reverse += char
    else:
        result += reverse[::-1] + ' '
        reverse = ' '
result += reverse[::-1]
print(result)


# English: Find the second largest number in a list.
# Hindi: List mein doosra sabse bada number dhoondo.
list = [1, 2, 3, 4, 5, 6, 34, 2, 34, 54, 12]
largest = None
second_largest = None

for num in list:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        second_largest = num
print(second_largest)




# English: Check if a number is an Armstrong number.
# Hindi: Check karo ki ek number Armstrong number hai ya nahi.
num = int(input('enter you numer: '))
print('Armstrong' if sum([int(d)**3 for d in str(num)]) == num else 'numbers is not a Armstrong number')

temp = num
cube = 0
while num > 0:
    digit = num % 10
    outpute = digit ** 3
    cube += outpute
    num //= 10
if cube == temp:
    print('this is a armstrong number')
else:
    print('this is not a armstrong number')


# English: Calculate the sum of digits of a number until it becomes a single digit.
# Hindi: Ek number ke digits ka sum tab tak nikalo jab tak woh ek single digit na ban jaye.
while num > 9:
    num1 = sum([int(i) for i in str(num)])
print(num1)


# English: Find pairs of numbers in a list that sum up to a target value.
# Hindi: List mein aise number ke pairs dhoondo jinka sum target value ke barabar ho.
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"{nums[i]} and {nums[j]} is a perfect pairs")


# English: Check if a string is a palindrome.
# Hindi: Check karo ki ek string palindrome hai ya nahi.
string = 'level'
if string == string[::-1]:
    print(f'{string} is a prlingdrome')
else:
    print(f'{string} is not a prlingdrome')

print('pelingdrome' if string[::1] == string else 'not a pelingdrome')


# English: Count the number of even and odd digits in a number.
# Hindi: Ek number mein even aur odd digits ki sankhya gino.
n = 345602
odd = sum(1 for i in str(n) if int(i) % 2 != 0)
even = sum(1 for i in str(n) if int(i) % 2 == 0)
print(odd)
print(even)


odd1 = 0
even1 = 0

for i in str(n):
    if int(i) % 2 == 0:
        even1 += 1
    else:
        odd1 += 1
print(odd1)
print(even1)

# English: Count the number of vowels and consonants in a string.
# Hindi: Ek string mein vowels aur consonants ki sankhya gino.
name = 'sachin masti'
vovels = 'aioue'
vovels_count = 0
consonants = 0
for char in name:
    if char in vovels:
        vovels_count += 1
    elif char.isalpha():
        consonants += 1
print(vovels_count)
print(consonants)

# English: Reverse a number and check if it matches a target number.
# Hindi: Ek number ko reverse karo aur check karo ki woh target number se match karta hai ya nahi.
number = 548
target_num = 845
new_num = 0

while number > 0:
    digit = number % 10
    new_num = new_num * 10 + digit
    number //= 10
print(new_num)
if target_num == new_num:
    print('this is a my fav number ')
else:
    print("this is not a my fav number")
