from imports import *
import Tools


if __name__ == '__main__':
    todays_date = Tools.get_todays_date()
    exec("day{}_1.execution()".format(todays_date))
    exec("day{}_2.execution()".format(todays_date))
