# program: ask user to guess when python 1.0 was released
# correct answer: 1994

# Initial question
ask_python = int(input('When was Python 1.0 released? '))

while ask_python != 1994: 
    if ask_python > 1994: 
        print('It was earlier than that!')
        ask_python = int(input('When was Python 1.0 released? '))
        continue
    elif ask_python < 1994: 
        print('It was later than that!')
        ask_python = int(input('When was Python 1.0 released? '))
        continue
    elif ask_python == 1994: 
        break
print('Correct!')

    