Microwave = {'a': 'v.h.h', 'b': 'v.h.m', 'c': 'v.h.V', 'd': 'v.h.M', 'e': 'v.H.v', 'f': 'v.H.h', 'g': 'v.H.m',
             'h': 'v.H.V', 'i': 'v.H.M', 'j': 'h.h.v', 'k': 'h.h.h', 'l': 'h.h.m', 'm': 'h.h.V', 'n': 'h.h.M',
             'o': 'h.H.v', 'p': 'h.H.h', 'q': 'h.H.m', 'r': 'h.H.V', 's': 'h.H.M', 't': 'm.h.v', 'u': 'm.h.h',
             'v': 'm.h.m', 'w': 'm.h.V', 'x': 'm.h.M', 'y': 'm.H.v', 'z': 'm.H.h', ' ': ''}

while True:
    string = input("Enter your sentence (q to quit): ")
    if type(string) != str:
        print("Please enter a string")

    if string == 'q':
        break

    else:
        letters = list(string.lower())
        for letter in letters:
            print(Microwave[letter], end='-')
    print("")
