import subprocess

if __name__ == '__main__':
    for i in range(14, 26):
        filepath = "new_day.bat "+str(i)
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

        stdout, stderr = p.communicate()
        print(p.returncode) # is 0 if success

