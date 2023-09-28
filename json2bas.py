# json2bas.py

import json

json_filename = "program.json"
bas_filename = "program.bas"

def json2bas():

    with open(json_filename, "r+") as ifile:
        PROGRAM = json.load(ifile) 
    ifile.close()
    
    ofile = open(bas_filename, "w")
    
    for l in PROGRAM:
        line = l.get("line")
        input = l.get("input")
        ofile.write(str(line) + " " + input + "\n")
    
    ofile.close()

