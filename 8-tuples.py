#!/usr/bin/env python3

# tuples list (city_from, city_to, time)
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

# - TASK: go through routes w/ loop and check how many (city_to = 'Rome')
# - TASK: sum(time) * # of flights

# - Variable created store the number of entries with 'Rome' as city_to
city_count = 0
# - Variable created to store the sum of time in minutes
time_sum_count = 0
# - for loop to iterate through the tuples
for connects in connections:
    # - if the second item in tuple matches 'Rome' proceed to add 1 to the city_count and add the 3rd item to all the others 
    if connects[1] == 'Rome':
        city_count += 1
        time_sum_count += connects[2]
        time_ave = time_sum_count/city_count
# print with f-strings
print(f'{city_count} connections lead to Rome with an average flight time of {time_ave} minutes')
        

