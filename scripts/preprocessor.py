#strips newlines and tokenizes with pipes which read.py expects. 
import sys
import pysbd

# main
input_file= sys.argv[1] 

tokenstring=""

with open(input_file, 'r') as file:
    stringtoread = file.read().replace('\n', ' ')

seg = pysbd.Segmenter(language="en", clean=False)    
sentences = seg.segment(stringtoread)
for sen in sentences:
    #TODO: need to further tokenize these based on parens (long parens only?), dashes (n and m), semicolons, quotes
    tokenstring+=sen + "| "

print (tokenstring)
