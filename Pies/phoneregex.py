import re

go = 1

while go == 1:
    num = input()

    patt = r"(^1|^8|^9)\d{2}(\s|-|\.)?\d{5}"

    match = re.search(patt , num)

    if match:

        print("Valid")
        continue

    elif match == "q":

        go = 0

    else:

        print("Invalid")
        continue
