
# English: This code doubles each number in the list.
# Hindi: Yeh code list mein har number ko double karta hai.
nums = [10, 20, 30, 40, 50]
new_nums =[i*2 for i in nums]
print(new_nums)

# English: This code counts the number of vowels in a string.
# Hindi: Yeh code ek string mein vowels ki sankhya ginta hai.
text = "python is awesome"
vowels ='aeiou'
# v=sum([char in vowels for char in text])
v = sum([char in vowels for char in text])
print(v)
v1 = 0
for char in text:
    if char in vowels:
        v1+=1
print(v1)

# English: This code checks if a number is a strong number.
# Hindi: Yeh code check karta hai ki koi number strong number hai ya nahi.
import math as m
num =int(input('enter your number'))
temp = num
strong =0
for i in str(num):
    strong+=m.factorial(int(i))
if strong == num:
    print('this is a strong number')
else:
    print('this is a not a strong number')

# English: This code calculates the LCM of two numbers for a limited time.
# Hindi: Yeh code do numbers ka LCM nikalta hai, lekin ek seemit samay ke liye.
import math as m
import time
num1 = int(input('enter your number: '))
num2 = int(input('enter your number: '))

start_time = time.time()
while num1 > 0:     # English: The loop will run for a maximum of 10 seconds.
     # Hindi: Loop 10 second tak chalega.
     if time.time() - start_time > 10:
         print("Loop finished after 10 seconds.")
         break
     lcm = (num1 * num2) / m.gcd(num1 , num2)
     print(int(lcm))

# English: This code removes duplicate elements from a list.
# Hindi: Yeh code list se duplicate elements ko hatata hai.
l =[1,2,2,3,4,5,6,2,3,4,5,67,5,4,343,56,67]
print(list(dict.fromkeys(l)))