## Melisa
### Description
Melisa is a windowed application based on jupyter qtconsole, using the sagemath kernel.
What I have done: the menu has been updated with the ability to save the results of work in the .ipynb format and the ability to open the created .ipynb documents in the current or in a new window.
Here is the full cycle from installation to launch:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda create -n melisa sage python=3.10
conda activate melisa
pip install jupyter qtconsole
pip install PyQt5
python3 melisa.py
```

### Goal
To build a portable executable file. I can't do it yet :( I'll be glad for any help!

