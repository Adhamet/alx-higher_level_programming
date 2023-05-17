#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tmp_dict = a_dictionary.copy()
    for key in tmp_dict.keys():
        tmp_dict[key] *= 2
    return (tmp_dict)
