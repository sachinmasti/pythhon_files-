# English: Counts the number of unique digits in a given number.
# Hindi: Diye gaye number mein unique digits ki sankhya ginta hai.
def count_unique_num(l) ->int:
    nums = []
    for i in str(l):
        if int(i) not in nums:
            nums.append(int(i))
    return len(nums)


print(count_unique_num(11122233377))

# English: Reverses the order of words in a given string.
# Hindi: Diye gaye string mein shabdon ka kram ulat deta hai.
def reverse_word_order(s: str) -> str:
    words = []
    word = ""
    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)

    res = ""
    for i in range(len(words)-1, -1, -1):
        res += words[i]
        if i != 0:
            res += " "
    return res

print(reverse_word_order("hello world python"))


# English: Counts the number of times an element in a list is greater than its preceding element.
# Hindi: Ek list mein kitni baar ek tatva apne pichle tatva se bada hai, uski gannna karta hai.
def sunflower(l) -> int:
    count = 0
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            count += 1
    return count

print(sunflower([1, 4, 3, 6, 7, 2]))


# English: Reverses the order of words in a given string using a more concise method.
# Hindi: Diye gaye string mein shabdon ka kram ulat deta hai, ek sankshep vidhi ka upyog karke.
def reverse_word_order(s):
     return " ".join(s.split()[::-1])
print(reverse_word_order("hello world python"))



def sachin(s) -> str:
    words = []
    word = ''
    for ch in s:
        if ch !=' ':
            word+=ch
        else:
            if word != '':
                words.append(word)
                word = ''
    if word !='':
        words.append(word)
    
    re = ''
    for i in range(len(words)-1,-1,-1):
        re += words[i]
        if i !=0:
            re+= ' '
    return re

print(sachin('my name is sachin'))