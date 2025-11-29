# English: Check if a string has balanced brackets.
# Hindi: Yeh code check karta hai ki string main brackets balanced hain ya nahi.
def is_balanced(string):
    stack = []
    opning = '([{' 
    closing = ')]} ' 
    pairs = {')':'(', ']':'[', '}':'{'}

    for i in string:
        if i in opning:
            stack.append(i)
        elif i in closing:
            if not stack or stack[-1] !=pairs[i]:
                return False
            stack.pop()
    return len(stack) ==0

# print(is_balanced('{[()]}'))

test_cases = [
    "{[()]}",
    "{[(])}",
    "((()))",
    "({[}])",
    "",
    "{[}",
]
print('='*50)
for test in test_cases:
    result = 'balanced' if is_balanced(test) else 'not balabnced'
    print(f'{test:15} --> {result}')
print('\n' + '='*50 +'\n')


# English: Remove duplicate characters from a string, preserving the original order.
# Hindi: Yeh code string se duplicate characters hatata hai, lekin order same rakhta hai.
def unique(s) -> str:
    new_s = '' 
    for i in s:
        if i not in new_s:
            new_s+=i
    return new_s

s= 'programming'
print(unique(s)) 

# English: Processes a list of numbers: doubles even numbers, adds 3 to odd numbers, and returns the total sum.
# Hindi: Yeh code ek list ke even numbers ko double aur odd numbers main 3 add karke, unka total sum batata hai.
def sum_all(n)->int:
    sum_lst = 0
    for i in n:
        if i % 2 ==0:
            sum_lst += i *2
        else:
            sum_lst += i +3
    return sum_lst

lst:list = [2,3,4,5,6,7,8,9,10]
print(sum_all(lst))

# English: Counts the number of times a value in a list is greater than the previously recorded maximum value.
# Hindi: Yeh code list mein count karta hai ki kitni baar ek value pichli maximum value se badi hai.
def increasing_pairs(l) -> int:
    start = l[0]
    count= 0
    for i in range(1,len(l)):
        if start < l[i]:
            count +=1
            start = l[i]
    return count

l = [1, 3, 2, 5, 4, 6]

print(increasing_pairs(l))


# English: Counts the number of adjacent pairs in a list where the second element is greater than the first.
# Hindi: Yeh code list mein adjacent pairs ko count karta hai jahan second element first se bada hota hai.
def sachin(v) -> int:
    count = 0
    for i in range(1,len(v)):
        if v[i-1] < v[i]:
            count+=1
    return count

print(sachin(l))