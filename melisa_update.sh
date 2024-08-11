#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate melisa
#pip install something...
cp ~/melisa/melisa.sh ~/
chmod +x melisa.sh
cd ..
chmod +x melisa.sh
conda deactivate

