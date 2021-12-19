from datetime import date
from aocd import get_data
from os import path, environ
from collections import defaultdict
from time import time
import numpy as np
import timeit
environ["AOC_SESSION"] = "53616c7465645f5fedac8b542af40f75294a922ee85d110ceaaae1f702405169a3964d045bd4aba9745ee54e3b8a8b45"

def read_full_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
    return input


def read_input_as_line(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def read_input_as_int(filename):
    input_full = []
    with open(filename, 'r') as file:
        for input_line in file.read().splitlines():
            input_line_list = []
            for i in input_line:
                input_line_list.append(int(i))
            input_full.append(input_line_list)

        return input_full

def get_todays_date():
    return str(date.today().day)


def insert_data(todays_date):
    filename = __file__[:-8]+"Day"+todays_date+"\\input.txt"
    if path.getsize(filename) == 0:
        with open(filename, "w") as inputfile:
            inputfile.write(get_data(year=2021, day=int(todays_date)))


def timeexecution(function):
    def timed(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("Time taken = {}".format(te-ts))
        return result
    return timed
