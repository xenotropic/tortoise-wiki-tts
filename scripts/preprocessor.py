#strips newlines and tokenizes with pipes which read.py expects. 
import sys, re
import pysbd

# makes $1.2 billion into 1.2 billion dollars which TTS handles more gracefully

def money_replace(matchobj):
    moneystr = matchobj.group(0)[1:] # string slice off $
    return moneystr + " dollars "

# spell out common abbreviations
def abbrev_remove (text):
    dictionary = {"Mr.":"Mister", "St.":"Street","Mrs.":"Missus","Ms.":"Miz","Dr.":"Doctor","Prof.":"Professor","Capt.":"Captain", "Dr.":"Drive" ,  "Ave.":"Avenue" , "Blvd.":"Boulevard", "Gen.":"General" }
    for key in dictionary.keys():
        text = text.replace(key, dictionary[key])
    return text

# This method from stack exchange https://stackoverflow.com/a/31505798/720763 CC-BY-SA-4.0

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr|Prof|Capt)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"

def gh_sentences(text):
    text = " " + text + "  "
    text = re.sub('==*', '-', text) # wikipedia headers
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace(":",":<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# Makes shorthand ordinals like "1st" into "first" which TTS reads more reliably
def ordinal_replace(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

def preprocess (text):
    text = abbrev_remove (text)
    text = re.sub('#[0-9][0-9]?', ordinal_replace, text)
    text = re.sub('\$[0-9.]* ?[bmtz]illion', money_replace, text) 
    text = gh_sentences (text)
    return text
