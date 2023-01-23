For the primary documentation, see https://github.com/neonbjb/tortoise-tts/

I'm trying to build out a easy-ish to use pipeline to take Wikipedia articles and generate a Tortoise-tts rendering of them. Not quite usable yet!

## Voices. 

To add voices they have to be in 22050 Hz 32-bit float format. One can do this with:

`ffmpeg -i 3.wav -ar 22050 -c:a pcm_f32le 3o.wav`
