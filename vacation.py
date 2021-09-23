###
### Author: Cumhur Aygar
### Class: CSc 110
### Description: Create a short mad lib story using inputted values.
###
###


mname = input("A male name:\n")
fname = input("A female name:\n")
pname = input("A pet name:\n")
pla = input("A place:\n")
adj = input("An adjective:\n")
ani = input("An animal:\n")
ing = input("A verb ending in ing:\n")
adv = input("An adverb:\n")


print("----------")

print(f'''{mname} and {fname} were best friends.
One day {mname} and {fname} decided to go on a
vacation to {pla}. However, they didn't know
what to do with their {adj} pet {ani} named {pname}.
{pname} had been causing problems, due to constant {ing}.
{mname} found a sitter for their pet, and {adv} went on the trip.''')