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


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Close", "Circle", "Lorong", "Crescent", "Hill", "Highway", "Heights", "Link", "Loop", "Park", "Terrace", "View", "Walk", "Way"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "St ": "Street",
            "street": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "Rd": "Road",
            "road": "Road",
            "Lor": "Lorong",
            "Jl.": "Jalan",
            "Jl": "Jalan",
            "Jln": "Jalan",
            "terrace": "Terrace",
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
                    v = tag.attrib['v']
                    print v,
                    clean_street_name = update_name(v, mapping)
                    print clean_street_name
                    audit_street_type(street_types, clean_street_name)

    return street_types


def update_name(name, mapping):

    pattern = re.compile(r'\b(' + '|'.join(mapping.keys()) + r')\b')
    if pattern:
        name = pattern.sub(lambda x: mapping[x.group()], name)

    return name


def test():
    st_types = audit(OSMFILE)
    # assert len(st_types) == 3
    pprint.pprint(dict(st_types))

if __name__ == '__main__':
    test()