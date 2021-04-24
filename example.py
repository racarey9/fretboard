from fretboard import *
import sys

# examples
e6 = tuple(filter(mk_get_note("E"), low_E_string))
a  = tuple(filter(mk_get_note("E"), A_string))
d  = tuple(filter(mk_get_note("E"), D_string))
g  = tuple(filter(mk_get_note("E"), G_string))
b  = tuple(filter(mk_get_note("E"), B_string))
e1 = tuple(filter(mk_get_note("E"), E_string))    

# sys.stderr.write(str(a) + "\n")

all_e = e6 + a + d + g + b + e1
# sys.stderr.write(str(all_e) + "\n")

whole_neck = low_E_string + A_string + D_string +\
             G_string + B_string + E_string
# sys.stderr.write(str(whole_neck) + "\n")

# d = dictionary
# n = note name
# v = note values

# We are building a dictionary of note names to
# lists of note locations.
# Add a note to the list that is the value of the hash
# entry.
#
# Create an empty list if needed.
def add_note(d, n, v):
    if not n in d:
        d[n] = []
    d[n].append(v)

notes = {}
for n in whole_neck:
    add_note(notes, n[0], n)

def getPostscriptEndCommands():
    return "showpage"
    
# Configuration
print(getPostscriptDefs())

f = get_note_in_range(11, 15, 2, 4, (remove_note(14, 3),remove_note(14, 4)))

# To visually review that enharmonics are correct
print(drawboard(notes, "-160", ("C", "D", "E",  "F", "G", "A", "B"), f, None, None))

f = get_note_in_range()
print(drawboard(notes, "-160", ("C", "D", "E",  "F", "G", "A", "B"), f, None, None))

f = get_note_in_range(lowstring=2, highstring=4)
print(drawboard(notes, "-160", ("C", "D", "E",  "F", "G", "A", "B"), f, None, None))

f = get_note_in_range(lowfret=11, highfret=19)
print(drawboard(notes, "-160", ("C", "C#", "D", "D#", "E",  "F", "F#", "G", "G#", "A", "A#", "B"), f))
print(drawboard(notes, "-160", ("C", "Db", "D", "Eb", "E",  "F", "Gb", "G", "Ab", "A", "Bb", "B"), f))

print(getPostscriptEndCommands())
print(getPostscriptDefs())

print(drawboard(notes, "-160", ("Cb", "Fb")))
print(drawboard(notes, "-160", ("E#", "B#")))

f = get_note_in_range()
print(drawboard(notes, "-160", ("G", "A", "B", "C", "D", "E", "F")))
print(drawboard(notes, "-160", ("G", "A", "B", "C", "D", "E", "F"), f,  "C Major"))

f = get_note_in_range(lowfret=11, highfret=16)
print(drawboard(notes, "-160", ("G", "A", "B", "C", "D", "E", "F"),  f, "C Major"))

f = get_note_in_range(lowfret=3, highfret=9)
print(drawboard(notes, "-140", ("C", "D", "E", "F#", "G", "A", "B"), f,  "G", "Major"))

print(getPostscriptEndCommands())
print(getPostscriptDefs())

f = get_note_in_range(lowfret=6, highfret=11)
print(drawboard(notes, "-140", ("C", "D", "E", "F#", "G", "A", "B"), f))

groups = [ ("C",  "E",  "G"),
           ("D",  "F",  "A"),
           ("E",  "G",  "B"),
           ("F",  "A",  "C"),
           ("G",  "B",  "D"),
           ("A",  "C",  "E"),
           ("B",  "D",  "F")]

locs = ("-40", "-140", "-140", "-140", "-140", "-140", "-140")

labels = ("Cmaj", "Dmin", "Emin", "Fmaj", "Gmaj", "Amin", "Bdim")
sublabels = ("Example", None, None, None, None, None, None)

f = get_note_in_range()
for i in range(0, len(groups)):
    print(drawboard(notes, locs[i], groups[i], f, labels[i], sublabels[i]))

print(getPostscriptEndCommands())
 
