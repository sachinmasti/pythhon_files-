num = 123
cube = sum([int(d)**3 for d in str(num) ])
print(cube)

string = 'sachin masti'
vovels = 'aeiou'
consonant = 0
count_vowels = 0

for char in string:
    if char.isalpha():
        if char.lower() in vovels:
            count_vowels +=1
        else:
            consonant +=1
print(f'{count_vowels=}')
print(f'{consonant=}')


lst =  [1, -1, 3, 2, -2, -8, 1, 7, 10, 23]

prefix_sum = 0
hashmap = {0:-1}
max_len = 0

for i , n in enumerate(lst):
    prefix_sum+=n

    if prefix_sum in hashmap:
        max_len = max(max_len,i-hashmap[prefix_sum])
    
    else:
        hashmap[prefix_sum] =i 
    
print(max_len)