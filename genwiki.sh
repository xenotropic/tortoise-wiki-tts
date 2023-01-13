#!/bin/bash
#pip3 install rotary_embedding_torch librosa einops inflect
#pip3 install pysbd html5lib
#cd /notebooks/tortoise-tts
#python3 setup.py install
#right now this is just hardcoded to load the wikipedia top 25; now planning to make it more general. also using paperspace filespace naming conventions
python3 /workspace/tortoise-wiki-tts/scripts/wikitop25tts.py > /notebooks/inputs/wikitop25.txt
python3 /workspace/tortoise-wiki-tts/read.py --voice train_lescault --preset fast --output_path=/workspace/outputs/wikitop25 --text-file=/workspace/inputs/wikitop25.txt  2>&1 | tee -a /workspace/logs/wiki25log.txt

# Things I have tried but that don't currently seem necessary
#/notebooks/tortoise-tts/tortoise_tts.py --batch-size 12 -v william -p fast -O /notebooks/jm/jm-outputs/wikitop25 < /notebooks/jm/jm-inputs/wikitop25.txt 2>&1 | tee -a /notebooks/jm/jm-logs/wiki25log.txt
#python3 read.py --textfile jm-inputs/wikitop25.txt --voice william --preset=fast --output_path=jm-outputs/wikitop25
#pip3 install -U scipy
#pip3 install transformers==4.19.0
#pip3 install -r requirements.txt
