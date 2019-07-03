"""
Using an enterprise appropriate programming language of your choice,
sort the data by each attribute (both ascending and descending)
and display the result.
"""
from pprint import pprint
from datetime import datetime

l = [                   {
                             "name": "carl", 
                             "age": 38, 
                             "skills": "awesome",
                             "modesty": "awesome",
                             "startDate": "2015-03-02T09:00:00.000000Z"
              },            { 
                             "name": "elson", 
                             "age": 53, 
                             "skills": "average",
                             "modesty": "terrible",
                             "startDate": "2017-02-20T09:00:00.000000Z"
              },            { 
                             "name": "david", 
                             "age": 32, 
                             "skills": "good",
                             "modesty": "average",
                             "startDate": "20/12/2014"
              },            { 
                             "name": "ben", 
                             "age": 41, 
                             "skills": "pretty good",
                             "modesty": "good",
                             "startDate": "2012-06-31T09:00:00.000000Z"
              } 
]

def sort_ascending(l, attr):
    """ Sorts a list of dictionaries by name and age."""
    if attr == "name" or "age":
        l = sorted(l, key = lambda x: x[attr])
    elif attr == "startDate":
        l = sort_date_ascending(l, attr)
    print("Sorted by %s, ascending:" %attr)
    pprint(l)


def sort_descending(l, attr):
    """ Sorts a list of dictionaries by name and age."""
    if attr == "name" or "age":
        l = sorted(l, key = lambda x: x[attr], reverse = False)
    elif attr == "startDate":
        l = sort_date_descending(l, attr)
    print("Sorted by %s, ascending:" %attr)
    pprint(l)

def sort_date_ascending(l, attr):
    """ Sorts a list of dictionaries by date."""
    if l[attr][2] == "/":
        return sorted(l, key=lambda x: datetime.strptime(x['startDate'][:10], '%d/%m/%Y'))
    else:
        return sorted(l, key=lambda x: datetime.strptime(x['startDate'][:10], '%Y-%m-%d'))


def sort_date_descending(l, attr):
    """ Performs reverced sorting of a list of dictionaries by date."""
    if l[attr][2] == "/":
        return sorted(l, key=lambda x: datetime.strptime(x['startDate'][:10], '%d/%m/%Y'), reverse = True)
    else:
        return sorted(l, key=lambda x: datetime.strptime(x['startDate'][:10], '%Y-%m-%d'), reverse = False)


sort_ascending(l, "name")
sort_ascending(l, "age")
sort_ascending(l, "startDate")


sort_descending(l, "name")
sort_descending(l, "age")
sort_descending(l, "startDate")