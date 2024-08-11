#!/bin/bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
source ~/.bashrc
yes | conda create -n melisa sage python=3.10
eval "$(conda shell.bash hook)"
conda activate melisa
pip install jupyter qtconsole
pip install PyQt5
cp ~/melisa/melisa.sh ~/
chmod +x melisa.sh
cd ..
chmod +x melisa.sh
conda deactivate
