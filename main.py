name = input("Type a word: ")

if 'ing' in name:
    print(name + "ly")

elif (len(name) >= 3):
    print( name + "ing")

elif (len(name) < 3):
    print(name)
