#!/bin/bash
cd /workspace/tortoise-tts
python -m pip install -r requirements.txt
python -m pip install pysbd html5lib
python -m pip install .
#right now this is just hardcoded to load the wikipedia top 25; now planning to make it more general. also using paperspace filespace naming conventions
python /workspace/tortoise-wiki-tts/scripts/wikitop25tts.py > /workspace/inputs/wikitop25.txt
python /workspace/tortoise-wiki-tts/read.py --voice train_lescault --preset fast --output_path=/workspace/outputs/wikitop25 --textfile=/workspace/inputs/wikitop25.txt  2>&1 | tee -a /workspace/logs/wiki25log.txt
