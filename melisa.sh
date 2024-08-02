#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate melisa
cd ~/melisa
python3 melisa.py
conda deactivate 

