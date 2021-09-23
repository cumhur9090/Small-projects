###
### Author: Cumhur Aygar
### Class: CSc 110
### Description: Create a USS Arizona using ASCII art
###
###


outer = int(input("USS Arizona outer width:\n"))

inner = int(input("USS Arizona inner width:\n"))

height = int(input("USS Arizona tower height:\n"))

t = (outer + inner)//7

#To not have to deal with all of the specific string variations later on, I created the 6 basic versions I'll need. 4 of them are variations of the inner function.
inner_space = inner*"  "
inner_mid = inner*"-#"
inner_dot = inner*".."
inner_line = inner*"_"
#and 2 of them are variations of the outer.
outer_space = outer*" "
outer_line = outer*"_"

#All that was left was to put them in their respective places.

#Also, I used while loops as this was the most efficient way I could find to stack the print functions on top of each other (for the height variable).
while t > 0:
    print(f"              {outer_space}       |{inner_space}|")
    t =t-1
print(f'''           {outer_space}       |##${inner_space}$##|''')
while height > 0:
    print(f"     {outer_space}              ##{inner_space}  ##")
    height = height-1

print(f'''     {outer_space}             #..#{inner_space}#..#
           {outer_space}\----. #..#{inner_dot}#..# .----/''')



print(f'''    {outer_space} \ ***|_|    |#..#{inner_mid}#..#|    |_|*** /
.____{outer_line}_|____          _{inner_dot}_          ____|_{outer_line}..
`---.{outer_space}                 {inner_space}                  {outer_space}--\.
 <<#\_{outer_line}________________{inner_line}______________________{outer_line}\  ''')






