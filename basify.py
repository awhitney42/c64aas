# json2bas.py

import json
import re
import os

home_variable = os.environ['HOME']

json_filename = f"{home_variable}/git/c64aas/program.json"
bas_filename = f"{home_variable}/git/c64aas/program.bas"

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

def bas2obj(program):

    PROGRAM = []
    program_lines = program.splitlines(True)
    for l in program_lines:
        l = re.sub(r"\n$",'', l).strip()
        if (l):
            line= re.search(r"\d+ ", l)
            input = re.sub(r"^\d+ ", '', l)
            element = {
            	"input": input,
            	"line": int(line.group(0).strip()),
            }
            PROGRAM.append(element)
    return PROGRAM


