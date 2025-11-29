
# English: This function finds the last non-repetitive character in a string.
# Hindi: Yeh function ek string mein antim non-repetitive character ko dhoondhta hai.
def my_func(s: str) -> str:
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i,0)+1
    for j in reversed(s):
        if hashmap[j] ==1:
            return j
    return ''
print(my_func('abaccdeff'))


# English: This function counts the number of times a digit is smaller than the preceding digit in a number.
# Hindi: Yeh function ginta hai ki ek sankhya mein kitni baar ek ank pichle ank se chhota hai.
def decrease(n:int) -> int:
    count = 0
    str_n = str(n)
    for i in range(1,len(str_n)):
        # print(str(n)[i])
        if str_n[i] < str_n[i-1]:
            count+=1
    return count

print(decrease(97531))


# English: This function finds all consecutive sequences of even numbers in a list.
# Hindi: Yeh function ek list mein even numbers ke sabhi lagatar sequences ko dhoondhta hai.
def even_sequence(l:list) -> list:
    new_l =[]
    current_list = []
    for i in range(len(l)):
        if l[i] % 2==0:
            current_list.append(l[i])
        
        else:
            if len(current_list) >= 2:
                new_l.append(current_list)
            current_list = []
    if len(current_list) >= 2:
        new_l.append(current_list)
    print(len(new_l))
    return new_l

print(even_sequence([2,4,5,6,8,10,3,12,14]))
