# English: Counts the number of vowels in a given string, ignoring case.
# Hindi: Yeh code diye gaye string mein vowels (svar) ki ginti karta hai, case ko ignore karte hue.
def vowels(s) -> int:
    v = 'aioue'
    count = 0
    for i in s:
        if i.isalpha():
            if i.lower() in v:
                count += 1
    return count

s:str = ' sachin masti'
print(vowels(s))


# English: Counts the number of words in a string, where words are separated by spaces.
# Hindi: Yeh code ek string mein shabdo ki ginti karta hai, jahan shabd spaces se alag hote hain.
def word_count(s) -> int:
    count = 0
    check = False
    for i in s:
        if i !=' ':
            if not check:
                count+=1
                check = True
        else:
            check = False
    return count

print(word_count(s))

# English: Counts the number of words in a camelCase string.
# Hindi: Yeh code camelCase string mein shabdo ki ginti karta hai.
def camel_words(s) -> int:
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count

s= 'myNameIsSachin'
print(camel_words(s))

# English: Counts groups of consecutive identical characters in a string.
# Hindi: Yeh code ek string mein lagatar aane wale identical characters ke groups ko ginta hai.
def count_groups(s) -> int:
    count = 1
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            count+=1
    return count

s:str = 'aaabbbaaacccddaa'
print(count_groups(s))
