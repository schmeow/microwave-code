Microwave = {'vhh': 'a', 'vhm': 'b', 'vhV': 'c', 'vhm': 'd', 'vHv': 'e', 'vHh': 'f', 'vHm': 'g',
             'vHV': 'h', 'vHM': 'i', 'hhv': 'i', 'hhh': 'k', 'hhm': 'l', 'hhV': 'l', 'hhV': 'm', 
             'hhM': 'n', 'hHv': 'o', 'hHh': 'p', 'hHm': 'q', 'hHV': 'r', 'hHM': 's', 'mhv': 't',
             'mhh': 'u', 'mhm': 'v', 'mhV': 'w', 'mhM': 'x', 'mHv': 'y', 'mHh': 'z'
}
section = ""

while True:
    string = input("Enter your sentence (q to quit): ")
    if type(string) != str:
        print("Please enter a string")

    if string == 'q':
        break

    else:
        while len(string) > 0:
            section = string[0:3]
            if "-" in section:
                print(" ", end = "")
                string = string[1:]
            else:
                print(Microwave[section], end = "")
                string = string[3:]
    print("")