#!/usr/bin/env python3

import random
import string

# function to generate random names for a given number of ec2 instances
def ec2_naming_generator(): 
    
    # script banner display
    print('''
    =======================================
    ====== EC2 RANDOM NAME GENERATOR ======
    =======================================
    ''')
    
    # ask user for number of ec2 instances they want named
    ec2_inst_requested = int(input('Enter number of EC2 instances that require a name: '))

    # while loop for department name
    while True: 
        # department name input
        department_name = input('Which department do you belong to [Marketing, Accounting, FinOps]: ')
        department_name = department_name.lower()

        # if statement to verify deparment name input will loop if not matched with strings
        if department_name in ('marketing','accounting','finops'): 
            break
        else: 
            print('You are not in the appropriate department to access the name generator. Please enter another department.')
            continue

    # random character generator function
    def character_generator():
        char_num = string.hexdigits
        ran_char_num = [(random.choice(char_num)) for i in range(10)]
        new_random_int = (''.join(ran_char_num))
        return new_random_int
    
    # for loop to iterate through the number of ec2 names requested
    for i in range(ec2_inst_requested): 
        print(department_name + '-' + character_generator())

# call the function
ec2_naming_generator() 

    
