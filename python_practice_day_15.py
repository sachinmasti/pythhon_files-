# Input: [10, 5, 8, 2, 7]
# Output: 18 - 7 = 11

lst = [10,5,8,2,7]

odd = 0
even = 0

for i,n in enumerate(lst):
    if i %2==0:
        even+=n
    else:
        odd+=n
print(even - odd)

num = 112233
dict1 = {}

for value in str(num):
    dict1[value] = dict1.get(value,0)+1
print(dict1)

dict2 = {}
for value in str(num):
    if value in dict2:
        dict2[value]+=1
    else:
        dict2[value]=1
print(dict2)

num = 112233
from collections import Counter

count = Counter(str(num))
print(dict(count))


# Input:  "aabbcaa"
# Output: "a1a2b1b2c1a3a4"

string = 'aabbcaa'
new_str = ""
char_counts = {}

for i in string:
    print(i)
    char_counts[i] = char_counts.get(i, 0) + 1
    new_str += i + str(char_counts[i])

print(new_str)
print(char_counts)
print(str(char_counts))
