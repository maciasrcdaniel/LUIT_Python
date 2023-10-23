#!/usr/bin/env python3


# - write a function named: unique

def unique(input_list=[]): 
    new_list = []
    for item in input_list: 
        if item not in new_list: 
            new_list.append(item)
    return new_list