@echo off

set arg1=%1

mkdir Day%arg1%
copy Day1\* Day%arg1%\

cd Day%arg1%
break>input.txt
break>test_input.txt
echo __all__ = ["day%arg1%_1", "day%arg1%_2"]>__init__.py

ren day1_1.py day%arg1%_1.py
ren day1_2.py day%arg1%_2.py
cd ..
type imports\__init__.py > temp.txt
echo from Day%arg1% import * > imports\__init__.py
type temp.txt >> imports\__init__.py
del temp.txt
echo __all__ += ["day%arg1%_1", "day%arg1%_2"]>>imports\__init__.py
