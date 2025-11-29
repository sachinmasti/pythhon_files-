# Find the middle character of a string.
s = 'sachin'

length  = len(s)
mid = length // 2

if mid % 2== 0:
    print(s[mid-1:mid+1])
else:
    print(s[mid])


# Remove consecutive duplicate characters from a string.
# Input → "aabbccddaa"
# Output → "abcd a" → final string "abcda"

string = 'aabbccddaa'

new_str = ''

for i in string:
    if new_str == "":
        new_str+=i
    elif new_str[-1] == i:
        continue
    else:
        new_str+=i
print(new_str)

# Count even and odd digits in a number.
n = 58340
odd = sum(1 for i in str(n) if int(i) % 2 != 0)
even = sum(1 for i in str(n) if int(i) % 2==0)

print(odd)
print(even)

o = 0
e = 0
while n>0:
    d = n%10
    if d % 2==0:
        e +=1
    else:
        o+=1
    n//=10
print(o)
print(e)

# Find the first non-repeated character in a string.
char = 'swiss'
hashmap = {}

for i in char:
    hashmap[i] = hashmap.get(i,0)+1

for j in hashmap:
    if hashmap[j] == 1:
        print(j)
        break

# Find two numbers in a list that sum up to a target value (Two Sum problem).
lst = [2,7,11,20]
target = 9

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] ==target:
            print(lst[i],lst[j])
