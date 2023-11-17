# program.py

from datetime import datetime
from flask import abort
from flask import request
import json
from ctypes import cdll
import re
import basify
from unidecode import unidecode

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

    if (request.content_type.find("text/plain") >=0):

        program_string = program.decode('utf-8').replace('\\"','"').replace('\\n','\n')

        whitelist = set('µÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ')
        program_string = ''.join(c if c in whitelist else unidecode(c) for c in program_string)

        # If entire program string is lowercase, then change it to uppercase to make CBMBASIC happy.
        if (program_string.islower()):
            program_string = program_string.upper()

        PROGRAM = basify.bas2obj(program_string)

    else:

        program_string = json.dumps(program)
        program_is_lower = False

        # If entire program string is lowercase, then change it to uppercase to make CBMBASIC happy.
        if (program_string.islower()):
           program_is_lower = True 

        for l in program:

            line = l.get("line")
            input = l.get("input")
   
            if (program_is_lower):
                input = input.upper()

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

