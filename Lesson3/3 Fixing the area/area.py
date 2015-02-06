#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):

    if area=='NULL':
        area = None
    else:
        if area[0:1] == '{':
            area_length = len(area)-1
            area_no_bracket = area[1:area_length]

            two_nums = area_no_bracket.split('|')
            num_0 = two_nums[0]
            num_1 = two_nums[1]

            num_0_str = num_0.split('e')
            num_0_str_length = len( num_0_str[0] ) - 1
            num_1_str = num_1.split('e')
            num_1_str_length = len( num_1_str[0] ) - 1

            if num_0_str_length>num_1_str_length:
                area = float(num_0)
            else:
                area = float(num_1)
        else:
            area = float(area)

    return area


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra matadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
                print line["areaLand"]
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None


if __name__ == "__main__":
    test()