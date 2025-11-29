lst = [1,2,3,4,5,5,67,87,76]
target = 3
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i],lst[j],'is a perfect combo')


num = 120
k =1
roteted_num = str(num)
new_num1 = roteted_num[-k:] + roteted_num[:-k]
print(new_num1)

if int(new_num1) % num == 0:
    print(True)
else:
    print(False)



s = 101090
k = 3

# ye line numbers ko original form main lane ke liye hai
sign = -1 if s < 0 else 1

# ye line number ko string main convert karata hai
str_s = str(s)

# ye line k ka reminder leta hai taki agar k > ho nubmer se to uss ko k ke reminder se reverse karne main asani ho
k = k% len(str_s)

# ye num ko reverse karne ke liye hai
ulta = str_s[-k:] + str_s[:-k]

# ye line se number ko integer main convert karata hai aur uss ko original form main lata hai
ulta_num = int(ulta) *sign

# ye nubmer ko check karta hai kya wo reverse nubmer se divisible hai 
if ulta_num % s ==0:
    print(True)
else:
    print(False)


# Input:
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print('this is a anagrams')
else:
    print('this is not a anagram')
