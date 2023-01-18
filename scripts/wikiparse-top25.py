import pandas
from urllib.request import urlopen
import json
import pysbd
import re

wikiurl = "Wikipedia%3ATop_25_Report"
stringtoread = ""

def make_ordinal(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

# the page is cross-referenced with e.g., "#4" to refer to #4 on the list.
# this replaces it with "number 4, [title of #4]," to make it easier to follow.

def ordinal_replace(matchobj):
    num = matchobj.group(0)[1:] #using string slicing to remove leading #
    num_index = int (num) - 1 # text numbers start from one, dataframe from zero
    return " number " + num + ", " + df.iloc[num_index]["Article"] 

# makes $1.2 billion into 1.2 billion dollars which TTS handles more gracefully

def money_replace(matchobj):
    moneystr = matchobj.group(0)[1:] # string slice off $
    return moneystr + " dollars "
    
# this happens to be the subheading line that has the dates

json_url = urlopen("https://en.wikipedia.org/w/api.php?action=parse&format=json&page=" + wikiurl + "&prop=sections&formatversion=2")
data = json.loads(json_url.read())
title= data["parse"]["sections"][0]["line"]
stringtoread = ("Here are the " + title + "." )

#this gets the wikitables on the page, of which there is only one
dfl = pandas.read_html("https://en.wikipedia.org/wiki/" + wikiurl , attrs={"class": "wikitable"}, flavor='html5lib');
# that returns a list of dataframes, we want the first and only dataframe, which is the only wikitable on the page
df = dfl[0]

for row_index, row in df.iterrows():
    stringtoread += "The " + make_ordinal (row["Rank"]) + " most popular article this week was " + row["Article"] + ". "
    notes =  row["Notes/about"]
    if not pandas.isna(notes):
        if ( row_index + 1 < len (df) ):
            if (notes == df.iloc[row_index+1]["Notes/about"]): continue # this handles multiple entries with the same notes
        notes = re.sub('#[0-9][0-9]?', ordinal_replace, notes)
        notes = re.sub('\$[0-9.]* ?[bmtz]illion', money_replace, notes) 
        stringtoread +=  notes + " "

seg = pysbd.Segmenter(language="en", clean=False)
sentences = seg.segment(stringtoread)

tokenstring=""

for sen in sentences:
    #TODO: might need to further tokenize these based on parens (long parens only?), dashes (n and m), semicolons, quotes
    tokenstring+=sen + "| "

print (tokenstring)

