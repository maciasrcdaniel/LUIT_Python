#!/usr/bin/env python3

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# 1. prompt user: Enter a word in English or EXIT: 
# 2. If user enters EXIT in capital letters terminate the program with 'Bye!'
# 3. else try to find the german equivalent in the dictionary above
    # 4. if word in dictionary print: Translation {}
    # 5. if word is NOT in the dictionary print: No match! 
    # 6. keep asking user the original prompt until they type: EXIT

while True: 
    enter_prompt = input('Enter a word in English or EXIT: ')
    if enter_prompt == 'EXIT':
        print('Bye!')
        break
    elif enter_prompt in sample_dict: 
        print(f'Translation: {sample_dict[enter_prompt]}')
    else:
        print('No match!')


        
    