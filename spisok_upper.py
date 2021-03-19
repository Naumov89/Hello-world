################################################################ variant 1
tv = ['Breaking bad', 'The x files', 'Fargo']
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

################################################################ variant 2

tv = ['Breaking bad', 'The x files', 'Fargo']
for i, show in enumerate(tv): # - enumerate - peredaet cpisok iz tv v enumerate
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)
