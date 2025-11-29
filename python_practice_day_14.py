
name = 'success'
checks = {}

for value in name:
    if value in checks:
        checks[value]+=1
    else:
        checks[value]=1
        

print(value)
print(checks)

c1 ={}
for value in name:
    c1[value] = c1.get(value, 0) + 1

print(c1)

# Input: "aabbccdeff"
# Output: "d"

char :str = 'aabbccdeff'

freq : dict = {}

for ch in char:
    freq[ch] = freq.get(ch,0)+1

for key , value in freq.items():
    if value ==1:
        print(key,value)
        break


nums = [2, 7, 11, 15]
target = 9
hashmap = {}

for i,n in enumerate(nums):
    diff = target - n
    if diff in hashmap:
        print(hashmap[diff],i)
        break
    hashmap[n] = i


def findNb(m):
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1

m = 36
print(findNb(m))
