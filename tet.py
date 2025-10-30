import json 
import os


thisfile_path = os.path.dirname(__file__)
contain = 0
while contain:
    contain = str(input("whta you want to fill in?"))
    
    temp = {"contain":contain
    }

"""Making json file"""
with open(os.path.join(thisfile_path,jsonfirsttest.json), 'r') as f:
    data = json.dump(contain,f)