#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate melisa
#pip install something...
cp ~/melisa/melisa.sh ~/
cd ..
conda deactivate
