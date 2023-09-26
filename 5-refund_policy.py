# return an item if 2 cases are met
# 10 days from the purchase date if the item is not used 
# No purchase date, if the item broke and it's not your fault

# 1st question 
purchase_in_days = int(input('How many days ago have you purchased the item? '))

# 2nd question
item_used = input('Have you used the item at all [y/n]? ')

# 3rd question
broken_item = input('Has the item broken down on its own [y/n]? ')

# if statement nested 
if purchase_in_days <= 10 and item_used == 'n' or broken_item == 'y': 
    print('You can get a refund.')
else: 
    print('You cannot get a refund.')
    
        