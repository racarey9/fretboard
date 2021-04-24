def getPostscriptDefs():
    return """
        <</Install { .70 .70 scale } bind >> setpagedevice
        0 950 translate

        /Times-Roman findfont
        14 scalefont
        setfont         
        1 setlinewidth

        /fretwidth 40 def
        /nut 80 def
        /0fret nut def

        /1fret  nut    fretwidth add def
        /2fret  1fret  fretwidth add def
        /3fret  2fret  fretwidth add def
        /4fret  3fret  fretwidth add def
        /5fret  4fret  fretwidth add def
        /6fret  5fret  fretwidth add def
        /7fret  6fret  fretwidth add def
        /8fret  7fret  fretwidth add def
        /9fret  8fret  fretwidth add def
        /10fret 9fret  fretwidth add def
        /11fret 10fret fretwidth add def
        /12fret 11fret fretwidth add def
        /13fret 12fret fretwidth add def
        /14fret 13fret fretwidth add def
        /15fret 14fret fretwidth add def
        /16fret 15fret fretwidth add def
        /17fret 16fret fretwidth add def
        /18fret 17fret fretwidth add def
        /19fret 18fret fretwidth add def
        /20fret 19fret fretwidth add def
        /21fret 20fret fretwidth add def
        /22fret 21fret fretwidth add def
        /23fret 22fret fretwidth add def

        /0fret nut def
        /stringwidth 20 def

        /1string 200 def
        /2string 1string stringwidth sub def
        /3string 2string stringwidth sub def
        /4string 3string stringwidth sub def
        /5string 4string stringwidth sub def
        /6string 5string stringwidth sub def

        % Draw a note
        % r = red
        % b = blue
        % g = green
        % w = text width (e.g. for sharps and flats)
        % id = color of text printed on note
        % 
        % This works by side effect.  Nothing is left on the stack.
        % id w r g b --
        /donote { 
         newpath
          exch

          /b  exch def
          /g  exch def
          /r  exch def
          /w  exch def
          /id exch def

          2 copy
          2 copy

          12 0 360 arc closepath
          r g b setrgbcolor fill
          12 0 360 arc closepath
          0 setgray
          stroke

          id setgray
          % Position to print note name
          4 sub
          2 1 roll
          w sub
          2 1 roll
          moveto
          show
        } def


        % Some useful colored notes
        % Use version beginning with "w" (wide) for sharps/flats

        /red      { 1 4  1  0  0 donote } def
        /wred     { 1 7  1  0  0 donote } def

        /orange   { 0 4  1  0  .5 donote } def
        /worange  { 0 7  1  0  .5 donote } def

        /magenta  { 0 4  1  1 .5 donote } def
        /wmagenta { 0 7  1  1 .5 donote } def

        /cyan     { 0 4 .5  1  1 donote } def
        /wcyan    { 0 7 .5  1  1 donote } def

        /yellow   { 0 4  1 .5  1 donote } def
        /wyellow  { 0 7  1 .5  1 donote } def

        /green    { 0 4 .5 .5  1 donote } def
        /wgreen   { 0 7 .5 .5  1 donote } def

        /blue     { 1 4 .5  1 .5 donote } def
        /wblue    { 1 7 .5  1 .5 donote } def

        /note     { 0 4  1  1  1 donote } def
        /wnote    { 0 7  1  1  1 donote } def

        /fadenote   { .5 4  1  1  1 donote } def
        /fadewnote  { .5  1  1  1 donote } def

        /inote   { 3 1 1 1 setgray fill donote } def

        % Draw a darkened circle (marker for 3rd, 5th, 7th, 9th, 12th frets)
        /dot {
          gsave
          newpath
          exch
          5 0 360 arc closepath
          0.5 setgray fill
          grestore
        } def

        % Draw the dots on the fretboard at the
        % 3rd, 5th, 7th, 9th, and 12th frets
        /midneck { 10 } def

        /dotfrets {
          3string midneck sub 3fret dot
          3string midneck sub 5fret dot
          3string midneck sub 7fret dot
          3string midneck sub 9fret dot

          2string midneck sub 12fret dot
          4string midneck sub 12fret dot
        } def

        /necklength 820 def
        /necktop    200 def
        /neckbottom 100 def

        % Draw the strings on the fretboard
        /strings {
          neckbottom stringwidth necktop {
              dup
              neckbottom exch moveto
              necklength exch lineto
          } for
        } def  

        % Draw the frets on the fretboard
        /frets {
          neckbottom fretwidth necklength {
              dup
              neckbottom moveto
              necktop    lineto
          } for
        } def

        % Draw a vertical separator between fretboard sections
        /divider {
            gsave
            2 setlinewidth
            dup
            1 0 0  setrgbcolor
            80 moveto
            220 lineto
            stroke
            grestore
        } def

        % Draw the entire fretboard
        /fretboard {
          0.1 setgray
          1 setlinewidth

          strings frets dotfrets 
          stroke

        } def

        % Draw horizontal text at location
        /hortext {
          gsave
          moveto
          /Courier findfont
          20 scalefont
          setfont
          show
          grestore
        } def

        % Draw vertical text at location
        /vertext {
          moveto
          gsave
          /Courier findfont
          20 scalefont
          setfont
          90 rotate
          show
          grestore
        } def

        % Print a title to the left
        /title {
          40 -10 vertext
        } def

        % Print a title to the top
        /htitle {
          40 250 hortext
        } def

        % Add text to the left of a fretboard
        /label {
          1string 170 sub 1fret 20 sub vertext
        } def

        % Add text a line below "label" text
        /sublabel {
          1string 150 sub 1fret 20 sub vertext
        } def

% There is a question here of how to color enharmonics.
% Do you want F and F# to share a color in different
% freboards where those represent the "F" note in 
% the represented diatonic?
% Or do you want F# and Gb to share a color because
% they are the same note?  I think the answer depends
% on the diagram(s) being constructed, so maybe it should
% be an option to drawboard.
% 
% 
% Having the name of the note specify its appearance
% is convenient, but not necessarily elegant.
% 
% This could be improved, but I tend to just directly 
% edit the generated PostScript

        /E  { magenta  } def
        /Eb { wmagenta } def
        /E# { wmagenta } def

        /F  { orange   } def
        /Fb { worange  } def
        /F# { worange  } def

        /G  { cyan     } def
        /Gb { wcyan    } def
        /G# { wcyan    } def

        /A  { green    } def
        /Ab { wgreen   } def
        /A# { wgreen   } def

        /B  { blue     } def
        /Bb { wblue    } def
        /B# { wblue    } def

        /C  { red      } def
        /Cb { wred     } def
        /C# { wred     } def

        /D  { yellow   } def
        /Db { wyellow  } def
        /D# { wyellow  } def

    """
