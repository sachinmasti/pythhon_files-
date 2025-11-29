# Input → 12345  
# Output → Number of digits: 5

n =12345
c = 0
while n > 0:
    n //=10
    c+=1
print(c)



n =12345
r =0
while n > 0:
    digit = n%10
    r= (r * 10) + digit
    n //=10
print(r)


n =121
p =0
t =n
while n > 0:
    digit = n%10
    p= (p * 10) + digit
    n //=10

if t == p:
    print('this is a pelindrom number')
else:
    print('this is not a pelindrom number')






if str(n) ==str(n)[::-1]:
    print('this is a pelindrome number')
else:
    print('this is not a pelingdrom number')

n =153
temp = n
Output =0
while n>0:
    digit =n%10
    cube = digit **3
    Output+=cube
    n //=10

print(Output)
if temp == Output:
    print('thsi is a Armstrong number ')
else:
    print('this is a not a Armstrong number')


n = 153
digits = [int(d) for d in str(n)]     # string se har digit liya
cube_sum = sum([d**3 for d in digits])
print(cube_sum)
n = int(input('enter your number: '))
print('Armstrong' if sum([int(d)**3 for d in str(n)]) == n else 'not a Armstrong')




# Input: 9875  
# Step 1: 9 + 8 + 7 + 5 = 29  
# Step 2: 2 + 9 = 11  
# Step 3: 1 + 1 = 2  
# Output: 2

n = 12346
while n > 9:
    p =0
    while n > 0:
     digit = n % 10
     p = p + digit
     n //=10
    n = p
print(n)

while n > 0:
    num =sum([int(d) for d in str(n)])
print(num)



# Input → 34561  
# Output → Even = 2, Odd = 3
 
sachin = 34561
odd =0
even =0
while sachin >0 :
    digit = sachin %2 ==0
    if digit:
        even+=1
    else:
        odd+=1
    sachin //=10
print(even,odd)

sachin = 34561
odd =sum([1 for d in str (sachin) if int(d) %2!=0])
even =sum([1 for d in  str (sachin) if int(d) %2==0])
print(odd,even)

number2 =5
# while number2 < 0:
#     fact = number2 *(number2-1)
# print(fact)
result =1
import math as m
for i in range(1,number2+1):
    result *= i
    factorial = m.factorial(i)
print(result)
print(factorial)

factorial1 =m.prod([n for n in range(1,number2+1)])
print(factorial1)



# Input → 1234  
# Output → (4¹ + 3² + 2³ + 1⁴) = 4 + 9 + 8 + 1 = 22

num = 1234
output = 0
p = 1

while num > 0:
    d = num % 10
    output +=d ** p
    p +=1
    num //= 10
print(output)


num = 1234
output = 0
pos = 1

while num > 0:
    d = num % 10
    output += d ** pos   # har digit ^ position
    pos += 1             # position badhao
    num //= 10           # last digit hatao
print(output)



number = 6
sum_of_all =0


for i in range(1,number):
    if number % i ==0:
        sum_of_all +=i
if sum_of_all == number:
    print(f'{number} is a perfect number')
else:
    print(f'{number} is not a perfect number')

perfect =sum([i for i in range(1, number) if number % i ==0])
print(f'{number} is a perfect number')


row = 7
for i in range(row,0,-1):
    print(' '* (row -i-1), '*' * (2*i-1))

for i in range(row):
    print(" " *(row - i- 1), "*" * (2 * i + 1))

for i in range(row):
    space =" " *(row - i- 1)
    star = "*" * (2 * i + 1)
    print(space,star)