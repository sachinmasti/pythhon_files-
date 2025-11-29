num = 405
sum_num = 0

for i in str(num):
    sum_num += int(i) **2

print(sum_num)

sum_n = sum([int(d)**2 for d in str(num)])
print(sum_n)


arry = [1,0,1,0,1,0]
arry = [-1 if x == 0 else x for x in arry]

arry=[1,-1,1,-1,1,-1]
prefix_sum = 0
hasmap = {0:-1}
max_len = 0

for i,num in enumerate(arry):
    prefix_sum+=num

    if prefix_sum in hasmap:
        max_len = max(max_len,i-hasmap[prefix_sum])
    
    else:
        hasmap[prefix_sum] = i

print(max_len)



name = 'sachin'
print(f'{name=}')