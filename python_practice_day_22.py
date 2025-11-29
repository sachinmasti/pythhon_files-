# English: Counts the number of even digits in a given integer.
# Hindi: Diye gaye integer mein even digits ki sankhya ginta hai.
def even_count(n) -> int:
    even_num = 0
    even = list(int(d) for d in str(n) if int(d) % 2 ==0)
    print(len(even))
    for i in str(n):
        if int(i) % 2 ==0:
            even_num += 1
    return even_num

num = 48217
print(even_count(num))

# English: Counts the number of adjacent vowels in a string.
# Hindi: Ek string mein aasann vowels ki sankhya ginta hai.
def vowel_count(s) -> int:
    count = 0
    vowels = 'aeiou'
    for i in range(1,len(s)):
        if s[i] in vowels and s[i-1] in vowels:
            count += 1
            print(s[i],s[i-1])
    return count

s= 'beautiful'
print(vowel_count(s))

# English: Counts the number of strictly increasing sequences of three consecutive elements in a list.
# Hindi: Ek list mein lagatar teen tatvon ke sakhti se badhte kram ki sankhya ginta hai.
def sequence(l) -> int:
    count = 0
    for i in range(len(l)-2):
        if l[i] < l[i+1] < l[i+2]:
            count += 1
    return count

l = [1,3,2,5,7,6,8]
print(sequence(l))






from colorama import Fore,Style,init
init(autoreset=True)

import time
while True:
    try:
        num = input('enter your number: ')
        if not num:
            print(f'{Fore.LIGHTRED_EX} your numver is a invalid')
            break
        num = int(num)

        start = time.time()

        if num <=1:
            print('this is not a prime number')

        elif num ==2 :
            print('num is a prime number')

        elif num % 2 ==0:
            print('this is a not a prime number')

        else:
            for i in range(3,int(num**0.5)+1,2):
                if i % 2 ==0:
                    print(f'{num}is a not a prime number')
                    break
            else:
                print(f'{num} is a prime number')

        end = time.time()
    except ValueError:
        print(f'your  number {num} is not a valid number')
        continue
    except KeyboardInterrupt:
        print(f'{Fore.CYAN}\nyour program is exit')
        break
    print((start - end),'is a time taken by code')



