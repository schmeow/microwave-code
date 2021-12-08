Microwave = {'a': 'vhh', 'b': 'vhm', 'c': 'vhV', 'd': 'vhM', 'e': 'vHv', 'f': 'vHh', 'g': 'vHm',
             'h': 'vHV', 'i': 'vHM', 'j': 'hhv', 'k': 'hhh', 'l': 'hhm', 'm': 'hhV', 'n': 'hhM',
             'o': 'hHv', 'p': 'hHh', 'q': 'hHm', 'r': 'hHV', 's': 'hHM', 't': 'mhv', 'u': 'mhh',
             'v': 'mhm', 'w': 'mhV', 'x': 'mhM', 'y': 'mHv', 'z': 'mHh', ' ': '-'}

while True:
    string = input("Enter your sentence (q to quit): ")
    if type(string) != str:
        print("Please enter a string")

    if string == 'q':
        break

    else:
        letters = list(string.lower())
        for letter in letters:
            print(Microwave[letter], end='')
    print("")