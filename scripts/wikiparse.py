import pysbd
import wikipedia
import re, sys
import preprocessor

wikiurl = sys.argv[1]

page = wikipedia.page(wikiurl)

stringtoread=page.content
#stringtoread = re.sub (";", ". ", stringtoread) 

#stringtoread = re.sub ("–", ". ", stringtoread)

sentences = preprocessor.preprocess ( stringtoread )
#seg = pysbd.Segmenter(language="en", clean=False)
#sentences = seg.segment(stringtoread)

tokenstring=""

    #TODO: need to further tokenize these based on parens (long parens only?), dashes (n and m), semicolons, quotes
for sen in sentences:
    tokenstring+=sen + "| "
    if (len(sen) > 390): print ("******ERROR: string over 390 characters: " + sen + "\n", file=sys.stderr )

print ( tokenstring )
