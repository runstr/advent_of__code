from datetime import date
from aocd import get_data
import os
os.environ["AOC_SESSION"] = "53616c7465645f5fedac8b542af40f75294a922ee85d110ceaaae1f702405169a3964d045bd4aba9745ee54e3b8a8b45"


def read_full_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
    return input


def read_input_as_line(filename):
    with open(filename, 'r') as file:
        input = file.read().splitlines()
    return input


def get_todays_date():
    return str(date.today().day)


def insert_data(todays_date):
    filename = __file__[:-8]+"Day"+todays_date+"\\input.txt"
    if os.path.getsize(filename) == 0:
        with open(filename, "w") as inputfile:
            inputfile.write(get_data(year=2021, day=int(todays_date)))
