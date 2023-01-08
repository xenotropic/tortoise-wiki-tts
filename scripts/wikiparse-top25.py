import pandas
from urllib.request import urlopen
import json
import pysbd

wikiurl = "Wikipedia%3ATop_25_Report"

def make_ordinal(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

# this happens to be the subheading line that has the dates

json_url = urlopen("https://en.wikipedia.org/w/api.php?action=parse&format=json&page=" + wikiurl + "&prop=sections&formatversion=2")
data = json.loads(json_url.read())
title= data["parse"]["sections"][0]["line"]
stringtoread = ("Here are the " + title + "." )
#this gets the wikitables on the page, of which there is only one
dfl = pandas.read_html("https://en.wikipedia.org/wiki/" + wikiurl , attrs={"class": "wikitable"}, flavor='html5lib');
# that returns a list of dataframes, we want the first and only dataframe, which is the only wikitable on the page
df = dfl[0]
#print (df)
for row_index, row in df.iterrows():
    stringtoread += ("The " + make_ordinal (row["Rank"]) + " most popular article this week was " + row["Article"] + ". " + row["Notes/about"] + " " )

#print (stringtoread)

seg = pysbd.Segmenter(language="en", clean=False)
sentences = seg.segment(stringtoread)

tokenstring=""

for sen in sentences:
    #TODO: need to further tokenize these based on parens (long parens only?), dashes (n and m), semicolons, quotes
    tokenstring+=sen + "| "

print (tokenstring)
