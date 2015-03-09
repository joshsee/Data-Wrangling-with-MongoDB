"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "singapore.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Jalan", "Lebuhraya", "Avenue", "Lorong", "Persiaran", "Road", "Street", "Drive", "Lane", "Way", "Walk", "Terrace", "Crescent", "Close", "Central", "Hill", "Link", "Park", "Loop", "Place", "Turn", "View", "Green"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Rd.": "Road",
            "road": "Road",
            "Ave": "Avenue",
            "Jl.": "Jalan",
            "Jln": "Jalan",
            "Lor": "Lorong",
            "Dr": "Drive"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):

    # YOUR CODE HERE
    street_name = name.split(' ')
    if street_name[-1] in mapping:
        correct_name = mapping[street_name[-1]]
        street_name[-1] = correct_name

    name = ' '.join(street_name)

    return name


def test():
    st_types = audit(OSMFILE)
    # assert len(st_types) == 3
    pprint.pprint(dict(st_types))


if __name__ == '__main__':
    test()