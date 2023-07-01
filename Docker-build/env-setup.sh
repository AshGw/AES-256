#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  apt-get update -y
  apt-get install -y git
  pip install --upgrade pip
  pip install virtualenv
  virtualenv vvvl
  . vvvl/bin/activate

elif [[ "$OSTYPE" == "darwin"* ]]; then
  brew update
  brew install git
  pip3 install --upgrade pip
  pip3 install virtualenv
  virtualenv vvvm
  . vvvm/bin/activate

elif [[ "$OSTYPE" == "win"* ]]; then
  python.exe -m pip install --upgrade pip
  pip3 install virtualenv
  python -m venv vvvw
  vvvw\\Scripts\\activate.ps1

else
  echo 'Could not automate this process on this system please install this manually'
  exit 1
fi
