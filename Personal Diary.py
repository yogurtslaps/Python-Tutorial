import os
import json
from datetime import datetime
from pathlib import Path


VERSION = "0.1"
tempPath = Path(__file__).parent / Path("temp/diary.txt")


def init():
    try:
        os.makedirs(tempPath.parent, exist_ok=True) #Create temp directory if not exist
    except OSError:
        print(f'Temp folder creation failed, please check disk write permissions. Program will exit. ')
        return 1

def writefile(content, timestamp):
    f = open(tempPath, "a")
    try:
        if timestamp:
            f.write(datetime.isoformat(datetime.now())+"\n")
        f.write(content)
    except IOError:
        print(f"Write failed on {tempPath}, program will exit.")
    f.close()

def viewfile():
    os.system('cls') #Clear Screen for clearer entry display.
    try:
        f = open(tempPath, "r")

    except FileNotFoundError:
        print(f"Diary File {tempPath} not found, creating...")
        writefile('', False)
        viewfile() #Recurses viewfile to retry
        return

    lines = f.readlines()
    [print(line, end="") for line in lines]

def delete_diary():
    os.remove(tempPath)

def main():
    print(f"=== Diary Manager V{VERSION} === \n©Clara Yau, June 11 2024\nAll Rights Reserved")
    init()
    input_buffer = ''
    while (True):
        input_buffer = input(">>>")
        input_buffer = input_buffer.split()
        
        try:
            cmd = input_buffer[0]
        except IndexError:
            continue

        if cmd == "help":
            print("Help String here, details all possible operations")
        
        elif cmd == "write":
            timestamp = False
            parameters = [param for param in input_buffer if param[0] == '-']
            if "-t" in parameters: #Activate timestamp mode
                timestamp = True
            content = input("Input content:\n")+'\n'
            writefile(content, timestamp);
        
        elif cmd == "view":
            viewfile()

        elif cmd == "delete":
            buffer = input(f"Are you sure you want to delete {tempPath.name}? [Y/N]")
            if buffer == "Y":
                delete_diary()
            else:
                continue

        elif cmd == "quit":
            break

        else:
            print(f"Command {input_buffer[0]} is invalid. Retry.")
            

if __name__ == "__main__":
    main()