# perfect number ka problem 

num = 6
num_list1 = sum([i for i in range(1,num) if num % i ==0])
print(num_list1)

num_list = 0
for i in range(1,num):
    if num % i == 0:
        num_list += i
if num == num_list:
    print('this is a perfect number')
else:
    print('this is not a perfect number')


# strong number ka problem 

import math as m
num1 = 146
temp = num1
all_sum = 0
while num1 > 0:
    # print(num1)
    d = num1 % 10
    all_sum += m.factorial(d)
    num1//=10
if temp == all_sum:
    print(f'{temp} is a strong number')
else:
    print(f'{temp} is not a strong number')

sachin = sum([m.factorial(int(i)) for i in str(temp)])

from colorama import Fore,Style,init
init(autoreset=True)
if temp == sachin:
    print(f'{temp} {Fore.GREEN}is a strong number')
else:
    print(f'{Fore.RED} {temp} {Style.RESET_ALL} is not a strong number')

number = 9875
tempt_num = number
# result =  0 

while number > 9:
    result =0
    while number > 0:
        d = number % 10
        result = result+d
        number //=10
    number = result
print(result)
 
while number > 9:
    number = sum(int(d) for d in str(number))
print(number)

n1 = 36
n2 = 60
com_div = []
for i in range(1,min(n1,n2)+1):
        if n1 % i ==0 and n2 % i ==0:
            com_div.append(i)
            div_gcd = i
print('gcd list', com_div)
print('gcd is', max(com_div))
print('gcd is', div_gcd)


n1 = 4
n2=6
lcm = (n1*n2) / m.gcd(n1,n2)
print(lcm)


for i in range(1,11):
    print(i)
else:
    print('hi')