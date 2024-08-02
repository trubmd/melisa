#!/bin/bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
source ~/.bashrc
yes | conda create -n melisa sage python=3.10
conda activate melisa
pip install jupyter qtconsole
pip install PyQt5
conda deactivate
