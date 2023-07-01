#!/bin/bash

git clone https://github.com/AshGw/AES-256.git
cd AES-256 || exit
rm -rf dist
rm -rf build
rm -rf AshCrypt.egg-info
if [[ "$OSTYPE" == "win"* ]]; then
  python.exe -m pip install --upgrade pip
else
  pip install --upgrade pip
fi
pip install -r important/requirements.txt
python setup.py develop

