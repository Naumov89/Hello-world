##################################### V1

s = ['a', 'b', 'c', 'd', 'e']
i = 0
for show in s:
    new = s[i]
    new = new.upper()
    s[i] = new
    i += 1
print(s)

####################################### V2

s = ['a', 'b', 'c', 'd', 'e']
for i, show in enumerate(s):
    new = s[i]
    new = new.upper()
    s[i] = new
print(s)