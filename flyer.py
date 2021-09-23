###
### Author: Cumhur Aygar
### Class: CSc 110
### Description: Create a Wright Flyer using ASCII art
###
###


size = int(input("Wright flyer size:\n"))

p = int(size*1.2)

height = (int(size/5) +1)
#I created a second variable that equaled height so that after my initial loop, I would still have a variable with the value of 'height' that I can use for my second loop.
h = height
#now like the USS Arizona, I had to create specific variations of the "panel" size values. I started by creating the left panels and the right panels.
panel_right = p*"|    "
panel_left = p*"    |"

#Then I created some basic variables to use for the non-panel parts of the plane:
spaces = p*"     "
equals = p*"====="
print(f'''{spaces}        #
{spaces}   #---------#
{spaces}   #---------#
={equals}==============={equals}=''')

#All that was left was to plug them in the ASCII art.
while height > 0:

    print(f" H{panel_left}  |  %H%  |  {panel_right}H")
    height -=1
print(f" H{panel_left}**|**%H%**|**{panel_right}H")
while h > 0:

    print(f" H{panel_left}  |  %H%  |  {panel_right}H")
    h -=1
print(f'''{equals}=======%H%======{equals}=
{spaces}   |         |
{spaces}   +#########+''')