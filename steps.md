git clone https://github.com/sachinsshetty/IndicTrans2.git


cd IndicTrans2

python3.10 -m venv venv

source venv/bin/activate

pip install torch==2.7.1 torchvision torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu128



root_dir=$(pwd)

git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
export INDIC_RESOURCES_PATH=$root_dir/indic_nlp_resources


## we use version 0.92 which is the latest in the github repo
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
cd indic_nlp_library
python3 -m pip install ./
cd $root_dir


pip install sentencepiece

git clone https://github.com/pytorch/fairseq.git
cd fairseq
python3 -m pip install ./
cd $root_dir

pip install mosestokenizer nltk



git lfs install
git clone https://huggingface.co/adalat-ai/ct2-rotary-indictrans2-en-indic-dist-200M


