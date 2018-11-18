# Create an Aardvark string (i.e., "Aardvark Ablution Acrimonious Adventures ... Zanzibar Zero 
# Zhora Zinfandel Zone Zuni Zwieback Zygote") from selected glyphs so you can see how the caps 
# you have drawn so far are behaving next to the lower case you have drawn so far.

from aardvarks_english import aardvarksEnglish
from aardvarks_english import combos
from random import shuffle
from AppKit import NSPasteboard, NSArray
import mojo

f = CurrentFont()

def aardvarker(charSet):
    aardvarks = ""
    for combo in combos:
        if combo[0] in charSet and combo[1] in charSet:
            newvark = ""
            key = combo[0] + combo[1]
            # print(aardvarksEnglish[key])
            if len(aardvarksEnglish[key]) > 1:
                shuffle(aardvarksEnglish[key])
                increment = 0
                newvark = ""
                while newvark == "" and increment < len(aardvarksEnglish[key]):
                    for word in range(len(aardvarksEnglish[key])):
                        currentWord = ""
                        for letter in range(len(aardvarksEnglish[key][word])):
                            if aardvarksEnglish[key][word][letter] in charSet:
                                currentWord = currentWord + aardvarksEnglish[key][word][letter]
                            if len(currentWord) == len(aardvarksEnglish[key][word]):
                                newvark = currentWord
                    increment += 1
            else:
                newvark = aardvarksEnglish[key][0]
            if len(newvark) <= 3 and "." in charSet:
                newvark += "."
            aardvarks += newvark + " "
    return aardvarks

t = aardvarker(f.selection)
p = NSPasteboard.generalPasteboard()
p.clearContents()
a = NSArray.arrayWithObject_(t)
p.writeObjects_(a)

mojo.UI.Message('Copied to clipboard: \n"%s"' % t)