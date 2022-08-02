def charFrequency(userInput):
    userInput = userInput.lower()
    dict = {}
    for char in userInput:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

if __name__ == '__main__':
    userInput = str(input('Enter a string: '))
    print(charFrequency(userInput))