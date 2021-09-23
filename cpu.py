###
### Author: Cumhur Aygar
### Class: CSc 110
### Description: This program takes the CPU gigahertz and CPU core inputs from the user
###                 and decides which category they fit into, and prints that category.
###

#First we create variables to assign the user's inputs into
giga = float(input("Enter CPU gigahertz:\n"))
core = int(input("Enter CPU core count:\n"))

#We then check if they fit each category, starting from the top. If they aren't above a certain number and don't fit in
#the higher category, we check the one below. Till finally, if no categories fit, we print
#"That CPU could use an upgrade".
if core >= 20:
    print("\nThat is a high-performance CPU.")
elif giga >= 3.2 and core >=8:
    print("\nThat is a high-performance CPU.")
elif giga >= 2.5 and core >=6:
    print("\nThat is a medium-performance CPU.")
elif giga >= 2.0 and core >= 2:
    print("\nThat is a low-performance CPU.")
else:
    print("\nThat CPU could use an upgrade.")