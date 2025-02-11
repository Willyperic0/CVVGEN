import os
from datetime import datetime

print("\033[38;2;195;63;243m" + r"""
  ______     ____     ______ _____ _   _ 
 / ___\ \   / /\ \   / / ___| ____| \ | |
| |    \ \ / /  \ \ / / |  _|  _| |  \| |
| |___  \ V /    \ V /| |_| | |___| |\  |
 \____|  \_/      \_/  \____|_____|_| \_|
""" + "\033[0m")

def check(xx):
    xx = str(xx).zfill(16)  
    digits = [int(x) for x in xx]

    for i in range(len(digits) - 2, -1, -2):  
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total_sum = sum(digits)
    return total_sum % 10 == 0

now = datetime.now()
actualmonth = now.month  
actualyear_4 = now.year  
actualyear_2 = int(str(now.year)[-2:])  

xx = input("\033[38;2;195;132;24mEnter \033[1mCC number:\033[0m ")
while len(xx) != 16 or not xx.isdigit() or not check(xx):  
    print("\033[38;2;242;44;64m[X] ERROR:\033[0m The CC is invalid.")
    xx = input("\033[38;2;195;132;24mEnter \033[1mCC number:\033[0m ")

dd = input("\033[38;2;64;126;231mEnter \033[1mMONTH:\033[0m ")
while not dd.isdigit() or not (1 <= int(dd) <= 12):  
    print("\033[38;2;242;44;64m[X] ERROR:\033[0m Invalid month.")
    dd = input("\033[38;2;64;126;231mEnter \033[1mMONTH:\033[0m ")

dd = int(dd)  
dd = f"{dd:02}"

yy = input("\033[38;2;61;151;184mEnter \033[1mYEAR:\033[0m ")
while not yy.isdigit() or (len(yy) != 2 and len(yy) != 4):  
    print("\033[38;2;242;44;64m[X] ERROR:\033[0m YY must be exactly 2 or 4 digits.")
    yy = input("\033[38;2;61;151;184mEnter \033[1mYEAR:\033[0m ")

if len(yy) == 2:
    yy = str(actualyear_4)[:2] + yy  

yy = int(yy)  

if yy < actualyear_4 or (yy == actualyear_4 and dd < actualmonth):
    print("\033[38;2;242;44;64m[X] ERROR:\033[0m The entered date cannot be earlier than the current month.")
else:
    file_index = 0
    while os.path.exists(f"list{file_index}.txt"):
        file_index += 1

    filename = f"list{file_index}.txt"

    with open(filename, "w") as file:
        for i in range(1000):
            file.write(f"{xx}|{dd}|{yy}|{i:03}\n")

    print(f"\033[38;2;123;151;38m[✓] FILE CREATED:\033[0m {filename}")