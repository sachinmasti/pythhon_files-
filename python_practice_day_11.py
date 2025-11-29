string = 'hello world'

vovels = 'aeiou'

v = 0
c = 0
for i in string:
    if i.isalpha():
        if i.lower() in vovels:
                v+=1
        else:
                c+=1
print(f'vovels are {v} and consonants are {c}')


num = 6
sum_num = []

for i in range(1,num):
    if num % i ==0:
        sum_num.append(i)
if sum(sum_num) == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')
# print(sum_num)

new_sum = sum([i for i in range(1,num) if num % i ==0])
print(new_sum)


str1 = "python"
str2 = "notepad"
comon = set(str1).intersection(set(str2))
print(comon)
print(list(set.intersection(set(str1),set(str2))))

from colorama import Fore,Style,init
init(autoreset=True)

def count_vovels(s:str):
    vovels = 'aeiou'
    vowels_count = 0
    consonants = 0 
    for ch in s:
        if ch.isalpha():
            if ch.lower() in vovels:
                vowels_count+=1
            else:
                consonants +=1
    return vowels_count,consonants

def perfect_number(n: int):
    if sum([i for i in range(1, n) if n % i == 0]) == n:
        print(Fore.CYAN + f"{n} is a perfect number")
    else:
        print(Fore.RED + f"{n} is not a perfect number")

def common_alpha(s1: str, s2: str):
    common = list(set(s1).intersection(set(s2)))
    print(Fore.MAGENTA + f"Common letters: {common}")

str1 = "beautiful"
str2 = "table"

vowels_count, consonants = count_vovels(str1)
print(Fore.GREEN + f"Vowels: {vowels_count}, Consonants: {consonants}")

# ✅ Pass vowel count to perfect number checker
perfect_number(vowels_count)

# ✅ Find common letters
common_alpha(str1, str2)