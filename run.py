# run.py

from datetime import datetime
from flask import abort
from flask import request
import subprocess
import json
import basify
import multiprocessing as mp
from ctypes import *

# Load the shared library for cbmbasic
#lib = cdll.LoadLibrary('../cbmbasic/libcbmbasic.so')
#lib.main.restype = c_int
#lib.main.argtypes = c_int,POINTER(c_char_p)

def get_timestamp():

    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def make_args(cmd):
    args = cmd.encode().split()
    return (c_char_p * len(args))(*args)

def cbmbasic(args):
    lib.main(len(args), args)

def read_all():

    output = ''
    line = ''

    # Convert program to BAS file
    basify.json2bas()

    # Run the cbmbasic ___main___ function in a subprocess.
    #my_args = make_args('main program.bas')
    #ps = [mp.Process(target=cbmbasic, args=(my_args,)) for i in range(8)]
    #for p in ps:
    #    p.start()

    process=subprocess.Popen(['timeout' ,'10', 'cbmbasic', 'program.bas'], stdout=subprocess.PIPE)
    out,err = process.communicate()

    output_basic = str(out, 'UTF-8')

    output_lines = output_basic.splitlines()
    output_json = json.dumps(output_lines)

    if (request.headers.get('accept') == "text/plain"):
        return output_basic
    else:
        return output_json
