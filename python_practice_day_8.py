# English: Loop from 1 to 100. If the number is divisible by both 3 and 5, print 'FizzBuzz'.
# Hindi: 1 se 100 tak loop karein. Agar number 3 aur 5 dono se divisible hai, to 'FizzBuzz' print karein.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    # English: If the number is divisible by 3, print 'Fizz'.
    # Hindi: Agar number 3 se divisible hai, to 'Fizz' print karein.
    elif i % 3 == 0:
        print('Fizz')
    # English: If the number is divisible by 5, print 'Buzz'.
    # Hindi: Agar number 5 se divisible hai, to 'Buzz' print karein.
    elif i % 5 == 0:
        print('Buzz')
    # English: Otherwise, print the number.
    # Hindi: Nahi to, number print karein.
    else:
        print(i)

# English: A more compact way to write FizzBuzz using boolean multiplication.
# Hindi: FizzBuzz likhne ka ek chhota tarika boolean multiplication ka use karke.
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

# # English: Checks if a number is a palindrome by comparing the number with its reverse.
# # Hindi: Check karta hai ki koi number palindrome hai ya nahi, number ko uske reverse se compare karke.
# num = int(input('enter your number: '))
# if str(num)[::-1] == str(num):
#     print('this is a palindrome')
# else:
#     print('this is not a palindrome')

# English: Counts the number of even and odd numbers from 1 to 10.
# Hindi: 1 se 10 tak ke even aur odd numbers ki sankhya ginta hai.
odd, even = 0, 0
for i in range(1, 11):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# English: Reverses a given integer.
# Hindi: Diye gaye integer ko reverse karta hai.
num = 1234
ew_num = 0
while num > 0:
    d = num % 10
    ew_num = (ew_num * 10) + d
    num //= 10
print(ew_num)

# English: Calculates the sum of the digits of a given number.
# Hindi: Diye gaye number ke digits ka sum calculate karta hai.
n = 518
sum_n = 0
while n > 0:
    d = n % 10
    sum_n += d
    n //= 10
print(sum_n)

# English: Checks if a number is an Armstrong number (sum of cubes of digits equals the number).
# Hindi: Check karta hai ki koi number Armstrong number hai ya nahi (digits ke cube ka sum number ke barabar hota hai).
number = 153
temp = number
total = 0
while number > 0:
    d = number % 10
    total += d ** 3
    number //= 10
if temp == total:
    print(f'{temp} is an Armstrong number')
else:
    print(f'{temp} is not an Armstrong number')

# English: Checks if a number is a perfect number (sum of its proper divisors equals the number).
# Hindi: Check karta hai ki koi number perfect number hai ya nahi (uske proper divisors ka sum number ke barabar hota hai).
num1 = 6
perfect = 0
for i in range(1, num1):
    if num1 % i == 0:
        perfect += i
if perfect == num1:
    print(f'{num1} is a perfect number')

# English: Checks if a number is prime by counting its divisors.
# Hindi: Divisors ko ginkar check karta hai ki koi number prime hai ya nahi.
num = 7
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

# English: An optimized prime number check, looping up to half the number.
# Hindi: Ek behtar prime number check, number ke aadhe tak loop karke.
if num > 1:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

# English: The most optimized prime check, looping up to the square root of the number.
# Hindi: Sabse behtar prime check, number ke square root tak loop karke.
import math as m
if num > 1:
    for i in range(2, int(m.sqrt(num)) + 1):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')

# English: Finds the middle character(s) of a user-input string.
# Hindi: User-input string ke beech ka character(s) dhundhta hai.
name = input('enter your name: ')
length = len(name)
mid = length // 2
print(mid)
if length % 2 == 0:
    print(name[mid - 1:mid + 1])
else:
    print(name[mid])


