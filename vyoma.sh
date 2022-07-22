#!/bin/bash

export PS1='\[\033[01;32m\]vyoma\[\033[00m\] \[\033[01;34m\]\w\[\033[00m\] (uptickpro) $ '
brew install icarus-verilog
PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.13
pyenv global 3.8.13
pip install --upgrade pip
pip install cocotb
export PYTHONPATH=/workspace/.pyenv_mirror/user/3.8.13/lib/python3.8/site-packages/pygpi:$PYTHONPATH
cp -r /workspace/.pyenv_mirror/user/3.8.13/lib/python3.8/site-packages/cocotb*  /home/gitpod/.pyenv/versions/3.8.13/lib/python3.8/site-packages/
cp -r /workspace/.pyenv_mirror/user/3.8.13/lib/python3.8/site-packages/pygpi /home/gitpod/.pyenv/versions/3.8.13/lib/python3.8/site-packages/
rm -rf core.*
clear
echo "****** UpTickPro (Evaluation Version) 1.0.0 *******"
echo "Copyright (c) 2022, Vyoma Systems Private Limited"
echo "All Rights Reserved."
