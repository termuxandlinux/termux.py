#!/bin/bash

pkg install x11-repo
pkg install termux-api -y
pkg install termux-x11-nightly -y
echo 'export DISPLAY=:1' >> $HOME/.bashrc
source $HOME/.bashrc
