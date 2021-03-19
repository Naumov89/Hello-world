
rhymes = {'1': 'lol', '2': 'red', '3': 'I', '4': 'floor', '5': 'live'}

n = input('Enter namber:')
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print('no found')