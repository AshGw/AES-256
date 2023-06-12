apt-get update -y
apt-get install -y curl
apt-get install -y git
pip install --upgrade pip
pip install virtualenv
virtualenv vvv
source vvv/bin/activatec
curl -sSfL https://raw.githubusercontent.com/AshGw/AES-256/main/important/setup.sh | bash
