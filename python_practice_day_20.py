# English: Defines a list of integers for demonstration purposes.
# Hindi: Yeh code demonstration ke liye integers ki ek list banata hai.
lst : list =  [1, 3, 2, 5, 4, 10, 8]

# English: Counts the number of 'peaks' in a list, where a peak is an element greater than its immediate neighbors.
# Hindi: Yeh code list mein 'peaks' ko count karta hai, jahan ek peak apne padosi elements se bada hota hai.
def count_peaks(l) -> int:
    count = 0
    for i in range(1,len(l) -1):
        # print(i)
        if l[i] > l[i-1] and l[i] > l[i+1]:
            count+=1
    return count

print(count_peaks(lst))

# English: Initializes colorama to add colored text to the terminal output.
# Hindi: Yeh code terminal output mein rangin text jodne ke liye colorama ko initialize karta hai.
from colorama import Fore,Style,init
init(autoreset=True)

print(f'{Fore.LIGHTCYAN_EX} this is a new program')

# English: Counts the number of adjacent pairs in a list that have alternating parity (odd/even or even/odd).
# Hindi: Yeh code list mein aise adjacent pairs ko count karta hai jinki parity alag-alag ho (odd/even ya even/odd).
def alternative (l) ->int:
    count = 0
    for i in range(len(l)-1):
        if (l[i] % 2 !=0 and l[i+1] % 2 ==0)or\
            (l[i] % 2==0 and l[i+1] % 2 != 0 ):
            count +=1
    return count

print(alternative(lst))

# English: Counts the number of 'valleys' in a list, where a valley is an element smaller than its immediate neighbors.
# Hindi: Yeh code list mein 'valleys' ko count karta hai, jahan ek valley apne padosi elements se chota hota hai.
def valleys(l) ->int:
    count= 0
    for i in range(1, len(l) - 1):
        if l[i] < l[i-1] and l[i] < l[i+1]:
            count +=1
    return count

print(f'{Fore.LIGHTYELLOW_EX} {valleys(lst)}')


# English: Defines a new list for the next function.
# Hindi: Agle function ke liye ek nayi list define ki gayi hai.
l = [1, 2, 3, 2, 4, 5]

# English: Counts the number of continuous increasing sequences in a list.
# Hindi: Yeh code list mein lagatar badhne wale sequences ki sankhya count karta hai.
def increase(l) -> int:
    count = 0
    flag = False
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            if not flag:
                count+=1
                flag = True
        else:
            flag = False
    return count

print(increase(l))
