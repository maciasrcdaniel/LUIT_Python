#!/usr/bin/env python3

# receive list of spendings each month 
# count number of times spending was low/normal/high

# LIST OF SPENDINGS
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

# VARIABLES FOR COUNTS 
low_count = 0
normal_count = 0
high_count = 0

# FOR LOOP TO ITERATE THROUGH THE "spedings" VARIABLE
for spend in spendings: 
    # IF STATEMENT THAT WILL VERIFY IF THE SPENDING IS IN MARGIN KEEP A COUNT
    if spend < 1000.0: 
        low_count += 1
    elif spend >= 1000.0 and spend <= 2500.0: 
        normal_count += 1
    else: 
        high_count += 1

# PRINT STRING CONCATENATION USING THE F-STRING        
print(f'Numbers of months with low spendings: {low_count}, normal spendings: {normal_count}, high spendings: {high_count}.')
    
