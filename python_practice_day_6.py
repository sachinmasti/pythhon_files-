# English: Check if a number is an Armstrong number.
# Hindi: जांचें कि कोई संख्या आर्मस्ट्रांग संख्या है या नहीं।
num = 153
cube = 0
tamp = num
check = 0

while num > 0:
    digit = num % 10
    check = digit **3
    cube += check
    num//=10
print(cube)
if cube == tamp:
    print(f"{tamp} is an armstrong number")
else:
    print(f"{tamp} is not an armstrong number")

# English: Armstrong number check using a list comprehension.
# Hindi: लिस्ट कॉम्प्रिहेंशन का उपयोग करके आर्मस्ट्रांग संख्या की जांच।
print('Armstrong' if sum([int(d)**3 for d in str(tamp)]) ==tamp else 'not a Armstrong')

# English: Reverse a number.
# Hindi: एक संख्या को उल्टा करें।
revers =0
num = 123 # Reset num for this example
while num> 0:
    d = num % 10
    revers = revers * 10 + d
    num //= 10
print(revers)

# English: Check if a number is a palindrome.
# Hindi: जांचें कि कोई संख्या पैलिंड्रोम है या नहीं।
n =121
if str(n) == str(n)[::-1]:
        print("this is a pelindrom number")
else:
        print('this is not a pelindrome number')

# English: Palindrome check using a one-liner.
# Hindi: एक लाइनर का उपयोग करके पैलिंड्रोम की जांच।
print('palindrome' if str(n) ==str(n)[::-1] else 'not a palindrome' )

# English: Alternative way to check for a palindrome.
# Hindi: पैलिंड्रोम की जांच करने का वैकल्पिक तरीका।
temp = n
new = 0
while n > 0:
    d =n % 10
    new =new * 10 + d
    n //=10
if new == temp:
    print(f'{new} 🤪this is a pelendrome')
else:
    print(f'{new} is not a prlingdrome')

# English: Count the number of odd and even digits in a number.
# Hindi: एक संख्या में विषम और सम अंकों की संख्या गिनें।
number = 1234567898
odd = sum(1 for i in str(number) if int(i) % 2!=0)
print(f"Number of odd digits: {odd}")

even = sum(1 for i in str(number) if int(i) %2==0)
print(f"Number of even digits: {even}")

# English: Generate and print the Fibonacci sequence.
# Hindi: फिबोनैकी अनुक्रम उत्पन्न और प्रिंट करें।
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
print("\nFibonacci sequence:")
fibonacci(10)
print()

# English: Find the largest digit in a number.
# Hindi: एक संख्या में सबसे बड़ा अंक खोजें।
n = 58341
second = 0
while n > 0:
    digit = n % 10
    if digit > second:
        second = digit
    n//=10
print(f"\nLargest digit: {second}")

# English: Check if a number is a Strong number.
# Hindi: जांचें कि कोई संख्या एक स्ट्रांग संख्या है या नहीं।
import math as m
num = 145
perfect = 0
temp= num
while num >0:
    d = num % 10
    perfect += m.factorial(d)
    num //= 10
if perfect == temp:
    print("this is a strong number")
else:
    print("this is not a strong number")

# English: Check if a number is a Harshad number.
# Hindi: जांचें कि कोई संख्या हर्षद संख्या है या नहीं।
num = 18
temp = num
sum_of_all =0
while num > 0:
    d = num % 10
    sum_of_all +=d
    num //=10
if temp % sum_of_all ==0:
    print(f'{temp} is a harshad number')
else:
    print(f"{temp} is not a harshad number")

sum_of_num = sum([int(i) for i in str(temp)])
print(f"Sum of digits: {sum_of_num}")

# English: Check if a number is an Automorphic number.
# Hindi: जांचें कि कोई संख्या ऑटोमॉर्फिक संख्या है या नहीं।
s = 153
sa =s **2
if str(sa).endswith(str(s)):
    print(f'{s} is a automorphic number')
else:
    print(f'{s} is not a automorphic number')

# English: Find and print all Automorphic numbers in the range 1 to 1000.
# Hindi: 1 से 1000 की सीमा में सभी ऑटोमॉर्फिक संख्याएँ खोजें और प्रिंट करें।
print("\nAutomorphic numbers from 1 to 1000:")
for i in range(1,1001):
    squar = i**2
    if str(squar).endswith(str(i)):
        print(i, end=" ")
print()

# English: Print the cube of numbers from 1 to 1000.
# Hindi: 1 से 1000 तक की संख्याओं का घन प्रिंट करें।
# print("\nCubes from 1 to 1000:")
# for i in range(1,1001):
#     print(i**3)

# English: Calculate factorial using recursion.
# Hindi: रिकर्सन का उपयोग करके फैक्टोरियल की गणना करें।
def factorial(n)-> int:
    if n ==1 or n ==0:
        return 1
    else:
        return n * factorial(n-1)
n = 10
print(f"\nFactorial of {n} is {factorial(n)}")

# English: Calculate factorial using an iterative approach with type hints.
# Hindi: टाइप हिंट के साथ एक पुनरावृत्ति दृष्टिकोण का उपयोग करके फैक्टोरियल की गणना करें।
def factorial_iterative(n: int) -> int:
  """Calculates the factorial of a non-negative integer."""
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

# Example usage:
print(f"Factorial of 5 is {factorial_iterative(5)}")

# English: Find and print all Armstrong numbers between 1 and 1000.
# Hindi: 1 और 1000 के बीच सभी आर्मस्ट्रांग संख्याएँ खोजें और प्रिंट करें।
print("\nArmstrong numbers between 1 and 1000:")
for i in range(1,1001):
    temp= i
    total = 0
    while temp > 0:
        d = temp % 10
        total+= d **3
        temp //=10
    if total == i:
        print(i, end=" ")
print()
