word = input('enter your word ')
x = len(word)

if word == word[::-1]:
    print(f'{word} if palidrom')
else:
    print("Слово не є паліндромом")