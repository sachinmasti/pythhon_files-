# English: Calculates the product of all even digits in a given number.
# Hindi: Diye gaye number mein sabhi even digits ka product (gunanphal) nikalta hai.
def even_num_pro(n) -> int:
    count = 1
    even_num = []
    while n>0:
        d= n % 10
        if d % 2==0:
            even_num.append(d)
        n //= 10
    
    if len(even_num) ==0:
        return 0
    for i in range(len(even_num)):
        count *= even_num[i]
    return count

print(even_num_pro(48271))


# English: Counts the number of pairs in a list whose sum is an even number.
# Hindi: List mein un jodo (pairs) ki sankhya ginta hai jinka yog (sum) ek even number hai.
def even_pairs(l) -> int:
    count = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if  (l[i] + l[j]) % 2 ==0:
                count+=1
    return count

print(even_pairs([1,2,3,4,5,6]))


# English: Counts the number of vowels and consonants in a given string.
# Hindi: Diye gaye string mein vowels aur consonants ki sankhya ginta hai.
def vowels_counts(s:str) -> int:
    vowels = 'aeoui'
    count_vowels = 0
    consonant  = 0
    for i in s.lower():
        if i.isalpha():
            if i in vowels:
                count_vowels +=1
            else:
                consonant+=1
    return count_vowels,consonant

print(vowels_counts('hi my name is sachin and my fav person is veena❣️'))
