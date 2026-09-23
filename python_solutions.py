numbers =  input().split(',')
res=[]
for i in numbers:
    dec = int(i,2)
    if dec%5==0:
        res.append(i)
print(','.join(res))


// 2nd Question


numbers = input().split(',')
res = []

for n in numbers:
    fact = 1
    for i in range(1, int(n) + 1):
        fact *= i
    res.append(str(fact))

print(','.join(res))


// 3rd Question 

s = input()
letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)