# List of notes and number of half steps to next note in scale
E = ("E", 1)
F = ("F", 2)
G = ("G", 2)
A = ("A", 2)
B = ("B", 1)
C = ("C", 2)
D = ("D", 2)

diatonic = (C, D, E, F, G, A, B)

# Rotate the C Major scale to create the order of
# the notes for each string
Estr_diatonic = diatonic[2:] + diatonic[:2]
Astr_diatonic = diatonic[5:] + diatonic[:5]
Dstr_diatonic = diatonic[1:] + diatonic[:1]
Gstr_diatonic = diatonic[4:] + diatonic[:4]
Bstr_diatonic = diatonic[6:] + diatonic[:6]

# Get the note preceding this diatonic note
def predecessor(note):
    val = None
    notes = "CDEFGAB"
    for i in range(len(notes)):
        if notes[i] == note:
            val = "B" if note == "C" else notes[i-1]
            break
    return val

# Get the note following this diatonic note
def successor(note):
    val = None
    notes = "CDEFGABC"
    for i in range(len(notes)):
        if notes[i] == note:
            val = notes[i+1]
            break
    return val

def add_accidentals(note, fret, string_number, halfsteps):
    val = []
    # Add the next note as an accidental
    val.append((note + "#", fret+1, string_number))
    if (halfsteps == 2):
        val.append((successor(note) + "b", fret+1, string_number))
    else:
        val.append((successor(note) + "b", fret, string_number))

    return val

# For each fret on a string, create a tuple of (note, fret, string)
# for it and the subsequent note with all enharmonic names
# and add them to the list to be returned
#
# Loop creating notes for frets nut -> 11 and then again 
# for their counterparts in 12 to 23
#
# (Could be called gen_chromatic?)
def gen_guitar_string(s, string_number):
    val = []

    for f in (0, 12):
        fret = f
        for i in s:
            note = i[0]
            halfsteps = i[1]

            # Add this note
            val.append((note, fret, string_number))
            val = val + add_accidentals(note, fret, string_number, halfsteps)
            fret = i[1] + fret
    return val

note_name_ix = 0
note_fret_ix = 1
note_string_ix = 2

# Create the string layouts
low_E_string = gen_guitar_string(Estr_diatonic, 6)
A_string     = gen_guitar_string(Astr_diatonic, 5)
D_string     = gen_guitar_string(Dstr_diatonic, 4)
G_string     = gen_guitar_string(Gstr_diatonic, 3)
B_string     = gen_guitar_string(Bstr_diatonic, 2)
E_string     = gen_guitar_string(Estr_diatonic, 1)

# Return a function to test whether a 
# note/fret tuple contains a given note
def mk_get_note(note):
    def f(note_and_fret):
        val = False
        if (note[note_name_ix] == note_and_fret[note_name_ix]):
            val = True
        return val
    return f

# Return a function to select a note within range of strings
def get_note_in_string_set(low, high):

    def note_in_set(n):
        if n != None:
            val = None
            if n[note_string_ix] in range(low, high + 1):
                val = n
            return val
    return note_in_set

# Return a function to select a specific note in a filter
def get_named_note(note_name):
    
    def get_one_note(n):
        if n != None:
            val = None
            if note_name == n[note_name_ix]:
                val = n
            return val
    return get_one_note

# Return func to get occurrences of the note within a range of frets
def get_note_in_position(lowfret, highfret):

    def note_in_position(n):
        val = None
        if n != None:
            if lowfret <= n[note_fret_ix]:
                if highfret > n[note_fret_ix]:
                    val = n
        return val
    return note_in_position

# Return func to avoid printing any note at the f fret on string s
def remove_note(f, s):

    def dont_print(n):
        val = None
        if n != None:
            if not (n[note_fret_ix] == f and n[note_string_ix] == s):
                val = n
        return val

    return dont_print

def get_note_in_range(lowfret=0, highfret=19, lowstring=1, highstring=6, removers=()):

    def note_in_range(n):
        for r in removers:
            n = r(n)
        return get_note_in_string_set(lowstring, highstring)(
                   get_note_in_position(lowfret, highfret)(n))

    return note_in_range

# Generate PostScript for the fretboard
def drawboard(notes, loc, targets, notefilter=get_note_in_range(), label=None, sublabel=None):
    val = ""
    val += "0 %s translate\n" % (loc)
    val += "fretboard\n"
    if label:
        val += "(%s) label\n" % (label)

    if sublabel:
        val += "(%s) sublabel\n" % (sublabel)

    for t in targets:
        for n in notes[t]:
            if notefilter(n):
                val += "(%s) %dfret %dstring %s\n" % (t, n[1], n[2], t)
    return val

