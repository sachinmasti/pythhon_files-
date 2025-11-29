# This dictionary maps month names to their corresponding numbers.
# d = {'juanvery':1,
#     'feb':2,
#         'march':3,
#             'april':4,
#                 'may':5,
#                     'june':6,
#                         'july':7,
#                             'august':8,
#                                 'september':9,
#                                     'october':10,
#                                         'november':11,
#                                             'december':12}

# This code prompts the user to enter a month number and then prints the corresponding month name.
# n = int(input('enter your month number: '))

# for month , num in d.items():
#     if n == num:
#         print('this is a month:', month)
'''

# This code demonstrates a for loop with a continue statement.
a = 5
for i in range(a):
    if a ==3:
        continue
    print(a)

# This function removes trailing zeros from a string.
def sachin(v) -> str:
    if v =='0':
        return '0'
    else:
        return v.rstrip("0")
    


a = "0"
print(sachin(a))

# This code finds the maximum sum of a contiguous subarray.
a = -1,2,-3,4,-5,6,8,9,-9
def sum_all(a):
    max_sum = current_sum = 0
    for num in a:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
print(sum_all(a))

    
# This code counts the number of vowels and consonants in a string.
w  = 'hello world'
vowels = 'aeiou'
v= 0
c = 0

for char in w.lower():
    if char in vowels:
        v+=1
    elif char.isalpha():
        c+=1
print(v)
print(c)



# This code counts the number of multiples of 3, 5, and both 3 and 5 up to a given number.
# Input
n = int(input("Enter a number: "))

# Counters
count_3 = 0
count_5 = 0
count_both = 0

# Loop through numbers
for i in range(1, n + 1):
    # Check if i is multiple of both 3 and 5

    # Fill logic here 👇
     if i % 3 == 0 and i % 5 == 0:
        count_both += 1
    
    # Check if i is multiple of 3
    # Fill logic here 👇
     if i % 3 ==0:
        count_3 += 1
    

    # Check if i is multiple of 5
    # Fill logic here 👇
     if i% 5 == 0:
        count_5 += 1
    

# Print results
print("Multiples of 3:", count_3)
print("Multiples of 5:", count_5)
print("Multiples of both 3 and 5:", count_both)


# This code prints the first half of a string.
w = 'hello world'
s = len(w) //2
ws = w[:s]
print(ws)


# This code checks if a number is prime.
n = int(input('enter your number: '))
is_prime = True
 
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n>1:
        print(n ,'prime')
else:
        print(n ,'not prime')

        '''

'''
🧩 Problem 1: First Non-Repeating Character

Description:
Tumhe ek string s di gayi hai. Tumhe pehla character return karna hai jo sirf ek baar appear hua ho.
Agar sab characters repeat ho rahe hain, to "None" return karo.

Input: s = "swiss"
Output: "w"

Input: s = "aabbcc"
Output: None

'''

# This code finds the first non-repeating character in a string.
s = 'sachin'
for i in s:
    if s.count(i) == 1:
        print(i)
        break
else:
    print('none')


# This code counts the frequency of each character in a string.
n = {}
for ch in s:
    if ch in n:
        n[ch]+=1
    else:
        n[ch] = 1
print(n)


# This code calculates the sum of even numbers in a list.
lst =[12,3,4,5,6,7,8,9]
new_lst = 0
for i in lst:
    if i %2==0:
        new_lst +=i
print(new_lst)

# This code calculates the sum of even numbers at even indices in a list.
lst =[12,3,4,5,6,7,8,9]
even_sum = 0
for i in range(len(lst)):
    if i%2 ==0:
        if lst[i] %2==0:
            even_sum+= lst[i]
print(even_sum)


# This code counts the number of odd numbers in a list.
lst1 = [2, 5, 7, 8, 9, 10]
# Output: 3   # (5, 7, 9)
no_count = 0
for i in  lst1:
    if i%2!=0:
        no_count +=1
    
print(no_count)


# This code creates a new list containing numbers from the original list that are between 5 and 10.
lst = [2, 5, 7, 8, 12, 10, 6]
# Output: 3   # (7, 8, 6)
new_lst =[]
for i in lst:
    if i > 5 and i < 10:
        new_lst.append(i)
print(new_lst)


# This code doubles the odd numbers in a list.
lst = [4, 7, 10, 13, 16, 19, 20]
new_lst = []
for i in lst:
    if i % 2 != 0:
        i*= 2
        new_lst.append(i)
print(new_lst)

# This code does the same thing as the previous code block, but using a list comprehension.
new_lst1 =[i * 2 for i in lst if i % 2 != 0]
print(new_lst1)

# This code converts all vowels in a string to uppercase.
string = 'hello world!'
v = 'aeiou'


new_str = []
for i in string:
    if i in v:
        new_str.append(i.upper())
    else:
        new_str.append(i)
    
result = ''.join(new_str)
print(result)


# This is another way to do the same thing as the previous code block.
new_str = []
for i in string:
    if i in v:
        new_str.append(i.upper())
    else:
        new_str.append(i)
final_string = ''.join(new_str)
print(final_string)

# This is a more concise way to do the same thing using a list comprehension.
last =''.join([i.upper() if i in v else i for i in string])
print(last)


# This code counts the number of digits in a number.
num =1234567890
count_num = 0
while num > 0:
    num = num // 10
    count_num+=1
print(count_num)


def sum_of_digits(n):
    n = abs(n)         # negative number handle
    total = 0
    while n > 0:
        digit = n % 10     # last digit nikala
        total += digit     # usse total me add kiya
        n //= 10           # ek digit kam kiya
    return total

print(sum_of_digits(50293))   # Output: 19


num =12345
if num < 0:
    print(int(str(abs))[::-1])
else:
    print(int(str(num)[::-1]))

reverse  = 0

while num > 0:
    last_num = num % 10
    reverse = reverse * 10 + last_num
    num //= 10
print(reverse)




num =121
rev = int(str(num)[::-1])
if num == rev:
    print(True)
else:
    print(False)


num =12345678901
sum_of_all_odd_num = 0
sum_of_all_even_num = 0

while num > 0:
    last_num = num % 10
    if last_num %2 ==0:
        sum_of_all_even_num += last_num
        # num //= 10
    else:
        sum_of_all_odd_num+= last_num
    num //=10
print(sum_of_all_even_num)
print(sum_of_all_odd_num)


row = 9
for i in range(row):
    print("-"  * (row - i - 1), "*" * (2*i-1))



num = 1234


sum_num = sum(int(digit) for digit in str(num))
print(sum_num)

# while num > 0:
    

num = int(input('enter your number: '))

is_prime = True

for i in range(2,int(num ** 0.5) +1):
    if num % i == 0:
        is_prime = False
        break
print(f'{num} is prime: {is_prime}')


def fib(n) -> int:
    if n ==0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 20
for i in range(n):
    print(fib(i), end = ' ')

def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n -1)

n = 10
print(fact(n))