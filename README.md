# HCL Manual Testing 


### QA Test Report 

* [Google XL Sheet](https://docs.google.com/spreadsheets/d/17K54A8W3J65E3hJ5q54dAt9aPQHAWz-VWDVJylRowG0/edit?gid=0#gid=0)   -- Click Here


### Jira Tool Team Link

* [Jira](https://rdxsworkspace-41553692.atlassian.net/jira/software/projects/KRG/summary)  -- Click Here


### Task TestCase (22.09.2026)

* [Google XL Sheet](https://docs.google.com/spreadsheets/d/17K54A8W3J65E3hJ5q54dAt9aPQHAWz-VWDVJylRowG0/edit?gid=1680199310#gid=1680199310)  -- Click Here

### Python Code (23.09.2026)

- *1 Question*

```python
numbers =  input().split(',')
res=[]
for i in numbers:
    dec = int(i,2)
    if dec%5==0:
        res.append(i)
print(','.join(res))
```

 - *2 Question*

```python
numbers = input().split(',')
res = []

for n in numbers:
    fact = 1
    for i in range(1, int(n) + 1):
        fact *= i
    res.append(str(fact))

print(','.join(res))
```

- *3 Question*

```python

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
```
