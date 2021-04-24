Guitar Fretboard Diagram Generator
==================================
This is a hack that I created for my own use to make it easier to
create diagrams of guitar fretboards.

It is a Python program to generate a PostScript program that contains
the diagram.

I am neither a PostScript nor a Python expert, so the the code is
probably not idiomatic and likely contains errors.

In PostScript there are a number of things I didn't take the time to
fully understand.  For example, I was not sure when to use gsave and
grestore.  I did most of the positioning in the coordinate system by
trial and error.

I am not planning to maintain this project, but I thought I'd put it
somewhere public in case someone else might be able to get some use
out of it.  If you are interested in modifying it please just copy
it into your own project.

There are no unit tests.  I made a number of changes recently and have
not thoroughly inspected the results to ensure that the note names and
positions are all correct.

There are some incomplete examples in example.py which should give
some idea how to use the code.
