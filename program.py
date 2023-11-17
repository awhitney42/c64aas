# program.py

from datetime import datetime
from flask import abort
from flask import request
import json
from ctypes import cdll
import basify

lib = cdll.LoadLibrary('../cbmbasic/libcbmbasic.so')

PROGRAM = [
            {
                "line": 10,
                "input": "PRINT \"FOO\"",
            },
            {
                "line": 20,
                "input": "GOTO 10",
            },
          ]

filename = "program.json"

def get_timestamp():

    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():

    with open(filename, "r+") as file:
        PROGRAM = json.load(file) 

    return PROGRAM

def read_one(line):

    with open(filename, "r+") as file:
        PROGRAM = json.load(file) 

    for l in PROGRAM:
        line_number = l.get("line")
        input = l.get("input")
        if line_number == line:
            return l
    else:
        abort(
            404, f"Line {line} not found"
        )

def create(program):

    PROGRAM = []

    if (request.content_type == 'text/plain'):

        program_string = program.decode('utf-8')
        PROGRAM = basify.bas2obj(program_string)

    else:

        for l in program:

            line = l.get("line")
            input = l.get("input")
    
            if input:
                element = {
                    "input": input,
                     "line": line,
                     }
                PROGRAM.append(element)
            else:
                abort(
                    406,
        			"Invalid program request",
            )

    with open(filename, "w") as file:
        file.write(json.dumps(PROGRAM)) # write PROGRAM to file

    return PROGRAM, 201

