from tinydb import TinyDB, Query
import os

db= TinyDB('TSSC_inventory.json')
db.truncate()

Item1 = {"Product":"Sheet 6 inch", 'Number':34}
db.insert(Item1)
Item1 = {"Product":"Bracket", 'Number':10}
db.insert(Item1)
Item1 = {"Product":"Sheet 8 inch", 'Number':34}
db.insert(Item1)
Item1 = {"Product":"T joint", 'Number':12}
db.insert(Item1)
Item1 = {"Product":"Rod", 'Number':23}
db.insert(Item1)
Item1 = {"Product":"SS304 10 inch", 'Number':5}
db.insert(Item1)

