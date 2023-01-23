For the primary documentation, see https://github.com/neonbjb/tortoise-tts/

I'm trying to build out a easy-ish to use pipeline to take Wikipedia articles and generate a Tortoise-tts rendering of them. Not quite usable yet!

## Voices. 

To add voices they have to be in 22050 Hz 32-bit float format. One can do this with:

`ffmpeg -i 3.wav -ar 22050 -c:a pcm_f32le 3o.wav`

## To-do

Most of what I'm doing is refining what happens in the text preprocessor to help the tts engine with things it does not say correctly by default. Eventually many of these may well be fixed by larger training sets, but for now I'm doing the simpler task of just making the text "easy to say", since tortoise does quite well saying things phonetically. 

- [ ] Reduce repeats -- sometimes Tortoise "phrase stutters" saying the same few words two or three times. IIRC there are parameters that can fix this. Have to find them. 
- [ ] Separate acronyms -- so it says FBI as F B I rather than Fubeye
- [ ] Roman numeral handling 
- [ ] Replace m-dashes with n-dashes in year ranges
- [ ] % to "percent"
- [ ] Remove footnoes -- most are being omitted by virtue of being in brackets (which Tortose ignores) but pincites to pages are outside of the brackets; might as well remove them all
- [ ] Remove brackets in quotes -- this is a common pattern to "fix" a quotation so it is readable out of its context, but then tortoise skips the bracketed text which is bad
- [ ] Country pronouciation -- Tortoise does not know how to say country names reliably, so like Czechoslovakia and Argentina don't come out right. Its training set was on out-of-copyright books so it's a large body of words it is not familiar with. 
- [ ] Common abbreviations -- e.g., kmh to "kilometers per hour", need a dictionary of these
