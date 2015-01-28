#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        # My Solution
        carrier_list = soup.find(id="AirportList").find_all('option')
        exclude_list = ['All', 'AllMajors', 'AllOthers']
        for content in carrier_list:
          value = content['value']
          if value not in exclude_list:
            data.append(value)

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()