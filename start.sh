#!/bin/bash

apt update && apt upgrade -y
apt install python3 -y
chmod +x .shell/setup.sh
echo 'alias termux-tool="py $HOME/termux/main.py"' >> $HOME/.bashrc
echo 'alias py="python"' >> $HOME/.bashrc
source $HOME/.bashrc
echo "Run"
echo 'source $HOME/.bashrc'
echo 'then you can run termux-tool for start the script'
echo 'thx from ©termuxandlinux'
